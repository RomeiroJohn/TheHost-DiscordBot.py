from discord.ext import commands
import discord

class avatar(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def showavatar(self,msg,userAvatar: discord.User = None):
        if userAvatar == None:
            embed = discord.Embed(title="This is your avatar")
            embed.set_author(name=msg.author.name)
            embed.set_image(url=msg.author.avatar_url)
            await msg.send(embed=embed)
        else:
            embed = discord.Embed(title="This is " + userAvatar.name + "'s avatar")
            embed.set_author(name=userAvatar.name)
            embed.set_image(url=userAvatar.avatar_url)
            await msg.send(embed=embed)
            
            
            
            
            


def setup(bot):
    bot.add_cog(avatar(bot))