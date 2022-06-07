# Package Imports
import discord
from discord.ext import commands

import datetime

class Timeout_Command(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @staticmethod
    async def timeout(interaction,user,duration,reason):

        timeout_duration = datetime.datetime.now().timestamp() + (duration * 60)

        await user.timeout(timeout_duration, reason=reason)

        embed = discord.Embed(

            title = None,
            description = f"{user.mention} has been timed out for {duration} minutes.",
            colour=discord.Colour.red()

        )

        await interaction.respond(embed = embed)

    @discord.slash_command(

        name="timeout",
        description="Time out a user."

    )
    async def timeout_slash(
        
        self,
        interaction: discord.Interaction,
        user: discord.Option(discord.Member, description="User to timeout."),
        duration: discord.Option(int, min_value=1, max_value=120, default=30, description="Duration of timeout (minutes)."), 
        reason: discord.Option(str, default="No reason provided.", description="Reason for timeout.")

    ):

        await self.timeout(interaction, user, duration, reason)


        

def setup(bot):

    bot.add_cog(Timeout_Command(bot))

