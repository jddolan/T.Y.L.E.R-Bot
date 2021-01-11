# Tyler's
# Yammering
# Lonesomeness
# Evasion
# Response
# Bot

# joe_id=139785944009015296
# tyler_id=130402289755095041

import os

import discord
import asyncio
import datetime
from datetime import datetime, timedelta, time
import random


token = "Nzk3NjE5NDUwMTI3ODQzMzg4.X_pG_w.WC-PkunlOkVlYH5_R5NU8VyIBfE"
guild = 'Flat Earf Rules'

msgLimit = 2
responseRateCap = 2
timeoutLength = 20

intents = discord.Intents.all()
client = discord.Client(intents=intents)

activities = [
    "playing runescape",
    "playing WoW",
    "watching porn",
    "talking about Isreal",
    "playing league",
    "flaking on people",
    "playing volleyball",
    "watching The Sopranos"
]

adjectives = [
    "great",
    "cool",
    "awesome",
    "amazing",
    "weird",
    "crazy",
    "wacky",
    "unbelievable",
    "nutty",
    "Pog",
]

class Tyler:
    id: int = 139785944009015296
    msgCount: int = 0
    msgsSinceLastResponse: int = 0
    channel = None
    startTime: datetime = None
    messages = []
    diff: int = 0
    waiting: bool = False
    lastResponse: str = None

    def reset(self):
        self.msgCount = 0
        self.startTime = None
        self.channel = None
        self.messages = []
        self.diff = 0
        self.waiting = False
        self.lastResponse = None
        self.msgsSinceLastResponse = 0

tyler = Tyler()

@client.event
async def on_message(message):
    if tyler.channel == None or tyler.channel == message.channel:
        if message.author.id == tyler.id:
            print("it's a message from tyler")
            if tyler.msgCount == 0:
                print("it's the first one")
                tyler.channel = message.channel
                tyler.startTime = message.created_at

            tyler.messages.append(message.content)

            tyler.msgCount += 1
            tyler.msgsSinceLastResponse += 1

            print(f"tyler has now sent {tyler.msgCount} messages in a row")

            def check(msg):
                print(f"went in the check, variables: \nmsgCount: {tyler.msgCount}\nmsgLimit: {msgLimit}\nauthor id: {msg.author.id}\ntyler id: {tyler.id}\n")
                return msg.author.id != tyler.id or (tyler.msgCount >= msgLimit + 1)

            if tyler.msgCount >= msgLimit and tyler.msgsSinceLastResponse >= responseRateCap:
                print("msgCount is higher than the limit")
                tyler.diff = int(message.created_at.timestamp()) - int(tyler.startTime.timestamp())
                if tyler.diff >= timeoutLength and tyler.waiting == False:
                    print("the time difference was higher than the time limit and we are not waiting on another message to be sent")
                    if tyler.msgsSinceLastResponse >= responseRateCap:
                        tyler.msgsSinceLastResponse = 0
                        await tyler.channel.send(response(tyler.messages))
                else:
                    print("the messages were sent within the time limit")
                    if tyler.waiting == False:
                        print("we are not waiting on another message")
                        try:
                            print("now waiting on the check...")
                            tyler.waiting = True
                            msg = await client.wait_for('message', timeout=timeoutLength - tyler.diff, check=check)
                            if (msg.author.id != tyler.id):
                                print("someone else sent a message, abort mission")
                                tyler.reset()
                            else:
                                print("sending message")
                                tyler.msgsSinceLastResponse = 0
                                await tyler.channel.send(response(tyler.messages))
                        except asyncio.TimeoutError:
                            print("timed out, sending message")
                            tyler.msgsSinceLastResponse = 0
                            await tyler.channel.send(response(tyler.messages))
                        print("resetting the waiting variable")
                        tyler.waiting = False


        elif message.author != client.user:
            print("message not from tyler found, abort mission")
            tyler.reset()
            if message.content == 'pee' or message.content == 'poo':
                await message.channel.send("Stop saying pee and poo it's not as funny as you think it is.")

def response(messages):
    responses = {
        "mild": [
            f"stfu {'Tyler' if random.random() < 0.75 else 'Richard'}",
            "Nobody cares, Tyler",
            "Very cool, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, Tyler",
            "I'm sure everyone is just busy and that's why they didn't respond",
            "ew..",
            "Tl;dr",
            "Tell me more...",
            "Get it, king!",
            "Nice cut, G",
            "oof",
            "What the fuck, Tyler?",
            "Let's fucking go, Tyler!",
            "stop.",
            "thanks!",
            "Why are you like this?",
            "Good shit dude",
            "Why would you say that?",
            spongebob(messages),
            "I appreciate you taking the time to write that, Tyler.",
            "That's a cool story Tyler, you should tell it at parties",
            "That's not very Pog of you, Tyler",
            "You're never going to find a big titty goth gf who plays volleyball if you say things like that",
            "?",
            "Wow!",
            "nmn",
            "Looks like you got DonoWalled, Tyler",
            "nice play fucking idiot"
            "Tyler, try to be more positive. You are a good player, just dont insult other for nothing and you'll have better game"
            f"Shouldn't you be {random.choice(activities)} or something, Tyler?"
        ],
        "moderate": [
            "Seriously, Tyler, you need to stop",
            "Looking like a Trump supporter out here with this wall of text you're building",
            "Will you stop, pretty please?",
            "If somebody was going to respond they probably would have done it by now, just saying"
        ],
        "severe": [
            "Get the hint and shut the fuck up dude",
            "Clearly nobody else is interested in what you're talking about right now",
            "Tyler, even though nobody else is reading your messages I'm forced to suffer through each one so please end my suffering and stop typing",
        ]
    }
    responses["moderate"] = responses["moderate"] + responses["mild"]
    responses["severe"] = responses["severe"] + responses["moderate"]

    if tyler.msgCount <= 5: 
        severity = "mild"
    elif tyler.msgCount > 5 and tyler.msgCount <= 8:
        severity = "moderate"
    else:
        severity = "severe"

    response = random.choice(responses[severity])
    while response == tyler.lastResponse:
        response = random.choice(responses[severity])

    tyler.lastResponse = response
    return response

def spongebob(messages):
    newmessage = ""
    for message in messages:
        msg = list(message)
        i = 0
        while i < len(msg):
            if random.random() < 0.5:
                msg[i] = msg[i].swapcase()
            i += 1
        newmessage = newmessage + "".join(msg) + "\n"
        
    return(newmessage)


client.run(token)