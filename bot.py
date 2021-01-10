# Tyler's
# Yammering
# Lonesomeness
# Evasion
# Response
# Bot

import os

import discord
import asyncio
import datetime
from datetime import datetime, timedelta, time
import random

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

msgLimit = 2
timeoutLength = 300

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
    id: int = int(os.getenv('TYLER_ID'))
    msgCount: int = 0
    channel = None
    startTime: datetime = None
    messages = []

    def add(self):
        self.msgCount += 1

    def subtract(self):
        self.msgCount -= 1

    def reset(self):
        self.msgCount = 0
        self.startTime = None
        self.channel = None
        self.messages = []


class TylerSpamError(Exception):
    pass

tyler = Tyler()

@client.event
async def on_message(message):
    if message.author.id == tyler.id:
        if tyler.msgCount == 0:
            tyler.channel = message.channel
            tyler.startTime = message.created_at

        tyler.messages.append(message.content)

        tyler.add()

        def check(msg):
            if msg.author.id == tyler.id:
                if tyler.msgCount >= (msgLimit - 1):
                    raise TylerSpamError
            return msg.author.id != tyler.id

        if tyler.msgCount == msgLimit:
            diff = int(message.created_at.timestamp()) - int(tyler.startTime.timestamp())
            if diff >= timeoutLength or (msgCount >= msgLimit + 2 and diff <= 20):
                await tyler.channel.send(response(tyler.messages))
            try:
                msg = await client.wait_for('message', timeout=timeoutLength - diff, check=check)
            except asyncio.TimeoutError:
                if tyler.msgCount >= msgLimit:
                    await tyler.channel.send(response(tyler.messages))
                    tyler.reset()
            except TylerSpamError:
                tyler.subtract()
                if tyler.msgCount == 1:
                    await tyler.channel.send(response(tyler.messages))
                    tyler.reset()



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
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
        f"That's {'fucking' if random.random() < 0.5 else ''} {random.choice(adjectives)}, Tyler",
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
        f"Shouldn't you be {activities} or something, Tyler?"
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