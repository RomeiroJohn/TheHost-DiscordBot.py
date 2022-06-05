from discord.ext import commands
import discord;

class createchannels(commands.Cog): # simple command for create voice and text channel
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="createvoicechannel") # manually voice channel creator
    async def createvoicechannel(self,msg,channelname): # adapt to automatically create temporary channel
        if msg.author.guild_permissions.manage_channels:
            await msg.guild.create_voice_channel(channelname)
        else:
            await msg.send("você não pode criar um canal porque não possui permissão")
    
    @commands.command(name="createtextchannel") # manually text channel creator
    async def createtextchannel(self,msg,channelname): # remove or adapt to something
        if msg.author.guild_permissions.manage_channels:
            await msg.guild.create_text_channel(channelname)
        else:
            await msg.send("você não pode criar um canal porque não possui permissão")

        
        
def setup(bot):
    bot.add_cog(createchannels(bot))