import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send("🎲 Você tirou " + str(numero) + "!")

@bot.command()
async def meme(ctx):

    imagens = os.listdir('images')
    img_name = random.choice(imagens)

    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def animais(ctx):
    imagens = os.listdir('images/animais')
    img_name = random.choice(imagens)

    with open(f'images/animais/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def jogos(ctx):
    imagens = os.listdir('images/jogos')
    img_name = random.choice(imagens)

    with open(f'images/jogos/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


bot.run("SEU TOKEN")
