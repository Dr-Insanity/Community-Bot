import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv
load_dotenv('.env')

def run():
    bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
    bot.remove_command('help')
    bot.load_extensions("cogs/")
    bot.run(os.getenv('token'))
run()