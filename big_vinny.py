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
version = "0.4.1"

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
        
    # Variables to determine how the bot should respond
    prompt = botkb.parse_content(message.content)
    length = len(prompt)
    
    print(length, prompt)
    
    # Was the bot's name mentioned with no context?
    if (length == 0):
        await message.channel.send(botkb.get_response(botkb.mentioned_responses))
        
# end on_message()

async def run_command(cmd, channel):
    if cmd == "!time":
        day = botkb.get_day()
        date = botkb.get_date("%B %d, %Y")
        time = botkb.get_time("%H:%M") 
        await channel.send("It is {}, {} at {}.".format(day, date, time))
    elif cmd == "!version":
        await channel.send("Thanks for asking! I'm running version {}.".format(version))

# Run the program based on the bot's token
client.run(token)