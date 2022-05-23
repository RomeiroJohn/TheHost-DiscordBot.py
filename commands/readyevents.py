from discord.ext import commands
import discord;

class readyevents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #@bot.events => commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game("In {} Servers".format(len(self.bot.guilds)))
        await self.bot.change_presence(activity=activity,status=discord.Status.dnd)
        print("Ready!, connected as {}".format(self.bot.user))


def setup(bot):
    bot.add_cog(readyevents(bot))