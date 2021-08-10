import os
import discord

TOKEN = os.environ['DISCORD_TOKEN']

# this is an object that represents a connection to discord,
# handles events, states and Discord's API
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

client.run(TOKEN)