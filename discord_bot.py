# Author: Riley Lynn Nairn
# Date: 2020 August 16
# Description: Discord bot for Trans Pride

import discord  # https://github.com/Rapptz/discord.py
from datetime import *
from discord.ext import commands

token = None # Obfuscated for GitHub
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, '(' + str(bot.user.id) + ').')
    print('------')


bot.run(token)
