# ████████╗██╗░░██╗██╗░██████╗  ██╗░██████╗  ░██╗░░░░░░░██╗███████╗██╗██████╗░██████╗░░░░
# ╚══██╔══╝██║░░██║██║██╔════╝  ██║██╔════╝  ░██║░░██╗░░██║██╔════╝██║██╔══██╗██╔══██╗░░░
# ░░░██║░░░███████║██║╚█████╗░  ██║╚█████╗░  ░╚██╗████╗██╔╝█████╗░░██║██████╔╝██║░░██║░░░
# ░░░██║░░░██╔══██║██║░╚═══██╗  ██║░╚═══██╗  ░░████╔═████║░██╔══╝░░██║██╔══██╗██║░░██║░░░
# ░░░██║░░░██║░░██║██║██████╔╝  ██║██████╔╝  ░░╚██╔╝░╚██╔╝░███████╗██║██║░░██║██████╔╝██╗
# ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░  ╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═╝╚═╝░░╚═╝╚═════╝░╚═╝

# Package Imports
import discord
from discord.ext import commands
from discord import command, slash_command

import datetime
import asyncio
import json
import os


# Initialisation
bot = commands.Bot(

    command_prefix = "+",
    case_insensitive = True,
    help_command = None,
    strip_after_prefix = True

)

@bot.event
async def on_ready():

    print("""
████████╗██╗░░██╗██╗░██████╗  ██╗░██████╗  ░██╗░░░░░░░██╗███████╗██╗██████╗░██████╗░░░░
╚══██╔══╝██║░░██║██║██╔════╝  ██║██╔════╝  ░██║░░██╗░░██║██╔════╝██║██╔══██╗██╔══██╗░░░
░░░██║░░░███████║██║╚█████╗░  ██║╚█████╗░  ░╚██╗████╗██╔╝█████╗░░██║██████╔╝██║░░██║░░░
░░░██║░░░██╔══██║██║░╚═══██╗  ██║░╚═══██╗  ░░████╔═████║░██╔══╝░░██║██╔══██╗██║░░██║░░░
░░░██║░░░██║░░██║██║██████╔╝  ██║██████╔╝  ░░╚██╔╝░╚██╔╝░███████╗██║██║░░██║██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░  ╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═╝╚═╝░░╚═╝╚═════╝░╚═╝

    """)

    print("Loading commands...")

    command_dir = os.listdir(f"{os.getcwd()}/Commands")

    # Removes non-module files
    for file in command_dir:

        if not file.endswith(".py"):

            command_dir.remove(file)

    c = 1
    for file in command_dir:
        ex = file[:-3]
        try:
            bot.load_extension(f"Commands.{ex}")
        except Exception as e:
            print(f"Command {ex} failed ({e}). [{c}/{len(command_dir)}]")
        else:
            print(f"Command {ex} loaded [{c}/{len(command_dir)}]")
        finally:
            c+=1

    print("Commands loaded.")

    print("Logged in successfully.")
    

# Config file
data = dict()

try:

    with open("config.json", "r") as config:

        data = json.load(config)

except FileNotFoundError:

    raise Exception("Could not run config.json as it does not exist. Run setup.py to generate a config file, and populate file.")

bot.run(data['token'])


