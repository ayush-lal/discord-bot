import requests
import json
import discord
# from dotenv import load_dotenv

# app id: 642159110384779286
# public key: efa9241751b1afd235003be73c7ab814067da4255ae1132ff6c505769f410d55




url = "https://reddit-meme-api.herokuapp.com/"

response = requests.request("GET", url)
data = response.json()
memeUrl = data["url"]

TOKEN = 'NjQyMTU5MTEwMzg0Nzc5Mjg2.XcS3Rg.1ln51YcN87AH5yuPeYnS7A5JOgI'
GUILD = 'YTB'

client = discord.Client()

@client.event
async def on_ready():
    await client.wait_until_ready()
    await client.get_channel(869105113250275338).send(memeUrl)
    await client.logout()

client.run(TOKEN)