import disnake
from disnake.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("-"*20)
        print("Comunity Bot is online!")
        print("Created By Alexjeeuh")
        print("Start date of the bot creation is '31/10/2023'")
        print("-"*20)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot:
            return
        
        msg = message.content.lower()
        Cusswords = (['fuck','shit', 'hoe', 'ass','nigger', 'bitch'])

        #Filter on text -->
        if msg in Cusswords:
            await message.delete()
            await message.channel.send(f'Please Watch you language! {message.author}')
        



def setup(bot: commands.Bot):
    bot.add_cog(events(bot))