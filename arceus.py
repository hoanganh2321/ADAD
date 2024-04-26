import discord
import requests
import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Kaioshin Dev🔥"))
    print(f"Đăng nhập với tên {bot.user}")

allowed_channels = [1231100851347525692]

@bot.event
async def on_message(message):
    if message.author != bot.user and message.content.startswith("https://spdmteam.com/key-system-1?hwid="):
        if message.channel.id not in allowed_channels:
            return

        start_time = datetime.datetime.now()
        api = 'https://stickx.top/api-arceusx/?hwid='
        api_key = 'E99l9NOctud3vmu6bPne'
        hwidd = message.content.replace("https://spdmteam.com/key-system-1?hwid=", "")
        hwid = hwidd.replace("&zone=Europe/Rome&os=android", "")

        wait_embed = discord.Embed(title="Bypassing...! ⏳", description="Vui Lòng Chờ Trong Giây Lát", color=0xffff00)
        wait_embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
        wait_message = await message.reply(embed=wait_embed)

        response = requests.get(f"{api}{hwid}&api_key={api_key}")

        json_data = response.json()
        key = json_data.get("key")

        if key == "Invalid HWID":
            embed = discord.Embed(title="Lỗi ❌", description="```Link Sai```", color=0xFF0000)
            embed.add_field(name="Your Link:", value=f"```\n{message.content}\n```", inline=False)
        else:
            embed = discord.Embed(title="Status:", description=f"```{key}```", color=0x00ff00)
            embed.add_field(name="Your Link:", value=f"```\n{message.content}\n```", inline=False)
            embed.set_thumbnail(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdml5dDVidHdvcjJ6Njdza2N6eHJnODMxaHIwZWI2emN3aXo0ejNwaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wkW0maGDN1eSc/giphy.gif")
            embed.set_footer(text=f"| Bot by Kaioshin |")
            embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
            print(key)

        await wait_message.edit(embed=embed)

    await bot.process_commands(message)

@bot.command()
async def setchannel(ctx):
    if ctx.author.guild_permissions.administrator:
        allowed_channels.append(ctx.channel.id)
        await ctx.send("# This channel is now set for bypass.")
    else:
        await ctx.send("# Only Admin can use.")

bot.run('TOKEN')
