import discord
import asyncio
import config
from discord.ext import commands
import os
import requests
import json
from threading import Timer

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="/help"), status=discord.Status.online)

@bot.event
async def on_ready():
    print('Online.')
    await bot.tree.sync()
    print('Synced all commands to all guilds.')
    get_prices()
    print("The bot is ready!")

def get_prices():
    # Getting prices:
    print("Getting prices...")
    print("Getting bazaar prices...")
    bazaar = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
    with open('bz.json', 'w') as bazaar_file:
        json.dump(bazaar, bazaar_file, indent=4)
    print("Bazaar prices ready!")
    print("Prices ready!")
    t = Timer(30.0, get_prices)
    t.start()


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
