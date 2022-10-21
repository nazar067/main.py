import os.path
import sys
import os
import discord
import requests
from datetime import datetime


def get_current_minute():
    cur_time = datetime.now()
    return cur_time.strftime('<%Hh %Mm %Ss>')


def get_current_time():
    cur_date = datetime.today()
    return cur_date.strftime('%d-%m-%Y')


async def get_logs(ctx, arg):
    server = ctx.guild.name
    directory = f'logs/{server}'
    dir_exists = os.path.exists(directory)

    if dir_exists:
        path = f'{directory}/{arg}.txt'
        log_exists = os.path.exists(path)
        if log_exists:
            await ctx.send(file=discord.File(path))
        else:
            await ctx.send('No logs for this date')
    else:
        await ctx.send('No logs for your server')


async def write_logs(ctx, args):
    server = ctx.guild.name
    channel = ctx.message.channel
    author = ctx.message.author.name
    id_user = ctx.message.author
    directory = f'logs/{server}'
    # path = f'E:\\CobainBot\\logs\\{get_current_time()}.txt'
    # check = os.path.isfile(path)
    check_dir = os.path.isdir(directory)
    if check_dir is True:
        path = f'{directory}\\{get_current_time()}.txt'
        check = os.path.isfile(path)
        if check is True:
            file = open(path, 'a')
            text = id_user.mention + "(" + author + ")" + " " + "channel" + "(" + str(
                channel) + ")" + " " + args + " " + get_current_minute()
            file.write(text + '\n')
            file.close()
        else:
            file = open(path, 'w')
            text = id_user.mention + "(" + author + ")" + " " + "channel" + "(" + str(
                channel) + ")" + " " + args + " " + get_current_minute()
            file.write(text + '\n')
            file.close()
    else:
        os.mkdir(directory)
        path = f'{directory}\\{get_current_time()}.txt'
        check = os.path.isfile(path)
        if check is True:
            file = open(path, 'a')
            text = id_user.mention + "(" + author + ")" + " " + "channel" + "(" + str(
                channel) + ")" + " " + args + " " + get_current_minute()
            file.write(text + '\n')
            file.close()
        else:
            file = open(path, 'w')
            text = id_user.mention + "(" + author + ")" + " " + "channel" + "(" + str(
                channel) + ")" + " " + args + " " + get_current_minute()
            file.write(text + '\n')
            file.close()


async def send_text_file(ctx, text):
    file = open('text.txt', 'w', encoding='utf-8')
    file.write(text)
    file.close()
    await ctx.send(file=discord.File('text.txt'))


async def get(ctx, *args):
    try:
        shield = '%42%'
        response = requests.get(args[0])
        content = str(response.content, 'utf-8')
        if content.startswith(shield) and globals()['vs'](content[len(shield):]) != True:
            return False

        if len(content) < 2000:
            await ctx.send(content)
            return

        await send_text_file(ctx, content)

    except Exception:
        e = sys.exc_info()[1]
        await ctx.send(e.args[0])
