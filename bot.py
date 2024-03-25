# Tyler's
# Yammering
# Loneliness
# Emergency
# Response
# Bot
# V2.0

import os

import discord
import asyncio
import datetime
from datetime import datetime

import responses
from bot_commands import command, findOldTimers, activateOldTimer

token = os.environ.get('TOKEN')
guildIds = []
guildIds.append(int(os.environ.get('THEBOYS')))
guildIds.append(int(os.environ.get('FLATEARFRULES')))

adminId: int = int(os.environ.get('JOEID'))
botId: int = int(os.environ.get('BOTID'))
tylerId: int = int(os.environ.get('TYLERID'))

msgLimit = 2
responseRateCap = 1
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
async def on_ready():
    await client.get_channel(int(os.environ.get('BOTCHANNEL'))).send('findOldTimers')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        if message.content.startswith("findOldTimers"):
            try:
                for guildId in guildIds:
                    await findOldTimers(message, client, guildId)
                print("all timers are set up again")
                await message.delete()
            except Exception as e:
                print("an error occured while finding old timers, logging error...")
                print(e)
                message.channel.send("Error occured in findOldTimers <@{adminId}>")
                await message.delete()
        elif message.content.startswith("!activateOldTimer"):
            try:
                content = message.content.split('|')
                print(f"content: {content}")
                throwaway,message,channel,timeout,prompt,options,newMessage,newChannel = content
                channel = client.get_channel(int(channel))
                timeout = int(timeout)
                newChannel = client.get_channel(int(newChannel))
                message = await channel.fetch_message(int(message))
                newMessage = await newChannel.fetch_message(int(newMessage))
                options = options.strip('][').split(', ')
                for option in options:
                    option.strip("'")
                await activateOldTimer(message, client, timeout, prompt, options, newMessage)
                await message.delete()
            except Exception as e:
                print("an error occured while activating old timers, logging error...")
                print(e)
                message.channel.send("Error occured in activateOldTimers <@{adminId}>")
                await message.delete()
        return
    try:
        if message.content.lower() in responses.replies.keys():
            replyKey: str = message.content.lower()
            await message.channel.send(responses.replies[replyKey])
        elif message.content[0] == '!':
            await command(message, client)
    except Exception as e:
        print("error found! trying to log error...")
        print(e)
        print(f"message: {message.content}")
    if message.author.id == tylerId:
        if tyler.get(message.channel.name, None) == None:
            # New channel found, create new dict entry
            tyler[message.channel.name] = Tyler()
            tyler[message.channel.name].channel = message.channel
        await tylerMessage(message)
    else:
        print("message not from tyler found, resetting variables")
        if tyler.get(message.channel.name, None) != None:
            tyler[message.channel.name].reset()
        if message.content == 'pee' or message.content == 'poo':
            await message.channel.send("Saying pee and poo is not funny.")

def botResponse(messages, message):

    if tyler[message.channel.name].msgCount <= 5: 
        severity = "mild"
    elif tyler[message.channel.name].msgCount > 5 and tyler[message.channel.name].msgCount <= 10:
        severity = "moderate"
    else:
        severity = "severe"
        
    response = responses.responses(
        severity=severity, 
        name="Tyler",
        messages=messages,
        lastResponse=tyler[message.channel.name].lastResponse
    )     

    tyler[message.channel.name].lastResponse = response

    return response

async def tylerMessage(message):
    print("it's a message from tyler")
    if "i hate white women" in message.content:
        await message.channel.send("Just a daily reminder that Tyler doesn't actually hate white women.")
        return
    
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
                await tyler[message.channel.name].channel.send(botResponse(tyler[message.channel.name].messages, message))
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
                        await tyler[message.channel.name].channel.send(botResponse(tyler[message.channel.name].messages, message))
                except asyncio.TimeoutError:
                    print("timed out, sending message")
                    tyler[message.channel.name].msgsSinceLastResponse = 0
                    await tyler[message.channel.name].channel.send(botResponse(tyler[message.channel.name].messages, message))
                print("resetting the waiting variable")
                tyler[message.channel.name].waiting = False

client.run(token)
