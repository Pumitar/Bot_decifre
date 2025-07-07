import discord
from discord.ext import commands
import os, random
import requests
from model import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
                file_name = attachment.filename
                file_url = attachment.url
                await attachment.save(f"./img/{file_name}")
                Image_path = f"./img/{file_name}"
                class_name, confidence_score = detect_cat(Image_path)
                response_mensage = f"**prediccion**: {class_name}\n**Confianza**: {confidence_score:.2f}"
                await ctx.send(response_mensage)
                
                
    else:
        await ctx.send("No ingreso ninguna imagen :(")
                
bot.run(os.getenv("DISCORD_TOKEN"))