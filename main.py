import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import asyncio
import emoji

# from translate import translate_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("--"),intents=intents)

languages = []

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello there!')
    await bot.process_commands(message)
    

@bot.command("add")
async def add_language(ctx):
    channel = ctx.channel
    # react = ["📰"]
    
    mes = await channel.send('Which language would you like to add?')
    # for tmp in react:
    #     await mes.add_reaction(tmp)
    
    def check(reaction, user):
        return user == ctx.author
    
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        language = emoji.demojize(str(reaction) + " ")[1:-2]
        languages.append(language)
        await ctx.send("Added " + language)

bot.run(TOKEN)