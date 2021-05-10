# Big Vinny Bot
# Author: ASquanchyPenguin
# Requires discord.py

import discord
import config

# Grab the Discord Client
client = discord.Client()

# Bot Token (Requires Local Configuration)
token = config.token

# Bot Information
name = "Big Vinny"
version = "0.1"

# Log the bot into Discord
@client.event
async def on_ready():
    print("Succesfully logged in as {0.user}!".format(client))
    print("{} is running version {}.".format(name, version))
# end on_ready()

# Called when the bot receives a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith("ding"):
        await message.channel.send("dong")
# end on_message()

# Run the program based on the bot's token
client.run(token)