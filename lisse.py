import os
import discord
import json

from dotenv import load_dotenv
from discord.ext import commands
from botutils import *
from pprint import pprint

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

autoJoinThreadDict = {}
try:
    with open("autoJoinUsers.json", "r") as f:
        rawUserDict = json.load(f)
        for user in rawUserDict:
            autoJoinThreadDict[int(user)] = rawUserDict[user]
    print("Users read successfully")
except FileNotFoundError:
    print('JSON file does not exist')
except json.decoder.JSONDecodeError:
    print('JSON file is not valid')

pprint(autoJoinThreadDict)

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command(name='HelloThere')
async def _helloThere(ctx):
    print("Received command: HelloThere")
    await ctx.send('General Kenobi!')

@bot.command(name='WTF')
async def _wtf(ctx):
    print("Received command: WTF")
    await ctx.send('Var är Boten?')

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
    global autoJoinThreadDict
    print('Received command: autoJoinThreads')
    key = ctx.channel.id
    if key not in autoJoinThreadDict:
        autoJoinThreadDict[key] = []
    channel = autoJoinThreadDict[key]
    userId = ctx.author.id
    if userId not in channel:
    	autoJoinThreadDict[key].append(ctx.author.id)

    with open("autoJoinUsers.json", "w") as f:
        # f.write(json.dumps(autoJoinThreadDict))
        f.write("asdf")

    pprint(autoJoinThreadDict)

    await ctx.send("Du kommer nu bli automatiskt tillagd i trådar som skapas i den här kanalen")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_thread_create(thread):
    global autoJoinThreadDict
    print(f'Thread created in channel {thread.parent.id}')
    users = autoJoinThreadDict.get(f'{thread.parent_id}', [])
    print(f'Adding following users to channel: {users}')
    for user in users:
        print('Adding user:', user)
        await thread.add_user(discord.Object(id=user))

bot.run(token)
