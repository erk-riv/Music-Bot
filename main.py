import discord
from discord.ext import commands
import os
import YTSource

cogs = [YTSource]
my_secret = os.environ['KEY']
client = commands.Bot(command_prefix = '-', intents = discord.Intents.all())
for i in range(len(cogs)):
  cogs[i].setup(client)
  
#my_secret = os.environ['KEY']
#client = commands.Bot(command_prefix = '-', intents = discord.Intents.all())
client.run(os.getenv('KEY'))