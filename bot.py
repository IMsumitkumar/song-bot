import os
import discord
from datetime import datetime
from discord.ext import commands

TOKEN = os.environ.get('TOKEN')

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def hello(ctx):
    print(ctx.message.content)
    await ctx.send("hi, sumit!")

@client.command()
async def add_riya(ctx):
    already_in_list = False
    content = ctx.message.content 
    content = content.split(" ")[1:]
    content = " ".join(content)
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                await ctx.channel.send("Opps! you have added it past. Song already in the list")
                already_in_list = True
                return
    
    if not already_in_list:
        with open("song/riya_song.csv", "a") as f:
            f.write(content+"\n")
            await ctx.channel.send(f"Hey Oreo! {content} has been added to your list.")
            return


@client.command()
async def remove_riya(ctx):
    content = ctx.message.content 
    content = content.split(" ")[1:]
    content = " ".join(content)
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                with open("song/riya_song.csv", "r") as f:
                    lines = f.readlines()
                with open("song/riya_song.csv", "w") as f:
                    for line in lines:
                        if line.startswith(content[:3]):
                            continue
                        f.write(line)
                await ctx.channel.send(f"Hey Oreo! {content} has been removed from your list.")
                return
    await ctx.channel.send("Opps! you have not added it past. Song not in the list")


@client.command()
async def add_sumit(ctx):
    already_in_list = False
    content = ctx.message.content 
    content = content.split(" ")[1:]
    content = " ".join(content)
    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                await ctx.channel.send("Opps! you have added it past. Song already in the list")
                already_in_list = True
                return
    
    if not already_in_list:
        with open("song/sumit_song.csv", "a") as f:
            f.write(content+"\n")
            await ctx.channel.send(f"Hey Sumit! {content} has been added to your list.")
            return

@client.command()
async def remove_sumit(ctx):
    content = ctx.message.content 
    content = content.split(" ")[1:]
    content = " ".join(content)
    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                with open("song/sumit_song.csv", "r") as f:
                    lines = f.readlines()
                with open("song/sumit_song.csv", "w") as f:
                    for line in lines:
                        if line.startswith(content[:3]):
                            continue
                        f.write(line)
                await ctx.channel.send(f"Hey Sumit! {content} has been removed from your list.")


@client.command()
async def add_all(ctx):
    already_in_list_riya = False
    already_in_list_sumit = False
    content = ctx.message.content 
    content = content.split(" ")[1:]
    content = " ".join(content)
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                await ctx.channel.send("Opps! you have added it past. Song already in the list")
                already_in_list_riya = True
    
    if not already_in_list_riya:
        with open("song/riya_song.csv", "a") as f:
            f.write(content+"\n")
            await ctx.channel.send(f"Hey Oreo! {content} has been added to your list.")

    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            if line.startswith(content[:3]):
                await ctx.channel.send("Opps! you have added it past. Song already in the list")
                already_in_list_sumit = True
                return
    
    if not already_in_list_sumit:
        with open("song/sumit_song.csv", "a") as f:
            f.write(content+"\n")
            await ctx.channel.send(f"Hey Sumit! {content} has been added to your list.")
            return

@client.command()
async def play_riya(ctx):
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            await ctx.channel.send(f".play {line.strip()}")

@client.command()
async def play_sumit(ctx):
    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            await ctx.channel.send(f".play {line.strip()}")

@client.command()
async def play_all(ctx):
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            await ctx.channel.send(f".play {line.strip()}")

    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            await ctx.channel.send(f".play {line.strip()}")

@client.command()
async def clear_riya(ctx):                                                                    
    with open("song/riya_song.csv", "r") as f:
        lines = f.readlines()
    with open("song/riya_song.csv", "w") as f:
        for line in lines:
            f.write(line)
    await ctx.channel.send("Hey Oreo! Your list has been cleared.")


@client.command()
async def clear_sumit(ctx):
    with open("song/sumit_song.csv", "r") as f:
        lines = f.readlines()
    with open("song/sumit_song.csv", "w") as f:
        for line in lines:
            f.write(line)
    await ctx.channel.send("Hey Sumit! Your list has been cleared.")


@client.command()
async def clear_all(ctx):
    with open("song/riya_song.csv", "r") as f:
        lines = f.readlines()
    with open("song/riya_song.csv", "w") as f:
        for line in lines:
            f.write(line)

    with open("song/sumit_song.csv", "r") as f:
        lines = f.readlines()
    with open("song/sumit_song.csv", "w") as f:
        for line in lines:
            f.write(line)
    await ctx.channel.send("Hey Oreo! Your list has been cleared.")
    await ctx.channel.send("Hey Sumit! Your list has been cleared.")


@client.command()
async def riya_list(ctx):
    all_song = ""
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            all_song += f"> {line}"

    all_song = all_song.strip()
    await ctx.channel.send(f"Hey Oreo! Here is your list:\n{all_song}")

@client.command()
async def sumit_list(ctx):
    all_song = ""
    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            all_song += f"> {line}"

    all_song = all_song.strip()
    await ctx.channel.send(f"Hey Sumit! Here is your list:\n{all_song}")

@client.command()
async def all_list(ctx):
    all_song = ""
    with open("song/riya_song.csv", "r") as f:
        for line in f:
            all_song += f"> Riya  : {line}"

    with open("song/sumit_song.csv", "r") as f:
        for line in f:
            all_song += f"> Sumit: {line}"

    all_song = all_song.strip()
    await ctx.channel.send(f"Here is your list:\n{all_song}")

@client.command()
async def riya_count(ctx):
    with open("song/riya_song.csv", "r") as f:
        lines = f.readlines()
    await ctx.channel.send(f"Hey Oreo! You have {len(lines)} songs in your list.")

@client.command()
async def sumit_count(ctx):
    with open("song/sumit_song.csv", "r") as f:
        lines = f.readlines()
    await ctx.channel.send(f"Hey Sumit! You have {len(lines)} songs in your list.")

@client.command()
async def all_count(ctx):
    with open("song/riya_song.csv", "r") as f:
        lines = f.readlines()
    await ctx.channel.send(f"Hey Oreo! You have {len(lines)} songs in your list.")

    with open("song/sumit_song.csv", "r") as f:
        lines = f.readlines()
    await ctx.channel.send(f"Hey Sumit! You have {len(lines)} songs in your list.")

@client.command()
async def please_help(ctx):
    await ctx.channel.send("""
    **Commands**
    > **!add_all <song>** : Add song to both list
    > **!add_riya <song>** : Add song to riya list
    > **!remove_riya <song>** : Remove song from riya list
    > **!add_sumit <song>** : Add song to sumit list
    > **!remove_sumit <song>** : Remove song from sumit list
    > **!play_riya** : Play riya list
    > **!play_sumit** : Play sumit list
    > **!play_all** : Play both list
    > **!clear_riya** : Clear riya list
    > **!clear_sumit** : Clear sumit list
    > **!clear_all** : Clear both list
    > **!riya_list** : List riya list
    > **!sumit_list** : List sumit list
    > **!all_list** : List both list
    > **!riya_count** : Count riya list
    > **!sumit_count** : Count sumit list
    > **!all_count** : Count both list
    > **!please_help** : Help
    """)



client.run(TOKEN)


