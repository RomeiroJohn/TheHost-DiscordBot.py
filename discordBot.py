import asyncio
from distutils.util import change_root
import discord  #discord.py
from discord.ext import commands
from decouple import config


bot = commands.Bot("$")


@bot.event
async def on_ready():
    activity = discord.Game("In {} Servers".format(len(bot.guilds)))
    await bot.change_presence(activity=activity,status=discord.Status.dnd)
    print("Ready!, connected as {}".format(bot.user))


@bot.command(name="oi")
async def sendhi(ctx):
    name = ctx.author.name
    response = "Olá," + name
    
    await ctx.send(response)

@bot.command(name="limpar")
async def clear(ctx, amount=None):
    if amount is None:
        await ctx.send("Favor, digite uma quantidade para limpar")
    else:
        await ctx.channel.purge(limit=int(amount))


apikey = config("apikey")
bot.run(apikey)