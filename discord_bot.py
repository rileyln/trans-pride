# Author: Riley Lynn Nairn
# Date: 2020 August 16
# Description: Discord bot for Trans Pride

import discord  # https://github.com/Rapptz/discord.py
from datetime import *
from discord.ext import commands

token = None  # Obfuscated for GitHub
bot = commands.Bot(command_prefix='!t')


@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, '(' + str(bot.user.id) + ').')
    print('------')

    today = date.today()
    day_of_week = today.weekday()
    print(today)

    if day_of_week == 0:
        print('Today is Monday.')
    elif day_of_week == 1:
        print('Today is Tuesday.')
    elif day_of_week == 2:
        print('Today is Wednesday.')
    elif day_of_week == 3:
        print('Today is Thursday.')
    elif day_of_week == 4:
        print('Today is Friday.')
    elif day_of_week == 5:
        print('Today is Saturday.')
    elif day_of_week == 6:
        print('Today is Sunday.')
    else:
        print('Not a valid day of the week.')


@bot.command()
async def welcome(context):
    await context.send('Welcome to Trans Pride! Please go to #role-selection to set your pronouns.')


bot.run(token)
