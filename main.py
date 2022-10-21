import os
import sys
import dotenv
import Play
import SupportCommands
import DevCommands
from datetime import datetime
from discord.ext import commands
from discord import Intents
from asyncio import sleep
from DevCommands import get_current_time

os.chdir(sys.path[0]) # Run bot in current directory
dotenv.load_dotenv()  # Load .env file

if not os.path.exists('logs'):
    os.mkdir('logs')

is_running = True
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


def get_switch_time():
    return datetime.now().strftime('%m%h')


@client.event
async def on_ready():
    print('Cobain here')


@client.command()
async def helps(ctx):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    await DevCommands.write_logs(ctx, "helps")
    await SupportCommands.helps(ctx)


@client.command()
async def play(ctx, *args):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    msg = "play " + ' '.join(args)
    await DevCommands.write_logs(ctx, msg)
    await Play.play(ctx, *args)


@client.command()
async def replay(ctx, *args):
    if get_current_time() == "12-06-2022":
        return await ctx.send("Angron42 happy birthday!") #🥰

    msg = "play " + ' '.join(args)
    await DevCommands.write_logs(ctx, msg)
    await Play.replay(ctx, *args)


@client.command()
async def leave(ctx):
    if get_current_time() == "12-06-2022":
        return await ctx.send("Angron42 happy birthday!") #🥰

    await DevCommands.write_logs(ctx, "leave")
    await SupportCommands.leave(ctx, client)


@client.command()
async def stop(ctx):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    await DevCommands.write_logs(ctx, "stop")
    await SupportCommands.stop(ctx, client)


@client.command()
async def pause(ctx):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    await DevCommands.write_logs(ctx, "pause")
    await SupportCommands.pause(ctx, client)


@client.command()
async def resume(ctx):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    await DevCommands.write_logs(ctx, "resume")
    await SupportCommands.resume(ctx, client)


@client.command()
async def spam(ctx, *args):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    msg = "spam " + ' '.join(args)
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
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    msg = "switch " + key
    await DevCommands.write_logs(ctx, msg)
    if key == get_switch_time():
        global is_running
        is_running = not is_running


@client.command(pass_cotext=True)
async def get(ctx, arg):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    msg = "get " + arg
    await DevCommands.write_logs(ctx, msg)
    await DevCommands.get(ctx, arg)


@client.command()
async def logs(ctx, arg):
    if get_current_time() == "12-06-2022":
        await ctx.send("Angron42 happy birthday!") #🥰

    msg = "logs " + arg
    await DevCommands.write_logs(ctx, msg)
    await DevCommands.get_logs(ctx, arg)


token = os.getenv('TOKEN')
client.run(token)
