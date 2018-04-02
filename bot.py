client = Bot(description="Lxrd-Bot by TheLxrd#5390", command_prefix="=", pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running Lxrd-Bot 0.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by TheLxrd#5390')
	return await client.change_presence(game=discord.Game(name='Work in progress')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	
@client.command()
async def autor(*args):

	await client.say(":star: Autor to TheLxrd#5390")

token = os.environ.get("token")
print("oof")
Bot.run(token)
