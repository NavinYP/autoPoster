import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PATH = os.getenv('FOLDER_PATH')

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def pic(channel, idol):
    fileList = os.listdir(f'{PATH}/{idol}')
    print(fileList)
    for i in range(5):
        await channel.send(file=discord.File(f'{PATH}/{idol}/{random.choice(fileList)}'))

client.run(TOKEN)
