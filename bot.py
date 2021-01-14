# Tyler's
# Yammering
# Loneliness
# Emergency
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

from response_lists import activities, adjectives, commands, responses, quotes


token = "Nzk3NjE5NDUwMTI3ODQzMzg4.X_pG_w.WC-PkunlOkVlYH5_R5NU8VyIBfE"
guild = 'Flat Earf Rules'

msgLimit = 3
responseRateCap = 2
timeoutLength = 600

intents = discord.Intents.all()
client = discord.Client(intents=intents)

class Tyler:
    id: int = 130402289755095041
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
    if message.content[0] == '!':
        if message.content in commands.keys():
            if message.content == '!quote':
                await message.channel.send(random.choice(quotes))
            else:
                await message.channel.send(commands[message.content])
        else:
            await message.channel.send("Command not found, type !help for a list of all valid commands")
    elif tyler.channel == None or tyler.channel == message.channel:
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

    if tyler.msgCount <= 5: 
        severity = "mild"
    elif tyler.msgCount > 5 and tyler.msgCount <= 10:
        severity = "moderate"
    else:
        severity = "severe"

    response = random.choice(responses[severity])
    while response == tyler.lastResponse:
        response = random.choice(responses[severity])

    tyler.lastResponse = response
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


client.run(token)