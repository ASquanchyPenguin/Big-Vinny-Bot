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
version = "0.3"

# Log the bot into Discord
@client.event
async def on_ready():
    print("Succesfully logged in as {0.user}!".format(client))
    print("{} is running version {}.".format(name, version))
# end on_ready()

# Called when the bot receives a message
@client.event
async def on_message(message):
    # Prevents the bot from responding to itself
    if message.author == client.user:
        return
        
    # Variables to determine if and how the bot should respond
    mentioned = client.user.mentioned_in(message)
    content = message.content.lower()
    array = content.split()
    
    # Check for built-in commands
    if mentioned and any(word in content for word in botkb.commands):
        if len(array) > 0:
            await run_command(array[1], message.channel)
            return
    
    # Checks if the bot should respond
    if mentioned or any(word in content for word in botkb.aliases):
        await message.channel.send("I should respond")
        
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