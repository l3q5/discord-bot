import discord
from tolkien import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print("logged in ")

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "bot":
        if user_message.lower() == "h":
            await message.channel.send(f"oieee {username}!")
            return
        elif user_message.lower() == "cu podre":
            await message.channel.send(f"bluezaosso {username}!")
            return

client.run(TOKEN)
