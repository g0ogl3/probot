import discord
from random import choice
from config import TOKEN
from discord.ext import commands
import os 
print(os.listdir('images'))
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
@bot.command()
async def mem(ctx):
    files_list = os.listdir('images')
    await ctx.send(file=discord.File(f"images/{choice(files_list)}"))
print(os.listdir('images/animals'))
@bot.command()
async def animals(ctx):
    files_list = os.listdir('images/animals')
    await ctx.send(file=discord.File(f'images/animals/{choice(files_list)}'))
bot.run(TOKEN)
