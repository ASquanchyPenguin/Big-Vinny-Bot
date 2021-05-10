from datetime import date
from datetime import datetime

# Common lists used by the bot
aliases = ["vinny", "yelly", "chig winny", "big beep beep"]
commands = ["!version", "!time"]
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

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

def get_time(format):
    today = datetime.now()
    time = today.strftime(format)
    return time
# end get_time()

