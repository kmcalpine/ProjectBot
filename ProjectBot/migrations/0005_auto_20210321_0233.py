# Generated by Django 3.1.7 on 2021-03-21 02:33

import ProjectBot.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBot', '0004_discorduser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='discorduser',
            managers=[
                ('objects', ProjectBot.managers.DiscordUserOAuth2Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]