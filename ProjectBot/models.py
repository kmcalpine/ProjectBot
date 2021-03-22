from django.db import models
from .managers import DiscordUserOAuth2Manager

class Reporter(models.Model):
    guild = models.CharField(max_length=70)
    full_name = models.CharField(max_length=70)
    msg_response = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    discriminator = models.IntegerField()
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)
    access_token = models.CharField(max_length=100)

    def is_authenticated(self):
        return True

class DiscordUserGuilds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    owner = models.BooleanField()
    permissions = models.CharField(max_length=100)
    discord_user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)