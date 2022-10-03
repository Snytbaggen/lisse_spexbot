import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from botutils import *

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command(name='HelloThere')
async def _helloThere(ctx):
    print("Received command: HelloThere")
    await ctx.send('General Kenobi!')

@bot.command(name='VilkenJävlaBot')
async def _vilkenBot(ctx):
    print("Received command: VilkenJävlaBot")
    await ctx.send('Motorboten')

@bot.command(name='Va?')
async def _va(ctx):
    print("Received command: Va?")
    await ctx.send('BRUM')

@bot.command(name='Paragraf17')
async def _seventeen(ctx):
    print("Received command: 17")
    await ctx.send("Det löser sig!")

@bot.command(name="Citat", aliases=['citat'])
async def _quotes(ctx):
    print('Received command: Citat')
    await ctx.send(get_quote())

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

bot.run(token)
