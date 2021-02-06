# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.ext.tasks import loop

import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#-------------lol----------------------

from riotwatcher import LolWatcher, ApiError
import pandas as pd
api_key = '<Api_Key>'
watcher = LolWatcher(api_key)
region = 'euw1'

def lol_api(username):
    me = watcher.summoner.by_name(region, username)
    return me['summonerLevel']

def rank_api(username):
    me = watcher.summoner.by_name(region, username)
    return watcher.league.by_summoner(region, me['id'])

@bot.command(name='rank', help='Do !!rank <username>')
async def nine_nine(ctx, username:str):
    x = rank_api(username)
    embed = discord.Embed(title=f"__**Results:**__", color=0x03f8fc,timestamp= ctx.message.created_at)
    if x != []:
        try:
            #response = "Your Rank is : {} {} with {} wins and {} losses".format(x[0]['tier'],x[0]['rank'],x[0]['wins'],x[0]['losses'])
            response = embed.add_field(name=f'**{x[0]["tier"]}**', value=f'> Rank: {x[0]["rank"]}\n> Wins: {x[0]["wins"]}\n> Losses: {x[0]["losses"]}',inline=False)
            await ctx.send(embed=response)
        except Exception as e:
            print(e)
            response = "Try Again"
            await ctx.send(response)
    else :
        response = "You are not ranked..."
        await ctx.send(response)



@bot.command(name='summoner', help='Do !!summoner <username>')
async def nine_nine(ctx, username:str):
    try:
        response = "Your Summoner Level is : "+str(lol_api(username))
    except :
        response = "Try Again"

    await ctx.send(response)



#----------------gamble--------------------
@bot.command(name='gamble', help='Do !!gamble <points>')
async def gamble(ctx, points:int):
    print(ctx.message.author)
    x = random.randrange(100)
    print(x)
    if x < 50 :
        response = "Sorry u lost your points"
    else :
        response = "YaaY, you won "+str(points*2)+" points"
    await ctx.send(response)



#----------------guess the number----------------
def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel

async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await bot.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            continue

@bot.command(name='guess')
async def guess(ctx):
    n = random.randint(1, 99)
    print(n)
    await ctx.send("Enter a number from 1 to 99 !")
    guess = await get_input_of_type(int, ctx)

    while n != guess:
        if guess < n:
            await ctx.send("guess is low")
            guess = await get_input_of_type(int, ctx)
        elif guess > n:
            await ctx.send("guess is high")
            guess = await get_input_of_type(int, ctx)


    await ctx.send("you guessed it! :tada: :tada: :tada: ")

#---------------bad word---------------
"""
@bot.event
async def on_message(message):
    for mention in message.mentions :
        if "NouAr" in mention.name:
            await message.channel.send("Dok yji sidek NouAr :crown:, matat9ala9ch")
            break
"""
#------------ping test------------
@bot.command(name='ping')
async def ping(ctx):
    ping_ = bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")

#------------go to voice channel and play---------------
@bot.command(name='play', help='Do !!play kes-jus or n3ichou...')
async def vuvuzela(ctx,meme:str):
    # grab the user who sent the command
    channel=ctx.message.author.voice.channel
    # only play music if user is in a voice channel
    if channel!= None:
        # create StreamPlayer
        vc= await channel.connect()
        try:
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", 'mp3/'+source=meme+'.mp3'), after=lambda: print('done'))
        except Exception as e:
            raise

        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
        await vc.disconnect()
    else:
        await ctx.send('User is not in a channel.')

#--------------change "is watching" every 5 sec--------------

watch_list = ["Netflix", "TV", "Anime", "YouTube", "You"]

@loop(seconds=5)
async def watch_change():
    watch=random.choice(watch_list)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watch))


@watch_change.before_loop
async def watch_change_before():
    await bot.wait_until_ready()


#handle errors
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


watch_change.start()
bot.run(TOKEN)
