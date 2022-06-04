import discord
import random

TOKEN = "NDY3ODg4NDU4NTUyMDQ5Njg0.GsgWSP.Do7eH5ubKeVIZ9jHjeEFVnzx9etIfFJuVcdD18"

client = discord.Client()

@client.event
async def on_ready():
    print('logged in ')

client.run(TOKEN)
