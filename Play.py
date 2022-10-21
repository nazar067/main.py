import json
import traceback

import discord
from asyncio import sleep
from youtube_dl import YoutubeDL
from youtube_search import YoutubeSearch

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}
YDL_OPTIONS = {
    'format': 'worstaudio/best',
    'default_search': 'auto',
    'noplaylist': 'True',
    'simulate': 'True',
    'preferredquality': '192',
    'preferredcodec': 'mp3',
    'key': 'FFmpegExtractAudio'
}


async def play(ctx, *args):
    voice = ctx.guild.voice_client
    if voice is None:
        vc = await ctx.message.author.voice.channel.connect()

    else:

        if ctx.guild.voice_client.channel == ctx.message.author.voice.channel:
            vc = voice
        else:
            await ctx.send('Вы не в одном канале')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')
    else:
        if "." in args[0]:
            await search_url(args[0], vc)
        else:
            search = ""
            for i in args:
                search = str(search) + " " + i
            print(search)
            await search_word(ctx, search, vc)

    # if not vc.is_paused():
    # await vc.disconnect()


async def search_url(url, vc):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']
    vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\nazar\\Documents\\BotServer\\ffmpeg.exe", source=URL,
                                   **FFMPEG_OPTIONS))
    while vc.is_playing():
        await sleep(1)


async def search_word(ctx, word, vc):
    await ctx.send("Ищу")
    yt = YoutubeSearch(word, max_results=1).to_json()
    try:
        yt_id = str(json.loads(yt)['videos'][0]['id'])
        yt_url = 'https://www.youtube.com/watch?v=' + yt_id
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(yt_url, download=False)
        url = info['formats'][0]['url']
        vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\nazar\\Documents\\BotServer\\ffmpeg.exe", source=url,
                                       **FFMPEG_OPTIONS))
        while vc.is_playing():
            await sleep(1)
        # if not vc.is_paused():
        # await vc.disconnect()
    except:
        await ctx.send("Ничего не найдено")


async def replay(ctx, *args):
    voice = ctx.guild.voice_client
    if voice is None:
        vc = await ctx.message.author.voice.channel.connect()

    else:

        if ctx.guild.voice_client.channel == ctx.message.author.voice.channel:
            vc = voice
        else:
            await ctx.send('Вы не в одном канале')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')
    else:
        while ctx.guild.voice_client.channel is not None:
            if "." in args[0]:
                await search_url(args[0], vc)
            else:
                search = ""
                for i in args:
                    search = str(search) + " " + i
                print(search)
                await search_word(ctx, search, vc)
