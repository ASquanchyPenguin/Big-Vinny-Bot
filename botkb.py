# Big Vinny Bot Knowledge Base
# Author: ASquanchyPenguin
# Used to tweak big_vinny.py

from datetime import date
from datetime import datetime

from random import choice 

# Common lists used by the bot
aliases = ["<@!841002321751441428>", "big vinny", "vinny", "yelly", "chig winny", "big beep beep"]
commands = ["!version", "!time"]
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
keys = ["get lit"]

# Common bot responses
mentioned_responses = ["Don't at me", "Hmm?", "What you want B?", "Did you have something to say?"]
unknown_responses = ["what", "I don't know what you mean.", "Was that even English?", "Right...", "bruh", "Why don't you rethink that one"]

# Common tasks for the bot

def get_date(format):
    today = date.today()
    time = today.strftime(format)
    return time
# end get_date()

def get_day():
    today = date.today()
    index = today.weekday()
    return weekdays[index]
# end get_day()

def get_response(data):
    return choice(data)
# end get_response()

def get_time(format):
    today = datetime.now()
    time = today.strftime(format)
    return time
# end get_time()

def parse_content(content):
    # Remove name
    for alias in aliases:
        content = content.replace(alias, '')
    
    # Force lower case and strip the content
    content = content.lower().strip()
    
    return content.split()
# end parse_content()

def permit_lit():
    day = date.today().weekday()
    hour = int(get_time("%H"))
    
   # Sun - Thur (risky lit)
    if ((day == 6 or day < 4) and hour > 17):
       return "I mean, I wouldn't advise it, but it's doable."
    # Fri - Sat (good lit)
    elif (day > 3 and day < 6 and hour > 17):
        return "Time to get LIT"
    # Otherwise no lit
    else:
        return "It is not time to get lit."
# end permit_lit()