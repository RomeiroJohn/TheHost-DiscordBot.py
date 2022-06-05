from discord.ext import commands
import discord


class embeds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="info")
    async def infobot(self,msg):
        title = "The Host - Bot settings"
        desc = "A list with all the bot features"
        color = 0x000000
        embed = discord.Embed(title=title, description=desc, color=color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/702019138033549312/980990345317855262/WhatsApp_Image_2022-05-30_at_21.24.16.jpeg")
        embed.set_author(name="The Host")
        embed.set_footer(text="J.#5211", icon_url="https://cdn.discordapp.com/avatars/208652904909766658/3a55bc4af8ce9eee26b984e89e986e2c.webp?size=32")
        embed.add_field(name="$info",value="send this list to the user",inline=False)
        embed.add_field(name="$limpar 'Ammount'", value="This command can clear the chat by passing a quantity", inline=False)
        await msg.send(embed=embed)



def setup(bot):
    bot.add_cog(embeds(bot))
