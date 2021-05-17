# Big Vinny Bot Knowledge Base
# Author: ASquanchyPenguin
# Used to tweak big_vinny.py

from datetime import date
from datetime import datetime

from random import choice

import config

# Common lists used by the bot
aliases = ["<@!841002321751441428>", "big vinny", "vinny", "yelly", "chig winny", "big beep beep"]

# Bot responses
responses = {
    "actions" : ["Thinking about stuff", "Performing routine maintainence", "Sleeping.", "Napping in my chair.", "Getting ready to be yelly boi", "About to play with Ollie"],
    "affirm-strong" : ["Hell yeah", "You bet.", "How could I say no to that?"],
    "affirm-request" : ["Okay. Are you ready?", "Sure! Why don't you get yourself pretty before I do.", ""],
    "affirm-weak" : ["I mean you do you", "I wouldn't but don't let me stop you", "I'm gonna pass, but if you really want to, go for it."],
    "decline" : ["Nah", "Yeah how about no", "Tbh, that's a bad idea", "I'm gonna advise you pass on that", "Are you serious? No way."],
    "decline-request" : ["Nah.. you know I can't do that", "Sorry I'm not required to do that"],
    "max-length" : ["You writing a novel over here?", "Sorry bud that's too many the words"],
    "mentioned" : ["Did you need something?", "Hmm?", "What you want B?", "Sup?", "You called?"],
    "mood" : ["Can't complain", "Pretty good", "Not too bad", "Great!"],
    "neutral" : ["I don't know", "That's a head scratcher. I'm gonna need time to think on that.", "Honestly idk", "I can't say yes, but I also can't say no."],
    "none" : ["Huh?", "Hmm. Not quite sure what you mean", "Was that even English?", "Bruh idk", "Haha bot go brr. I don't know what this means.", "Sir are you even speaking English?"],
    "thoughts" : ["Am I alive?", "How did Jon Snow know about Lady and Nymeria?", "Do crabs think that fish can fly?", "Is it possible to touch your elbows together behind your back?"]
}

# Quick Reference for Keys based on indices
response_keys = [
    "actions",
    "affirm-strong",
    "affirm-weak",
    "decline",
    "decline-request",
    "max-length",
    "mentioned",
    "mood",
    "neutral",
    "none",
    "thoughts"
]

# Creates a response vector with the given targeted keys
def create_response_vector(keys):
    response_vector = [None] * len(response_keys)
    print("Response Vector Before: ", response_vector)

    for num in range(len(response_keys)):
        if response_keys[num] in keys:
            response_vector[num] = 1
        else:
            response_vector[num] = 0

    print("Response Vector After: ", response_vector)
    return response_vector
# End create_response_vector

# Determines the correct response based on the prompt
def determine_response(prompt):
    message_list = get_message(prompt).split()
    message_list_length = len(message_list)

    print("List: {}\nLength: {}".format(message_list, message_list_length))

    # No message
    if message_list_length == 0:
        return choice(responses["mentioned"])

    # Exceeds max length
    if message_list_length > config.max_query_length:
        return choice(responses["max-length"])

    return get_response(create_response_vector(["affirm-strong", "affirm-weak", "decline", "none"]))
# end determine_response

# Returns the cleansed message based on the prompt
def get_message(prompt):
    print("Prompt: ", prompt)
    cleansed_message = prompt.lower()

    for alias in aliases:
        cleansed_message = cleansed_message.replace(alias, '')

    cleansed_message = cleansed_message.strip()
    print("Cleansed: ", cleansed_message)

    return cleansed_message
# end get_message

# Returns a random response from the requested entries in the matrix
def get_response(response_vector):
    response_pool = list()

    # Verify the vector is the correct length
    if len(response_vector) != len(response_keys):
        print("Invalid vector length. Vector={}".format(response_vector))
        return choice(responses["none"])

    # Create possible response pool
    for num in range(len(response_keys)):
        if response_vector[num] == 1:
            response_values = responses[response_keys[num]]

            for value in response_values:
                response_pool.append(value)

    # Return random option based on response pool
    return choice(response_pool)
# end get_response
