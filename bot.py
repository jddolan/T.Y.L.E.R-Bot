# Tyler's
# Yammering
# Loneliness
# Emergency
# Response
# Bot
# V1.00

import os

import discord
import asyncio
import datetime
from datetime import datetime, timedelta, time
import random
import re

import responses
from bot_commands import command

token = os.environ.get('TOKEN')
joeId: int = int(os.environ.get('JOEID'))
botId: int = int(os.environ.get('BOTID'))
tylerId: int = int(os.environ.get('TYLERID'))

msgLimit = 2
responseRateCap = 2
timeoutLength = 300

intents = discord.Intents.all()
client = discord.Client(intents=intents)

class Tyler():
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

tyler: dict = {}

@client.event
async def on_message(message):
    try:
        if message.content[0] == '!':
            await command(message, client)
    except:
        print("error, probably an image attached")
        print(f"message: {message.content}")
    if message.author.id == tylerId:
        if tyler.get(message.channel.name, None) == None:
            # New channel found, create new dict entry
            tyler[message.channel.name] = Tyler()
            tyler[message.channel.name].channel = message.channel
        await tylerMessage(message)
    elif message.author != client.user:
        print("message not from tyler found, abort mission")
        if tyler.get(message.channel.name, None) != None:
            tyler[message.channel.name].reset()
        if message.content == 'pee' or message.content == 'poo':
            await message.channel.send("Stop saying pee and poo it's not as funny as you think it is.")

def response(messages, message):

    if tyler[message.channel.name].msgCount <= 5: 
        severity = "mild"
    elif tyler[message.channel.name].msgCount > 5 and tyler[message.channel.name].msgCount <= 10:
        severity = "moderate"
    else:
        severity = "severe"

    response = random.choice(responses[severity])
    while response == tyler[message.channel.name].lastResponse:
        response = random.choice(responses[severity])

    tyler[message.channel.name].lastResponse = response
    if response == "spongebob":
        response = spongebob(messages)
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


async def tylerMessage(message):
    print("it's a message from tyler")
    if tyler[message.channel.name].msgCount == 0:
        print("it's the first one")
        tyler[message.channel.name].channel = message.channel
        tyler[message.channel.name].startTime = message.created_at

    tyler[message.channel.name].messages.append(message.content)

    tyler[message.channel.name].msgCount += 1
    tyler[message.channel.name].msgsSinceLastResponse += 1

    print(f"tyler has now sent {tyler[message.channel.name].msgCount} messages in a row")

    def check(msg):
        print(f"went in the check, variables: \nmsgCount: {tyler[message.channel.name].msgCount}\nmsgLimit: {msgLimit}\nauthor id: {msg.author.id}\ntyler id: {tylerId}\n")
        return msg.channel == tyler[message.channel.name].channel and (msg.author.id != tylerId or (tyler[message.channel.name].msgCount >= msgLimit + 1))

    if tyler[message.channel.name].msgCount >= msgLimit and tyler[message.channel.name].msgsSinceLastResponse >= responseRateCap:
        print("msgCount is higher than the limit")
        tyler[message.channel.name].diff = int(message.created_at.timestamp()) - int(tyler[message.channel.name].startTime.timestamp())
        if tyler[message.channel.name].diff >= timeoutLength and tyler[message.channel.name].waiting == False:
            print("the time difference was higher than the time limit and we are not waiting on another message to be sent")
            if tyler[message.channel.name].msgsSinceLastResponse >= responseRateCap:
                tyler[message.channel.name].msgsSinceLastResponse = 0
                await tyler[message.channel.name].channel.send(response(tyler[message.channel.name].messages, message))
        else:
            print("the messages were sent within the time limit")
            if tyler[message.channel.name].waiting == False:
                print("we are not waiting on another message")
                try:
                    print("now waiting on the check...")
                    tyler[message.channel.name].waiting = True
                    msg = await client.wait_for('message', timeout=timeoutLength - tyler[message.channel.name].diff, check=check)
                    if (msg.author.id != tylerId):
                        print("someone else sent a message, abort mission")
                        tyler[message.channel.name].reset()
                    else:
                        print("sending message")
                        tyler[message.channel.name].msgsSinceLastResponse = 0
                        await tyler[message.channel.name].channel.send(response(tyler[message.channel.name].messages, message))
                except asyncio.TimeoutError:
                    print("timed out, sending message")
                    tyler[message.channel.name].msgsSinceLastResponse = 0
                    await tyler[message.channel.name].channel.send(response(tyler[message.channel.name].messages, message))
                print("resetting the waiting variable")
                tyler[message.channel.name].waiting = False

client.run(token)