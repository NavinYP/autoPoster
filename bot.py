import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run('Njk2MDIwNDMxOTQ1MzM0ODA2.Xoipxg.6u2_uwC3zPVunFyTnPS92a3SpY4')