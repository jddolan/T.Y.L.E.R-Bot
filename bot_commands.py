import random
import re
import responses
import os
import asyncio
from numbers import units, numbers, numberLink, emojiLink, numberEmojis
from lenny import lenny as lennyface
from time import sleep
from datetime import datetime, timedelta, time
from bad_words import badWords

joeId: int = int(os.environ.get('JOEID'))
botId: int = int(os.environ.get('BOTID'))
botChannel: int = int(os.environ.get('BOTCHANNEL'))

# People Who I think would make the bot say something I wouldn't feel comfortable with it saying
badUsers: list = [
    '138775042585526272', # Corey
    '138329017504890881', # Matthew
    '138712901404983296', # Harrison
    '130402289755095041', # Tyler
    '259193538384887809', # Micah
    '138358974071308289', # Scott
    joeId
]

async def command(message, client):
    messageStr = message.content.split(' ')

    commands = {
        '!8ball': eightball,
        '!addquote': addQuote,
        '!about': about,
        '!coinflip': coinflip,
        '!conch': eightball,
        '!crush': crush,
        '!eightball': eightball,  
        '!help': help,
        '!joke': joke,
        '!lenny': lenny,
        '!link': link,
        '!poll': poll,
        '!quote': quote,
        '!reminder': reminder,
        '!response': response,
        '!roll': roll,
        '!rps': rps,
        '!scan': scan,
        '!test': test
    }
    if message.author.id in badUsers:
        print("testing the filter")
        for word in messageStr:
            word = re.sub(r'\W+', '', word)
            if word in badWords:
                print(f"filtering a message from {message.author.name}")
                await message.channel.send("Your message was caught by the language filter, please refrain from using shitty language. Ping me if you don't know which word got caught in the filter and I'll look into it")
                return 
    commandStr = messageStr[0]
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
    help = responses.validCommands()

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
    await message.channel.send("""Flat Earf Rules, TYLER:
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
    string = ('¯\\\\_', '_/¯')
    await message.channel.send(string[0] +  string[1])
    return

async def crush(message, client):
    await message.channel.send(random.choice(responses.crush()))
    return

async def poll(message, client):
    try:
        match = re.match('(.*) (.*) "(.*)" (.*)', message.content.split('!poll ')[1])
        time = int(match.group(1))
        print(f"time: {time}")
        unit = match.group(2)
        print(f"unit: {unit}")
        prompt = match.group(3)
        print(f"prompt: {prompt}")
        options = match.group(4)
        print(f"options: {options}")
        if unit not in units.keys():
            raise
        options = options.split(', ')
        if len(options) < 1 or len(options) > 9:
            raise
    except:
        await message.channel.send(f"""Invalid input. Example of a valid submission: !poll 60 minutes "Prompt goes here" option 1, option 2, ..., option 9
Valid units of time are seconds, minutes, hours, days, weeks, months, or years
The maximum number of options for a poll is 9""")
        return
    await timer(message, client, time, unit, prompt, options)
    return

async def reminder(message, client):
    try:
        match = re.match('(.*) (.*) "(.*)"', message.content.split('!reminder ')[1])
        time = int(match.group(1))
        print(f"time: {time}")
        unit = match.group(2)
        print(f"unit: {unit}")
        prompt = match.group(3)
        print(f"prompt: {prompt}")
        if unit not in units.keys():
            raise
    except:
        await message.channel.send(f"""Invalid input. Example of a valid submission: !reminder 60 minutes "remind me to replace Tyler"
Valid units of time are seconds, minutes, hours, days, weeks, months, or years""")
        return
    await timer(message, client, time, unit, prompt)
    return

async def timer(message, client, time, unit, prompt, options = [], ):
    print("get in the timer function")
    if options != []:
        msg = f"**<@{message.author._user.id}>'s Poll Started!**\n\n**Prompt: " + prompt + "**\n\n"
        i: int = 1
        for option in options:
            msg = msg + f"{numbers[i]} : ***{option}***\n"
            i += 1
        msg = msg + "\n React to this message with what you think is the best option!"
    else:
        msg = f"""<@{message.author._user.id}>'s reminder set for {time} {unit}:\n\n **{prompt}**"""

    print(f"message: {msg}")
    newMessage = await message.channel.send(msg)
    await newMessage.edit(content=newMessage.content + f"\nrequestId:{message.id}")
    
    if options != []:
        for i in range(1,len(options) + 1):
            await newMessage.add_reaction(emojiLink[i])

    timeout: int = time * int(units[unit])
    print(f"timeout: {timeout}")

    def check(cancelMsg):
        return cancelMsg.author.id == joeId and cancelMsg.content == "cancel reminders"
    
    def organize(results):
        for i in range(0, len(results) - 1):
            for j in range(i+1, len(results)):
                if results[i]['index'] > results[j]['index']:
                    results[i], results[j] = results[j], results[i]
        return results

    def getWinners(results):
        winners = []
        winner = results[0]
        for result in results:
            if result['count'] > winner['count']:
                winner = result
        for result in results:
            if result['count'] == winner['count']:
                winners.append(result)
        return winners

    try:
        print("test waiting")
        cancelMsg = await client.wait_for('message', timeout=timeout, check=check)
        print("waiting done")
    except asyncio.TimeoutError:
        print("timed out, sending message")
        if options != []:
            msg = await newMessage.channel.fetch_message(newMessage.id)
            results = []
            for reaction in msg.reactions:
                
                if reaction.emoji in numberEmojis.keys() and numberLink[numberEmojis[reaction.emoji]] <= len(options):
                    i: int = numberLink[numberEmojis[reaction.emoji]] - 1
                    results.append({
                        'option': options[i],
                        'count': reaction.count - 1,
                        'index': i + 1
                    })
            winners = getWinners(results)
            print(f"winners: {winners}")
            resultMsg = f"""<@{message.author._user.id}>'s poll "{prompt}" has finished! Results:\n\n"""
            for i in range(0, len(options)):
                resultFound: bool = False
                for result in results:
                    if options[i] == result['option']:
                        resultFound = True
                        resultMsg = resultMsg + f"{numbers[i+1]} ***{options[i]}*** : {result['count']} vote{'s' if result['count'] > 1 or result['count'] == 0 else ''}\n"
                if not resultFound:
                    print(f"result not found for option {i}")
                    resultMsg = resultMsg + f"{numbers[i+1]} ***{options[i]}*** : 0 votes\n"
            if len(winners) > 1:
                if winners[0]['count'] == 0:
                    print("poll result: donowall")
                    resultMsg = resultMsg + f"\nNobody voted on this poll, get donowalled nerd"
                else:
                    print("poll result: tie")
                    resultMsg = resultMsg + f"\nIt was a tie! The winning options with {winners[0]['count']} vote{'s' if winners[0]['count'] > 1 or winners[0]['count'] == 0 else ''} are:\n\n"
                    for winner in winners:
                        resultMsg = resultMsg + f"{numbers[winner['index']]} : ***{winner['option']}***\n"
            else:
                print("poll result: one winner")
                resultMsg = resultMsg + f"\nThe winning option with {winners[0]['count']} vote{'s' if winners[0]['count'] > 1 or winners[0]['count'] == 0 else ''} is option {numbers[winners[0]['index']]}: ***{winners[0]['option']}***"
        else:
            resultMsg = f"Reminder for <@{message.author._user.id}>: {prompt}"

        await message.channel.send(resultMsg)
        return

async def findOldTimers(msg, client, guildId):
    print(f"msg: {msg.content}")
    print("setting up old timers...")
    guild = client.get_guild(guildId)
    for channel in guild.channels:
        try:
            iterator = await channel.fetch_message(channel.last_message_id)
            print(f"last message: {iterator.content}")
            oldIterator = "temp"
            while(True):
                async for message in channel.history(limit=9999999999,before=iterator):
                    iterator = message
                    if int(message.created_at.timestamp()) < 1580774400: # The day I implemented reminders/polls, nothing will be found beyond this time
                        print("no prompt found")
                        raise Exception
                    if message.content.startswith('!reminder'):
                        try:
                            match = re.match('(.*) (.*) "(.*)"', message.content.split('!reminder ')[1])
                            time = int(match.group(1))
                            print(f"time: {time}")
                            unit = match.group(2)
                            print(f"unit: {unit}")
                            prompt = match.group(3)
                            print(f"prompt: {prompt}")
                            if unit not in units.keys():
                                raise Exception
                            newMessage = await findOldPrompt(message, client, time, unit, prompt)
                            if newMessage == None:
                                raise Exception
                            timeout = int(time * units[unit])
                            difference = int(datetime.now().timestamp()) - int(newMessage.created_at.timestamp())
                            if difference < timeout:
                                await client.get_channel(botChannel).send(f"!activateOldTimer|{message.id}|{message.channel.id}|{timeout - difference}|{prompt}|[]|{newMessage.id}|{newMessage.channel.id}")
                            else:
                                raise Exception
                        except Exception as e:
                            done = True
                    elif message.content.startswith('!poll'):
                        try:
                            match = re.match('(.*) (.*) "(.*)" (.*)', message.content.split('!poll ')[1])
                            time = int(match.group(1))
                            print(f"time: {time}")
                            unit = match.group(2)
                            print(f"unit: {unit}")
                            prompt = match.group(3)
                            print(f"prompt: {prompt}")
                            options = match.group(4)
                            print(f"options: {options}")
                            if unit not in units.keys():
                                raise Exception
                            options = options.split(', ')
                            if len(options) < 1 or len(options) > 9:
                                raise Exception
                            newMessage = await findOldPrompt(message, client, time, unit, prompt, options)
                            if newMessage == None:
                                raise Exception
                            timeout = time * units[unit]
                            difference = int(datetime.now().timestamp()) - int(newMessage.created_at.timestamp())
                            if difference < timeout:
                                await client.get_channel(botChannel).send(f"!activateOldTimer|{message.id}|{message.channel.id}|{timeout - difference}|{prompt}|{options}|{newMessage.id}|{newMessage.channel.id}")
                            else:
                                raise Exception
                        except Exception as e:
                            continue
                
                if oldIterator == iterator:
                    print("done scanning")
                    raise Exception
                if int(iterator.created_at.timestamp()) < 1580774400: # The day I implemented reminders/polls, nothing will be found beyond this time
                    print("no prompt found")
                    raise Exception
                oldIterator = iterator
        except Exception:
            continue
    return

async def findOldPrompt(message, client, time, unit, prompt, options = []):
    iterator = await message.channel.fetch_message(message.channel.last_message_id)
    oldIterator = "temp"
    print("finding old prompt...")
    print(f"message: {iterator.content}")
    print(f"message id: {iterator.id}")
    while(True):
        async for prompt in message.channel.history(limit=9999999999,before=iterator):
            iterator = prompt
            try:
                requestId = prompt.content.split('requestId:')[1]
                if f"{message.id}" == requestId:
                    print("prompt found!")
                    return prompt
                if int(prompt.created_at.timestamp()) < 1580774400: # The day I implemented reminders/polls, nothing will be found beyond this time
                    print("no prompt found")
                    return None
            except:
                if int(prompt.created_at.timestamp()) < 1580774400: # The day I implemented reminders/polls, nothing will be found beyond this time
                    print("no prompt found")
                    return None
                else:
                    continue
        if oldIterator == iterator:
            print("done scanning")
            break
        if int(prompt.created_at.timestamp()) < 1580774400: # The day I implemented reminders/polls, nothing will be found beyond this time
            print("no prompt found")
            return None
        oldIterator = iterator
    print("didn't find the prompt")
    return None
    
async def activateOldTimer(message, client, timeout, prompt, options, newMessage):
    def check(cancelMsg):
        return cancelMsg.author.id == joeId and cancelMsg.content == "cancel reminders"

    def getWinners(results):
        winners = []
        winner = results[0]
        for result in results:
            if result['count'] > winner['count']:
                winner = result
        for result in results:
            if result['count'] == winner['count']:
                winners.append(result)
        return winners

    try:
        print("test waiting")
        cancelMsg = await client.wait_for('message', timeout=timeout, check=check)
        print("waiting done")
    except asyncio.TimeoutError:
        print("timed out, sending message")
        if options != []:
            try:
                msg = await newMessage.channel.fetch_message(newMessage.id)
                results = []
                for reaction in msg.reactions:
                    
                    if reaction.emoji in numberEmojis.keys() and numberLink[numberEmojis[reaction.emoji]] <= len(options):
                        i: int = numberLink[numberEmojis[reaction.emoji]] - 1
                        results.append({
                            'option': options[i],
                            'count': reaction.count - 1,
                            'index': i + 1
                        })
            except Exception:
                print("it was this msg")
            winners = getWinners(results)
            print(f"winners: {winners}")
            resultMsg = f"""<@{message.author._user.id}>'s poll "{prompt}" has finished! Results:\n\n"""
            for i in range(0, len(options)):
                print(f"len(options): {len(options)}")
                resultFound: bool = False
                for result in results:
                    if options[i] == result['option']:
                        resultFound = True
                        resultMsg = resultMsg + f"{numbers[i+1]} ***{options[i]}*** : {result['count']} vote{'s' if result['count'] > 1 or result['count'] == 0 else ''}\n"
                if not resultFound:
                    print(f"result not found for option {i}")
                    resultMsg = resultMsg + f"{numbers[i+1]} ***{options[i]}*** : 0 votes\n"
            if len(winners) > 1:
                if winners[0]['count'] == 0:
                    print("poll result: donowall")
                    resultMsg = resultMsg + f"\nNobody voted on this poll, get donowalled nerd"
                else:
                    print("poll result: tie")
                    resultMsg = resultMsg + f"\nIt was a tie! The winning options with {winners[0]['count']} vote{'s' if winners[0]['count'] > 1 or winners[0]['count'] == 0 else ''} are:\n\n"
                    for winner in winners:
                        resultMsg = resultMsg + f"{numbers[winner['index']]} : ***{winner['option']}***\n"
            else:
                print("poll result: one winner")
                resultMsg = resultMsg + f"\nThe winning option with {winners[0]['count']} vote{'s' if winners[0]['count'] > 1 or winners[0]['count'] == 0 else ''} is option {numbers[winners[0]['index']]}: ***{winners[0]['option']}***"
        else:
            resultMsg = f"Reminder for <@{message.author._user.id}>: {prompt}"

        await message.channel.send(resultMsg)
        return
    return