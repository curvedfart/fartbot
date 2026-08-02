import discord
import requests
import aiohttp
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content is not None:                
      payload = {"text": message.content}

      async with aiohttp.ClientSession() as session:
          async with session.post("http://127.0.1.1:5000/ai", json=payload) as resp:
              result = await resp.json() 

    await message.channel.send(result["response"])        
 
client.run('your_token')
