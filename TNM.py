import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import trump as t
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
import youtube_song as y
from discord.utils import get

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='saami square ')



@bot.command()
async def entry(ctx):
    await ctx.reply("https://tenor.com/view/jkledits-ajith-thala-ajithkumar-mankatha-gif-13454919")

@bot.command(name = 'kaapathu')
async def save(ctx):
    await ctx.reply('saami square dhan prefix(idhu theriyanum ley)'+"\n"
    '>for stylish thala entry type prefix+entry' + '\n'
    '>for TNEB moment type prefix+hehe' + '\n'
    '>for some arasiyal kisu kisu type prefix+quotes' + '\n'
    '>for flexing on your lifestyle (😜) type prefix+vaazhkai' + '\n'
    '>for songs type prefix+paatu "songname"' + '\n'
    'Ippo poi saami kumdu 🤣😎')

@bot.command(name = 'hehe')
async def bums(ctx):
    await ctx.reply("https://tenor.com/view/eps-edapadi-edapadi-palanisamy-tamil-nadu-cm-cm-gif-15163984")


@bot.command(name = "quotes")
async def moment(ctx):
    val = t.get_quote()
    await ctx.send(val)

@bot.command(name = 'vaazhkai')
async def villain(ctx):
    await ctx.send("https://tenor.com/view/viswasam-ajith-thala2019pongal-thookku-durai-visvasam-viswasam-viswaasam-ak-thala-gif-13176644")

@bot.command(name="paatu")
async def play(ctx, *, query=None):
    if query:
        FFMPEG_OPTS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        video, source = y.search(query)
        voice = get(bot.voice_clients, guild=ctx.guild)

        channel = ctx.author.voice.channel

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if not voice.is_playing():
            voice.play(
                discord.FFmpegPCMAudio(source, **FFMPEG_OPTS),
                after=lambda e: print("done", e),
            )
            voice.is_playing()
            await ctx.send(f"kaila kaasu vaaila dosa (search only saami songs)😎")
        else:
            await ctx.send(f"porumai ah iru da biscothe 🤬")
    else:
        await ctx.send("Paatu search pannu ley bums 🤣")

@bot.event
async def on_ready():
    print(f'{bot.user} is running')
    

bot.run(token)