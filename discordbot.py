import requests
import json
import discord
from dotenv import load_dotenv
load_dotenv()
import os

discordBotToken = os.environ.get('TOKEN')

url = "https://reddit-meme-api.herokuapp.com/"

response = requests.request("GET", url)
data = response.json()
memeUrl = data["url"]

client = discord.Client()

@client.event
async def on_ready():
    await client.wait_until_ready()
    await client.get_channel(869105113250275338).send(memeUrl)
    await client.close()

client.run(discordBotToken)