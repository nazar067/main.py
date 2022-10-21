import datetime

import discord

import Play
import SupportCommands
import DevCommands
import TrollCommands
from discord.ext import commands
from asyncio import sleep

is_running = True

client = commands.Bot(command_prefix='$')


def get_current_time():
    cur_time = datetime.datetime.now()
    return str(cur_time.minute) + str(cur_time.hour)


@client.event
async def on_ready():
    print('Cobain here')


@client.command()
async def helps(ctx):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    await DevCommands.write_logs(ctx, "helps")
    await SupportCommands.helps(ctx)


@client.command()
async def play(ctx, *args):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "play "
    for i in args:
        msg = str(msg) + " " + i
    await DevCommands.write_logs(ctx, msg)
    await Play.play(ctx, *args)


@client.command()
async def replay(ctx, *args):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "play "
    for i in args:
        msg = str(msg) + " " + i
    await DevCommands.write_logs(ctx, msg)
    await Play.replay(ctx, *args)


@client.command()
async def leave(ctx):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    await DevCommands.write_logs(ctx, "leave")
    await SupportCommands.leave(ctx, client)


@client.command()
async def stop(ctx):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    await DevCommands.write_logs(ctx, "stop")
    await SupportCommands.stop(ctx, client)


@client.command()
async def pause(ctx):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    await DevCommands.write_logs(ctx, "pause")
    await SupportCommands.pause(ctx, client)


@client.command()
async def resume(ctx):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    await DevCommands.write_logs(ctx, "resume")
    await SupportCommands.resume(ctx, client)


@client.command()
async def spam(ctx, *args, ):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "spam "
    for i in args:
        msg = str(msg) + " " + i
    await DevCommands.write_logs(ctx, msg)
    global is_running
    string = None
    repeats = None
    delay = None

    try:
        string = args[0]
        repeats = int(args[1])
        delay = float(args[2])

    except:
        await ctx.send('Изначально пишешь, что нужно спамить, потом количество, потом задержку в секундах (0.5 - 60)')
        return

    if delay < 0.5 or delay > 60:
        await ctx.send('Задержка должна быть в пределах между 0.5 и 60 секундами.')
        return

    for i in range(repeats):
        if not is_running:
            is_running = True
            break
        else:
            await ctx.send(string)
            await sleep(delay)


@client.command(pass_context=True)
async def switch(ctx, key):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "switch " + key
    await DevCommands.write_logs(ctx, msg)
    if key == get_current_time():
        # globals()['is_running'] = not globals()['is_running']
        global is_running
        is_running = not is_running


@client.command(pass_cotext=True)
async def get(ctx, arg):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "get " + arg
    await DevCommands.write_logs(ctx, msg)
    await DevCommands.get(ctx, arg)


@client.command()
async def logs(ctx, arg):
    cur_time = datetime.datetime.now()
    date = str(cur_time.day) + "-" + str(cur_time.month) + "-" + str(cur_time.year)
    if date == "12-6-2022":
        await ctx.send("Angron42 happy birthday!")
    msg = "logs " + arg
    await DevCommands.write_logs(ctx, msg)
    await DevCommands.get_logs(ctx, arg)


token = ''
client.run(token)
