=#run start.bat
import discord
from discord.ext import commands
import json
import os
import colorama

with open("config.json") as f: #make sure to edit config.json
    config = json.load(f) #basically just retrieves the config.json file

token = config.get("token") #gets the token from config.json

bot = commands.Bot(command_prefix="")

status = config.get("status") #gets the status from config.json

clear = lambda: os.system("cls") #sets a var for clear so if you do clear(), it will execute cls which clears the console

from colorama import Fore, Style #imports colorama for colors in the console

@bot.event #if u don't know this you're dumb
async def on_connect(): #when the bot connects it will execute the code below it
    stream = discord.Streaming(name=status, url=config.get("url")) #basically just sets a streaming variable
    await bot.change_presence(activity=stream) #changes the status to stream
    clear() #clears console
    print(Fore.BLUE + 'Streaming selfbot is on!') #prints blue text that outputs 'Streaming selfbot is on!'

bot.run(token, bot=False) #runs the bot and that is why you need the token var. after the , it says bot=False since we are not running a bot
