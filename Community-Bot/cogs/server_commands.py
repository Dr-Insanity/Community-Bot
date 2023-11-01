import disnake
from disnake.ext import commands 


class Server_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#Slash Commands --->
    @commands.slash_command(guild_ids=[1164904954906017898])
    async def ping(self,ctx):
        await ctx.send('pong')
    
#--> Chat Commands
    @commands.command()
    async def purge(self, ctx, custom_amount: int):
        await ctx.channel.purge(limit = custom_amount+1)




def setup(bot: commands.Bot):
    bot.add_cog(Server_Commands(bot))