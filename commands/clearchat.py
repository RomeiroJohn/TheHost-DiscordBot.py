from discord.ext import commands


class clearchat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="limpar")
    async def clear(self,ctx, amount=None):
        try:
            valor = int(amount)
        except:
            await ctx.send("O valor: **`{}`** é invalido :thumbsup:".format(amount))
        if valor < 0:
            await ctx.send("Favor, Digite números positivos")
        else:
            await ctx.channel.purge(limit=valor+1)


def setup(bot):
    bot.add_cog(clearchat(bot))
