import random
import re
import responses
import os

joeId: int = int(os.environ.get('JOEID'))
botId: int = int(os.environ.get('BOTID'))

async def command(message, client):
    commandStr = message.content.split(' ')[0]
    commands = {
        '!help': help,
        '!about': about,
        '!quote': quote,
        '!addquote': addQuote,
        '!scan': scan,
        '!roll': roll,
        '!rps': rps
    }
    command = commands.get(commandStr, invalidCommand)
    await command(message, client)
    return

async def help(message, client):
    await message.channel.send('''Valid Commands: 

!about: More information about the bot
!help: A list of valid commands for the bot
!quote: Provides a quote
!addquote: !addquote <quote> <user> submits the quote to be added to the bot's list of randomly generated quotes. Must be approved by Joe and the person being quoted
!roll: !roll <XdY> will roll a Y-sided die X times''')
    return

async def about(message, client):
    await message.channel.send("This is a bot designed to respond to Tyler when other people aren't. Created by Joe")
    return

async def invalidCommand(message, client):
    await message.channel.send("Command not found, type !help for a list of all valid commands")
    return

async def scan(message, client):
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

async def quote(message, client):
    await message.channel.send(random.choice(responses.quotes))
    return

async def addQuote(message, client):
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

async def roll(message, client):
    try:
        rollInput = message.content.split('!roll ')[1]
        print(f"rollInput: {rollInput}")
        match = re.match('([0-9]+)d([0-9]+)', rollInput)
        rolls = int(match.group(1))
        sides = int(match.group(2))
        print(f"rolls: {rolls}")
        print(f"sides: {sides}")
    except:
        try:
            match = re.match('d([0-9]+)', rollInput)
            rolls = 1
            sides = int(match.group(1))
        except:
            print("first roll error")
            await message.channel.send(f"Invalid format. Example of a valid submission: !roll 3d6")
            return
    
    try:
        total = 0
        dice: list = []
        for i in range(0,rolls):
            dice.append(f"{random.randrange(1,sides+1,1)}")
        print(f"dice: {dice}")
        for die in dice:
            total += int(die)
        print(f"total: {total}")
    except:
        print("second roll error")
        await message.channel.send(f"Invalid values. Example of a valid submission: !roll 3d6")
        return

    if len(dice) == 1:
        await message.channel.send(f"<@{message.author._user.id}> rolled {total}.")
    else:
        await message.channel.send(f"<@{message.author._user.id}> rolled {total}. ({' + '.join(dice)}) = {total}")
    return

async def rps(message, client):
    await message.channel.send("work in progress")