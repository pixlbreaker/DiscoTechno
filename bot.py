import discord
import os
import json
import keep_alive

from discord.ext import commands

# Token and the bot
f = open("info.json")
data = json.load(f)
TOKEN = data['TOKEN']

bot = commands.Bot(command_prefix="!")

# Load function for extensions
@bot.command
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

# Unloads function for extension
@bot.command
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()

# Run the bot
bot.run(TOKEN)