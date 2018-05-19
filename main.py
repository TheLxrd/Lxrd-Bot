import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='?')

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Nick uzytkownika: {}".format(user.name))
    await bot.say("ID uzytkownika: {}".format(user.id))
    await bot.say("Status uzytkownika: {}".format(user.status))
    await bot.say("Najwyzsza rola/ranga: {}".format(user.top_role))
    await bot.say("Data dołączenia: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("**{} zostal wyrzucony!".format(user.name))
    await bot.kick(user)
  

bot.run("NDMwMDY1MDUxMDM5MTcwNTcw.DeHaWQ.w21jv_LsIP5mrFjvgqxvRw5ZtI4")
