import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from translate import translate_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"),intents=intents)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello there!')
    await bot.process_commands(message)

@bot.command()
async def foo(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)