from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def gilgamesh(ctx):
    await ctx.send('人類最古の物語『ギルガメシュ叙事詩』に記された王。 真名は古代メソポタミア文明における、シュメール初期王朝時代のウルク第1王朝の第五代王「ギルガメッシュ」。')



bot.run(token)
