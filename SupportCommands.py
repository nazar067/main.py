import discord


async def helps(ctx):
    await ctx.send("$play - command to play music. $play url or keywords\n"
                   "$replay - command to replay music. $replay url or keywords\n"
                   "$leave - command to exit the bot. $leave\n"
                   "$stop - command to stop music. $stop\n"
                   "$pause - command to pause music. $pause\n"
                   "$resume - command to resume music. $resume\n"
                   "$spam - command to spam some text. $spam text how many times to repeat(for example 4) delay in "
                   "seconds(0.5 - 60)\n"
                   "$get - command to view page source code. $get url\n"
                   "$logs - command to view logs. $logs date(for example 8-4-2022)")


async def leave(ctx, client):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


async def stop(ctx, client):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


async def pause(ctx, client):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


async def resume(ctx, client):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")
