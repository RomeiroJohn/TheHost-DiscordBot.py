from discord.ext import commands


class clearchat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="limpar")
    async def clear(self,msg, amount=None):
        try:
            valor = int(amount)
        except:
            await msg.send("O valor: **`{}`** é invalido :thumbsup:".format(amount))
        if valor < 0:
            await msg.send("Favor, Digite números positivos")
        else:
            await msg.channel.purge(limit=valor+1)


def setup(bot):
    bot.add_cog(clearchat(bot))
