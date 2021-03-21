from django.db import models
from .managers import DiscordUserOAuth2Manager

class Reporter(models.Model):
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

    def is_authenticated(self):
        return True