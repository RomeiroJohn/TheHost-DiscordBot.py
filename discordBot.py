from ast import Try
import asyncio
from distutils.util import change_root
from logging import exception
import string
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
    try:
        valor = int(amount)
    except:
        await ctx.send("O valor: **`{}`** é invalido".format(amount))
    if valor < 0:
        await ctx.send("Favor, Digite números positivos")
    else:
        await ctx.channel.purge(limit=valor+1)



apikey = config("apikey")
bot.run(apikey)