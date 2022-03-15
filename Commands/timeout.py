# Package Imports
import discord
from discord.ext import commands


class Timeout_Command(commands.Cog):

    def __init__(self,bot):

        self.bot = bot
        

def setup(bot):

    bot.add_cog(Timeout_Command(bot))

