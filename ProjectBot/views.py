from rest_framework import viewsets
from django.core import serializers
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import redirect
from .models import Reporter
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render
import json
import requests



@login_required(login_url='/oauth2/login')
def guild_view(request):
    template_name = "index.html"
    return render(request, template_name)

@login_required(login_url='/oauth2/login')
def default_view(request, server):
    template_name = "index.html"
    return render(request, template_name)

auth_url_discord = 'https://discord.com/api/oauth2/authorize?client_id=778669779141263391&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify'

def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)

@login_required(login_url='/oauth2/login')
def get_authenticated_user(request: HttpRequest):
    return JsonResponse({ 'msg': 'authenticated' })


def discord_login_redirect(request: HttpRequest):
    print('here')
    code = request.GET.get('code')
    print(code)
    user = exchange_code(code)
    print(user)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    print(discord_user)
    login(request, discord_user)
    return redirect('/guilds')

def exchange_code(code: str):
    data = {
        'client_id': '778669779141263391',
        'client_secret': '',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/oauth2/login/redirect',
        'scope': 'identify guilds bot'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    print(response)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v8/users/@me', headers= {
        'Authorization': 'Bearer %s' % access_token
    })
    print(response.json())

    user = response.json()
    user['access_token'] = access_token

    return user

@login_required(login_url='/oauth2/login')
def discord_user_guilds(request):
    user = None
    if request.user.is_authenticated():
        print(request.user.id)
        user = request.user
        response = requests.get('https://discord.com/api/v8/users/@me/guilds', headers={
            'Authorization': 'Bot ',
        })
        print('here')
        print(response.json()[0])

        result = {}
        i = 0
        for item in response.json():
            result[i] = item
            i += 1
        return JsonResponse(result)


    return JsonResponse({'msg': 'authenticated'})

@login_required(login_url='/oauth2/login')
def discord_commands(request):
    print(request)
    return JsonResponse({ 'msg': 'authenticated' })

@login_required(login_url='/oauth2/login')
def reporter_view(request, server):
    print('here')
    if request.method == 'POST':
        print('POSTING')
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        Reporter.objects.create(
            guild = server,
            full_name = data['cmd_name'],
            msg_response = data['msg_response']
        )
    queryset = Reporter.objects.filter(guild=server);
    qs_json = serializers.serialize('json', queryset)
    return HttpResponse(qs_json, content_type='application/json')

def reporter_view_id(request, server, id):
    queryset = Reporter.objects.filter(guild=server).filter(full_name=id)
    qs_json = serializers.serialize('json', queryset)

    return HttpResponse(qs_json, content_type='application/json')

@login_required(login_url='/oauth2/login')
def reporter_view_id_delete(request, server, id):
    queryset = Reporter.objects.filter(id=id).delete()
    return HttpResponse(None, content_type='application/json')

