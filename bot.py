import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')

client.run(TOKEN)
