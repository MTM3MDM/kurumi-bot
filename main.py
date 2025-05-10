import discord
from discord.ext import commands
import os  # ✅ 이 줄 추가!

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='쿠루미', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 작동 중!')

@bot.command()
async def 핑(ctx):
    await ctx.send("퐁!")

bot.run(os.getenv("TOKEN"))
