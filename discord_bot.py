# Author: Riley Lynn Nairn
# Date: 2020 August 16
# Description: Discord bot for Trans Pride

import discord # https://github.com/Rapptz/discord.py
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzQzMjM5OTI3NTYyNzY0Mjg5.XzRyHw.a3lQzyv6mn_QediNuuHTvDZnQLc')

