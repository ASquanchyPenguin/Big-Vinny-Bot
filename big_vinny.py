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
name = "Big Vinny"
version = "0.2"

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
        
    # Variables to determine if bot should respond
    mentioned = client.user.mentioned_in(message)
    content = message.content.lower()
    
    # Checks if the bot should respond
    if mentioned or any(word in content for word in botkb.aliases):
        await message.channel.send("I should respond")
# end on_message()

# Run the program based on the bot's token
client.run(token)