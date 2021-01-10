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
    "amazing"
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
    channel = None
    startTime: datetime = None
    messages = []
    diff: int = 0

    def add(self):
        self.msgCount += 1

    def subtract(self):
        self.msgCount -= 1

    def reset(self):
        self.msgCount = 0
        self.startTime = None
        self.channel = None
        self.messages = []
        self.diff = 0


class TylerSpamError(Exception):
    msg = "test"

tyler = Tyler()

@client.event
async def on_message(message):
    if message.author.id == tyler.id:
        if tyler.msgCount == 0:
            tyler.channel = message.channel
            tyler.startTime = message.created_at

        tyler.messages.append(message.content)

        tyler.add()

        print(tyler.msgCount)

        def check(msg):
            print("test5\n")
            # if msg.author.id == tyler.id:
            #     if tyler.msgCount >= int(msgLimit - 1) or (tyler.msgCount >= msgLimit + 2 and tyler.diff <= 20):
            #         raise TylerSpamError
            return msg.author.id != tyler.id or (tyler.msgCount >= msgLimit + 2 and tyler.diff <= 20)

        if tyler.msgCount >= msgLimit:
            print("test1\n")
            tyler.diff = int(message.created_at.timestamp()) - int(tyler.startTime.timestamp())
            if tyler.diff >= timeoutLength:
                await tyler.channel.send(response(tyler.messages))
            try:
                print("test2\n")
                msg = await client.wait_for('message', timeout=timeoutLength - tyler.diff, check=check)
                if (msg.author.id != tyler.id):
                    tyler.reset()
                elif (tyler.msgCount >= msgLimit + 2 and tyler.diff <= 20):
                    await tyler.channel.send(response(tyler.messages))
            except asyncio.TimeoutError:
                print("test3\n")
                if tyler.msgCount >= msgLimit:
                    await tyler.channel.send(response(tyler.messages))
            # except TylerSpamError:
            #     print("test4\n")
            #     if tyler.msgCount >= msgLimit:
            #         await tyler.channel.send(response(tyler.messages))

    elif message.author != client.user:
        tyler.reset()
        if message.content == 'pee' or message.content == 'poo':
            await message.channel.send("Stop saying pee and poo please it's not as funny as you think it is.")

def response(messages):
    responses = [
        "stfu Tyler",
        "stfu Richard",
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
    ]
    return random.choice(responses)

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