# Tyler's
# Yammering
# Loneliness
# Emergency
# Response
# Bot

import os

import discord
import asyncio
import datetime
from datetime import datetime, timedelta, time
import random
import re

from response_lists import activities, adjectives, commands, responses, quotes


token = os.environ.get('TOKEN')
joeId: int = int(os.environ.get('JOEID'))
botId: int = int(os.environ.get('BOTID'))
tylerId: int = int(os.environ.get('TYLERID'))

msgLimit = 3
responseRateCap = 2
timeoutLength = 600

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
    if message.content[0] == '!':
        await command(message)
    elif message.author.id == tylerId:
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

async def command(message):
    command = message.content.split(' ')[0]
    
    if command in commands.keys():
        if command == '!quote':
            await quote(message)
        elif command == '!addquote':
            await addQuote(message)
        elif command == "!scan":
            await scan(message)
        elif command == '!roll':
            await roll(message)
        else:
            await message.channel.send(commands[command])
    else:
        await message.channel.send("Command not found, type !help for a list of all valid commands")
    return

async def scan(message):
    count = 0
    print(f"id: {message.id}")
    iterator = message
    oldIterator = "temp"
    while(True):
        async for msg in message.channel.history(limit=9999999999,before=iterator):
            count += 1
            iterator = msg
            if '"-' in msg.content or '" -' in msg.content:
                #  or "-" in msg.content:
                print(msg.content)
                print(f"count: {count}\n")
        if oldIterator == iterator:
            print("done scanning")
            break
        oldIterator = iterator
        print(f"last message: {msg}")
        print(msg.content)
        print("fetching more results")
        print(f"iterator: {iterator}")

async def quote(message):
    await message.channel.send(random.choice(quotes))
    return

async def addQuote(message):
    try:
        match = re.match('(.*) \<@!(.*)\>', message.content.split('!addquote ')[1])
        quote = match.group(1)
        userId = int(match.group(2))
    except:
        await message.channel.send(f"""Invalid format. Example of a valid submission:
!addquote this is an example quote <@{botId}>""")
        return
        
    
    print(f"quote: {quote}")
    print(f"userId: {userId}")

    newMessage = await message.channel.send(f"""<@{message.author._user.id}> submitted the following quote: 

"{quote}" - <@{userId}>

Adding the quote requires permission from the quote's source. <@{userId}>, please react to this message with <:yea:750400833946124429> or <:nay:750400843097964608> to approve or deny adding this quote.""")

    def check(reaction, user):
        print(f'reaction: {reaction}')
        return user == client.get_user(userId) and (reaction.emoji.name == 'yea' or reaction.emoji.name == 'nay')

    reaction, user = await client.wait_for('reaction_add', check=check)

    if reaction.emoji.name == 'yea':
        await newMessage.edit(content=f"""<@{message.author._user.id}> submitted the following quote: 

"{quote}" - <@{userId}>

Permission to add this quote was approved!""")
        await client.get_user(joeId).send(f"quote submission from {message.author._user.name}: {quote} - <@{userId}>")
    elif reaction.emoji.name == 'nay':
        await newMessage.edit(content=f"""<@{message.author._user.id}> submitted the following quote: 

"{quote}" - <@{userId}>

Permission to add this quote was denied.""")
    
    return

async def roll(message):
    try:
        rollInput = message.content.split('!roll ')[1]
        print(f"rollInput: {rollInput}")
        match = re.match('([0-9]+)d([0-9]+)', rollInput)
        rolls = int(match.group(1))
        sides = int(match.group(2))
        print(f"rolls: {rolls}")
        print(f"sides: {sides}")
    except:
        print("first roll error")
        await message.channel.send(f"Invalid format. Example of a valid submission: !roll 3d6")
        return
    
    try:
        total = 0
        dice: list = []
        for i in range(1,rolls):
            dice.append(f"{random.uniform(1,sides)}")
        for die in dice:
            total += int(die)
    except:
        print("second roll error")
        await message.channel.send(f"Invalid values. Example of a valid submission: !roll 3d6")
        return

    await message.channel.send(f"<@{message.author._user.id}> rolled {total}. ({' + '.join(dice)} = {total}")
    return

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