import random
import re
import responses
import os
from lenny import lenny as lennyface
from time import sleep

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
        '!rps': rps,
        '!coinflip': coinflip,
        '!link': link,
        '!response': response,
        '!8ball': eightball,
        '!eightball': eightball,
        '!lenny': lenny,
        '!joke': joke,
        '!test': test
    }
    command = commands.get(commandStr, invalidCommand)
    await command(message, client)
    return

async def invalidCommand(message, client):
    print(f"Invalid Command {message} detected, sending to help")
    message.content = '!help '+ message.content
    await help(message, client)
    return

async def help(message, client):
    output = ""
    help = {
        '!help': "**!help** <command: Optional> provides a list of valid commands for the bot",
        '!about': "**!about** provides information about the bot",
        '!quote': "**!quote** <name: Optional> provides a quote, if a name is not provided the quote will be randomly selected from all stored quotes",
        '!addquote': "**!addquote** <quote> <user> submits the quote to be added to the bot's list of randomly generated quotes. Must be approved by Joe and the person being quoted",
        '!scan': "**!scan** is not recommended to use unless you have access to the bot's logs, as it will serve no purpose without them. Will scan a server and find messages that contain the passed string.",
        '!roll': "**!roll** <XdY> will roll a Y-sided die X times",
        '!rps': "**!rps** <choice> choose rock paper or scissors and play against the bot",
        '!coinflip': "**!coinflip** <choice: Optional> flip a coin, optionally choose heads or tails",
        '!link': "**!link** provides a link to a piece of content significant to the Flat Earf Rules discord server",
        '!response': "**!response** <name: Optional> generates a random response, optionally include the name of the person the response is for",
        '!8ball': "**!8ball** <question: Optional> provides an answer from the magic 8-ball",
        '!lenny': "**!lenny** generates a random lenny face ( ͡° ͜ʖ ͡°)",
        '!joke': "**!joke** generates a funny joke",
        '!test': "**!test** this command will generally do nothing aside from showing a message related to something in development"
    }
    try:
        input = message.content.split('!help ')[1]
        if input[0] != '!':
            input = '!' + input
        if input in help.keys():
            print("command found in help keys, setting output")
            output = output + f"{help[input]}"
        else:
            print("command not found in help keys, raising error")
            output = f"Command {input} not found.\n\n"
            raise
    except:
        print("invalid command, presenting list of all valid commands")
        output = output + "Valid Commands: \n\n"
        for key in help.keys():
            output = output + f"{help[key]}\n"
    print("sending output...")
    await message.channel.send(output)
    print("output sent")
    return

async def about(message, client):
    msg = await message.channel.send("""Flat Earf Rules, TYLER:
Tyler's
Yammering
Loneliness
Emergency
Response
T.Y.L.E.R. Bot was originally designed to respond to Tyler when other people weren't. It now does a lot of random stuff, type !help to see the list of commands the bot recognizes. Created by Joe Dolan."""
)
    return

async def quote(message, client):
    funcNames = {
        'tyler': responses.tyler,
        'joe': responses.joe,
        'ximing': responses.ximing,
        'matt': responses.matt,
        'matthew': responses.matthew,
        'micah': responses.micah,
        'landon': responses.landon,
        'mango': responses.mango
    }
    try:
        names = message.content.split('!quote ')[1].lower().split(' ')
        print(f"names: {names}")
        try:
            quotes = []
            for name in names:
                func = funcNames.get(name, None)
                if func == None:
                    raise func
                quotes = func() + quotes
                print(f"quotes: {quotes}")
            quote = random.choice(quotes)
        except:
            quote = "An invalid name was submitted. Valid options are tyler, joe, ximing, matt, matthew, micah, landon, and mango. Please try again with one of those names, or type just !quote to get a quote from a random person."
    except:
        quote = random.choice(responses.quotes)

    await message.channel.send(quote)
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
    rpsChoices = ['rock','paper','scissors']

    try:
        input = message.content.split('!rps ')[1]
    except:
        await message.channel.send(f"Invalid option. Please choose rock, paper, or scissors. Example: !rps rock")
        return

    print(f"input: {input}")
    if input != 'rock' and input != 'scissors' and input != 'paper':
        await message.channel.send(f"Invalid option. Please choose rock, paper, or scissors. Example: !rps rock")
        return
    
    choice = random.choice(rpsChoices)
    output = f"<@{message.author.id}> chose {input}. I choose {choice}. "
    tie = "It's a tie!"
    lose = "You lose!"
    win = "You win!"
    if input == 'rock':
        if choice == 'rock':
            await message.channel.send(output + tie)
        elif choice == 'paper':
            await message.channel.send(output + lose)
        elif choice == 'scissors':
            await message.channel.send(output + win)
    elif input == 'paper':
        if choice == 'rock':
            await message.channel.send(output + win)
        elif choice == 'paper':
            await message.channel.send(output + tie)
        elif choice == 'scissors':
            await message.channel.send(output + lose)
    elif input == 'scissors':
        if choice == 'rock':
            await message.channel.send(output + lose)
        elif choice == 'paper':
            await message.channel.send(output + win)
        elif choice == 'scissors':
            await message.channel.send(output + tie)
    return

async def coinflip(message, client):
    sides = {
        1: 'heads',
        2: 'tails'
    }

    lose = "You lose!"
    win = "You win!"

    result = sides[random.choice([1,2])]
    try:      
        input = message.content.split('!coinflip ')[1]
        output = f"<@{message.author.id}> chose {input}. The result was {result}. "
        if input != 'heads' and input != 'tails':
            await message.channel.send(f"Invalid option. Please choose heads or tails. Example: !coinflip heads")
            return
        else:
            if input == result:
                await message.channel.send(output + win)
            else:
                await message.channel.send(output + lose)
    except:
        await message.channel.send(f"<@{message.author.id}> the result was {result}.")

async def link(message, client):
    await message.channel.send(random.choice(responses.links()))
    return

async def response(message, client):
    try:
        input = message.content.split('!response ')[1].split(' ')
        name = input[0]
        severity = "mild"
        # Severity input option (waiting to implement until the bot has done some of the severe responses naturally)
        # if len(input) > 1:
        #     if input[1] in ['mild', 'moderate', 'severe']:
        #         severity = input[1]
        #     else:
        #         await message.channel.send(f"Invalid severity input, mild will be used as the severity. Valid options for severity are mild, moderate, or severe.")
        #         severity = "mild"
        # else:
        #     severity = "mild"
        await message.channel.send(responses.responses(severity=severity, name=name))
    except:
        await message.channel.send(responses.responses(severity="mild"))

async def eightball(message, client):
    await message.channel.send(random.choice(responses.eightball()))
    return

async def lenny(message, client):
    await message.channel.send(lennyface())
    return

async def joke(message, client):
    await message.channel.send(random.choice(responses.jokes()))
    return

async def test(message, client):
    string = ('¯' + '\\' + '_', '_/¯')
    await message.channel.send(string[0] +  string[1])
    return