# Big Vinny Bot Knowledge Base
# Author: ASquanchyPenguin
# Used to tweak big_vinny.py

from datetime import date
from datetime import datetime

from random import choice

# Common lists used by the bot
aliases = ["<@!841002321751441428>", "big vinny", "vinny", "yelly", "chig winny", "big beep beep"]

# Bot responses
responses = {
    "affirm_strong" : ["Hell yeah", "Bet let's go right now", "How could I say no to that?"],
    "affirm_weak" : ["I mean you do you", "I wouldn't but don't let me stop you", "You can, but I'll pass"],
    "decline" : ["Nah fam not right now", "Yeah how about no", "Tbh, it's a bad idea", "I'm gonna advise you pass on that"],
    "max-length" : ["You writing a novel over here?", "Sorry bud that's too many the words"],
    "mentioned" : ["Don't at me", "Hmm?", "What you want B?", "Sup?"],
    "none" : ["Huh?", "Hmm. Not quite sure what you mean", "Was that even English?", "Bruh idk", "Haha bot go brr. I don't know what this means.", "Sir are you even speaking English?"]
}

# Determines the correct response based on the prompt
def determine_response(prompt):
    return "PASS"
# end determine_response
