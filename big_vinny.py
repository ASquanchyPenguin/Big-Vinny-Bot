# Big Vinny Bot
# Author: ASquanchyPenguin
# Requires discord.py

import discord
import botkb
import config

# Grab the Discord Client
client = discord.Client()

# Bot Token (Requires Local Configuration)
token = config.token

# Bot Information
name = config.name
version = "0.4.2"

# Log the bot into Discord
@client.event
async def on_ready():
    print("Succesfully logged in as {0.user}!".format(client))
    print("{} is running version {}.".format(name, version))
# end on_ready()

# Called when the bot receives a message
@client.event
async def on_message(message):
    # Check if we should respond
    if (message.author == client.user) or (not any(word in message.content for word in botkb.aliases)):
        return

    # Respond to the message
    response = botkb.determine_response(message.content)
    await message.channel.send(response)
# end on_message()

# Run the program based on the bot's token
client.run(token)
