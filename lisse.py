import os
import discord
import json

from dotenv import load_dotenv
from discord.ext import commands
from botutils import *

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

autoJoinThreadDict = {}
try:
    f = open("autoJoinUsers.json", "r")
    autoJoinThreadDict = json.load(f)
    f.close()
except FileNotFoundError:
    print('JSON file does not exist')
except json.decoder.JSONDecodeError:
    print('JSON file is not valid')

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

@bot.command(name='autoJoinThreads')
async def _threadJoin(ctx):
    print('Received command: autoJoinThreads')
    key = ctx.channel.id
    if key not in autoJoinThreadDict:
        autoJoinThreadDict[key] = []
    autoJoinThreadDict[key].append(ctx.author.id)

    f = open("autoJoinUsers.json", "w")
    f.write(json.dumps(autoJoinThreadDict))
    f.close()

    await ctx.send("Du kommer nu bli automatiskt tillagd i trådar som skapas i den här kanalen")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_thread_create(thread):
    print(f'Thread created in channel {thread.parent.id}')
    users = autoJoinThreadDict.get(f'{thread.parent_id}', [])
    for i in range(len(users)):
        print(f'Adding user: {users[i]}')
        await thread.add_user(discord.Object(id=users[i]))


bot.run(token)
