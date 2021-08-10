import os
import discord

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

# this is an object that represents a connection to discord,
# handles events, states and Discord's API
client = discord.Client()

class CustomClient(discord.Client):
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)