from django.contrib.auth import models

class DiscordUserOAuth2Manager(models.UserManager):
    def create_new_discord_user(self, user):
        new_user = self.create(
            id=user['id'],
            avatar=user['avatar'],
            public_flags=user['public_flags'],
            flags=user['flags'],
            locale=user['locale'],
            mfa_enabled=user['mfa_enabled'],
            username=user['username'],
            discriminator=user['discriminator'],
            access_token=user['access_token']
        )
        return new_user

    def create_new_discord_user_guild(self, guild, user):
        new_guild = self.create(
            id=guild['id'],
            name = guild['name'],
            icon = guild['icon'],
            owner = guild['owner'],
            permissions = guild['permissions'],
            discord_user = user
        )