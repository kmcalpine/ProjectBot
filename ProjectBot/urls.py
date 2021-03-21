"""ProjectBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, re_path, include
from ProjectBot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user', views.get_authenticated_user, name='get_authenticated_user'),
    path('api/commands.json', views.reporter_view),
    path('api/commands.json/', views.reporter_view),
    path('api/commands', views.default_view, name="entry-point"),
    path('api/commands/', views.default_view, name="entry-point"),
    path('api/commands/<str:cmd>/', views.reporter_view_cmd),
    path('api/commands/<int:id>/', views.reporter_view),
    path('oauth2/login', views.discord_login, name='oauth2_login'),
    path('oauth2/login/redirect', views.discord_login_redirect, name='oauth2_login_redirect'),
    path('api/commands/delete/<int:id>/', views.reporter_view_id_delete),

    re_path(r"^.*$", views.default_view, name="entry-point"),
]