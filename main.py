import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import asyncio
import emoji

from languages import language_dat

from translate import translate_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(""),intents=intents)

languages = []

@bot.event
async def on_message(message):
    if  bot.user.mentioned_in(message) and message.content.startswith('<@' + str(bot.user.id) + '>') and message.content.endswith(str(bot.user.id) + '>'):     
        await message.channel.send('Hello there!')

    elif bot.user.mentioned_in(message) and message.content.startswith('<@' + str(bot.user.id) + '>'):
        if len(languages) > 0:
            for language in languages:
                text = message.content
                start = text.find(">") + 1
                text = text[start:]
                translated_message, source_langauge = translate_message(text, target_lang=language)
                if source_langauge != language:
                    await message.reply(language_dat[language]["Icon"] + ": " + translated_message)
        else:
            await message.channel.send('Please add languages using ++ command!')

    await bot.process_commands(message)
    

@bot.command("++")
async def add_language(ctx):
    if not ctx.message.content.startswith("++"):
        return
    
    channel = ctx.channel
    react = ["🇬🇧", "🇪🇸", "🇩🇪","🇫🇷"]
    
    mes = await channel.send('Which language would you like to add?')
    for tmp in react:
        await mes.add_reaction(tmp)
    
    def check(reaction, user):
        return user == ctx.author
    
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        print(str(reaction))
        flag = emoji.demojize(str(reaction) + " ")[1:-2]

        language = None

        for k,v in language_dat.items():
            if flag in v['Flags']:
                language = k
                break

        if language != None and language not in languages:
            languages.append(language)
            await ctx.send('Added ' + language_dat[language]["Language"])
        elif language in language_dat.keys():
            await ctx.send(language + ' is already added!')
        else:
            await ctx.send('Please make a valid selection!')

@bot.command("--")
async def remove_language(ctx):
    await ctx.send('remove!')

@bot.command("list")
async def list_languages(ctx):
    if len(languages) > 0:
        await ctx.send('Currently translating to the following languages:')
        for language in languages:
            await ctx.send(language)
    else:
        await ctx.send('Use the ++ command to add a language!')

bot.run(TOKEN)