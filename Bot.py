import asyncio

import discord

 
client = discord.Client() 

@client.event
async def on_ready():
	print('Du bist eingeloggt als User{}' .format(client.user.name ))
	client.loop.create_task(status_task())

async def  status_task():
	 await client. change_presence(activity=discord.Game('Hi ich bin ein Bot'), status=discord.Status.online)
	 await asyncio.sleep(2)
	 await client. change_presence(activity=discord.Game('Bots sind Cool'), status=discord.Status.online)
	 await asyncio.sleep(2)

@client.event
async def on_message(message):
	 if message.author.bot:
	 	 return
	 if 'Wie geht es dir?' in message.content:
	 	 await message.channel .send('gut ')

client.run(os.getenv('Tocken'))
