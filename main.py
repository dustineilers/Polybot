import os
import discord

from discord.ext import commands

TOKEN = "MTE0NDY0MTY5NDI4NTk3MTU2Ng.GPkGqc.2e-X6rdTBKjZzqhv8m8dRKnn2_gvXI52Kd8EoA"

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