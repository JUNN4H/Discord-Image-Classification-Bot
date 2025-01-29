import discord
from discord.ext import commands
from detector import detect_object

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
async def save(ctx,):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = "images/" + attachment.filename
                await attachment.save(file_path)
                await ctx.send(f'Gambar {file_path} telah disimpan!')
                
                result = detect_object(file_path)
                
                await ctx.send(F"Ini gambar {result}")
            else:
                await ctx.send(f'{attachment.filename} bukanlah gambar!')
    else:
        await ctx.send('Tidak ada lampiran gambar!')
    
bot.run("")
