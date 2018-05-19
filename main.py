import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='?')

DEIN_USERNAME = "307189697199996928"
chat_filter = ["DISCORD.GG/"]
bypass_list = ["307189697199996928"]

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** Twoja wypowiedź została zablokowana!")
                except discord.errors.NotFound:
                    return 
    #if message.content == "cookie":
        #await client.send_message(message.channel, ":cookie:")
    #if message.content.upper().startswith('?PING'):
        #userID = message.author.id
        #await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    #if message.content.startswith('?test'):
        #userID = message.author.id
        #await client.send_message(message.channel, "Witaj, <@%s> na **Cookie Community**!" % (userID))
        #await client.send_message(message.channel, "<#444938789366792192> - regulamin serwera")
        #await client.send_message(message.channel, "<#444938637164150784> - wprowadzenie na serwerze")
    #if message.content.upper().startswith('<@4325391499422722>'):
        #userID = message.author.id
        #await client.send_message(message.channel, "<@%s>, mój prefix to `?`!" % (userID))
    #if message.content.upper().startswith('2+2'):
        #userID = message.author.id
        #await client.send_message(message.channel, "<@%s>, **2+2** = **4**" % (userID))
    if message.content.upper().startswith('?DEV'):
        if message.author.id == "307189697199996928":
            await client.send_message(message.channel, ":ok_hand: | Rzeczy deweloperskie bota wysłane na pv!")
        else:
            await client.send_message(message.channel, ":finger: | Nie masz uprawnień do tego! (Musisz być deweloperem)")
    if message.content.upper().startswith('?UPR'):
        userID = message.author.id
        if "447347555077193728" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień serwer: **Najwyższy Komandor**" % (userID))
        if "425292756437696522" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień serwer: **Użytkownik**" % (userID))
        if "445084050823053315" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień serwer: **Support**" % (userID))
        if message.author.id == "447347723075715074": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień bota: **Główny Komandor**" % (userID))
        if message.author.id == "372026600989917195": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień bota: **Support bota**" % (userID))
        if message.author.id == "344378141290266625": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>, twój poziom uprawnień bota: **Wyższy support**" % (userID))
@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

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
   
@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "Witaj, **{0}** na **{1}**! Baw się tu dobrze. :wink:".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)

@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "Żegnaj **{0}**, było nam miło ciebie gościć ".format(member.mention)
    await client.send_message(serverchannel, msg)

bot.run("TOKEN")
