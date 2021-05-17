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
    "affirm-strong" : ["Hell yeah", "Bet let's go right now", "How could I say no to that?"],
    "affirm-weak" : ["I mean you do you", "I wouldn't but don't let me stop you", "You can, but I'll pass"],
    "decline" : ["Nah fam not right now", "Yeah how about no", "Tbh, it's a bad idea", "I'm gonna advise you pass on that"],
    "max-length" : ["You writing a novel over here?", "Sorry bud that's too many the words"],
    "mentioned" : ["Don't at me", "Hmm?", "What you want B?", "Sup?"],
    "none" : ["Huh?", "Hmm. Not quite sure what you mean", "Was that even English?", "Bruh idk", "Haha bot go brr. I don't know what this means.", "Sir are you even speaking English?"]
}

# Quick Reference for Keys based on indices
response_keys = ["affirm-strong", "affirm-weak", "decline", "max-length", "mentioned", "none"]

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
