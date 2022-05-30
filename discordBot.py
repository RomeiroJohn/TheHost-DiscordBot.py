from discord.ext import commands
from decouple import config
import os

bot = commands.Bot("$")

def loadcogs(bot):
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

loadcogs(bot)

apikey = config("apikey")
bot.run(apikey)