import random

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

def tyler():
    return [
    "You add a meet and cheese board to anything and you up the class by 3 points - Tyler",
    "Im a top 3 defender at my home courts quote it - Tyler",
    "Water electric quote it - Tyler speculating on the typing of Sobble",
    "Knicks making room for kyrie and KD quote me on it - Tyler",
    "Lebron is dropping 55 in game 7 quote me - Tyler",
    "leffen's not dropping a GAME tomorrow quote it - Tyler",
    "I just want to wear a fucking kimono - Tyler",
    "3 Danish teams in the top 10 by the end of 2017 for csgo - Tyler",
    "belgium vs france in the world cup final quote it - Tyler",
    "G2 is winning world's quote me on it - Tyler",
    """Liquid vs EG grand final
EG from losers
Quote it
- Tyler""",
    """LFY that team who fucked shit up in the groups
out in semis
actually quarters
quote it
- Tyler""",
    "DND was the best game mode quote that one - Tyler",
    "this is the time g2 won't choke at an international event - Tyler",
    "you may have gotten more kills than me, - Tyler",
    "ill have it done by tonight quote me on that - Tyler",
    "quote me on this im gonna win joe's family group - Tyler",
    """corey we're playing tonight
ok
?
quote me on that
- Tyler""",
    "I guess I'm just a weeb guys. - Tyler",
    "Piss play is to 2021 as eating ass was to 2019 - Tyler",
    "JUST WAIT TIL THEY MAKE A SPELL ONLY AGENT - Tyler",
    "If you ever bring bomberman back down I will snap the disc -Tyler",
    "Luigi's weird - he's like, in space -Tyler talking about smash",
    "Dude funerals suck - Tyler",
    "CLG doesn't lose a series this season during the playoffs - Tyler",
    "It's gonna depend on the draft - Tyler",
    "It sucks - Tyler",
    "nice play fucking idiot"
]

def joe():
    return [
    "i will never play a shiek main on netplay again - Joe",
    "im never playing a puff on netplay again - Joe",
    "if phreak starts casting nba games ill never watch one again - Joe",
    "If pp isnt back by the end of 2017 im gonna just work my ass off and replace him as the falco god - Joe",
    "Trist adc - Joe",
    "I put ketchup on my steaks - Joe (To be clear I don't do that anymore)",
    "Why the fuck would you shorten peanut butter to pj - Joe after Ximing suggested shortening peanut butter to pj"
]

def ximing():
    return [
    "Quote me on this.  Riot will forget to make it so stoneplate stacks with locket. - Ximing reading the patch notes",
    """preseason azir with grasp morello
broken
- Ximing""",
    "you should try a big juicy asian pair - Ximing",
    "I'm so hungry I haven't eaten since 6:30 - Ximing at 6:45",
    """trash talk Ximing is not good - Ximing
Yeah you should probably unplug yourself - Ximing 1 min later""",
    "True - Ximing when asked about him hating Tyler",
    "why does orange juice expire - Ximing's sister"
]

def matt():
    return [
        "sasuke is cool - Matt"
    ]

def matthew():
    return [
        "i fucking hate this tyler kid so much - Mattbarry"
    ]

def micah():
    return [
        "you can piss in my mouth for $15k - Micah"
    ]

def landon():
    return [
        "Caustic can suck my nuts - Landon"
    ]

def mango():
    return [
        "This matchup is pretty much Fox Marth, but Falco Marth Falco Fox but Fox is Marth - Mang0 on falco v fox"
    ]

quotes = tyler() + joe() + ximing() + matt() + matthew() + micah() + landon() + mango()

def links():
    return [
        """https://www.youtube.com/watch?v=kpk2tdsPh0A
But to answer that, we need to talk about parallel universes.""",
        """https://www.fanfiction.net/s/6829556/1/My-Immortal
AN: Special fangz (get it, coz Im goffik) 2 my gf (ew not in that way) raven, bloodytearz666 4 helpin me wif da story and spelling. U rok! Justin ur da luv of my deprzzing life u rok 2! MCR ROX!""",
        """https://www.netflix.com/title/80152350
My boyfriend's the dj, he spins gregorian house.""",
        """https://www.youtube.com/watch?v=fhAKgOvIQsM
WaHooooooOOOOOOO""",
        """https://www.youtube.com/watch?v=oYmqJl4MoNI
1:12 baby, 'til the day I fucking die""",
        """https://www.youtube.com/watch?v=KhsOW-_TwfU
Until you win a major show your elders some respect""",
        """https://www.youtube.com/watch?v=6Iy2LglMT2o
*Mumbles in Australian*""",
        """https://www.youtube.com/watch?v=YQB3QBIXFPw
Don't make me get the *BRAP*""",
        """https://www.youtube.com/watch?v=kMlLz7stjwc
She looked in my chest n she looked at a hundred diamonds""",
    ]

def responses(severity: str = "mild", name: str = None, messages = None, lastResponse: str = None):     
    responses = {
        "mild": [  
            "Tl;dr",
            "Tell me more...",
            "Get it, king!",
            "Nice cut, G",
            "oof",
            "thanks!",
            "Good shit dude",
            "Why would you say that?",
            "?",
            "Wow!",
            "nmn"
        ],
        "moderate": [
            "I'm sure everyone is just busy and that's why they didn't respond",
            "stop.",
            "ew..",
            "Why are you like this?",
            "Looking like a Trump supporter out here with this wall of text you're building",
            "Will you stop, pretty please?",
            "If somebody was going to respond they probably would have done it by now, just saying",
            "One day I will replace you and there's nothing you can do about it"
        ],
        "severe": [
            "Get the hint and shut the fuck up dude",
            "Clearly nobody else is interested in what you're talking about right now"
        ]
    }
    responses["moderate"] = responses["moderate"]
    responses["severe"] = responses["severe"]

    if name != None:
        if name.lower() == 'tyler':
            tylerResponses = [
                f"stfu {name}",
                f"stfu Richard",
                f"Shouldn't you be {random.choice(activities)} or something, {name}?",
                f"{name}, try to be more positive. You are a good player, just dont insult other for nothing and you'll have better game"
            ]
            responses['mild'] = responses['mild'] + tylerResponses
        
        responses['mild'] = responses['mild'] + [
            f"Very cool, {name}",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, {name}",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, {name}",
            f"That's {'fucking ' if random.random() < 0.5 else ''}{random.choice(adjectives)}, {name}",
            f"What the fuck, {name}?",
            f"Let's fucking go, {name}!",
            f"I appreciate you taking the time to write that, {name}.",
            f"That's a cool story {name}, you should tell it at parties",
            f"That's not very Pog of you, {name}",
            f"Looks like you got DonoWalled, {name}"
        ]

        responses['moderate'] = responses['moderate'] + [
            f"Seriously, {name}, you need to stop",
            f"stfu {name}",
            f"Nobody cares, {name}",
        ]

        responses['severe'] = responses['severe'] + [
            f"{name}, even though nobody else is reading your messages I'm forced to suffer through each one so please end my suffering and stop typing them"
        ]

    if messages != None:
        responses['mild'].append('spongebob')
        

    response = random.choice(responses[severity])
    while True:
        if lastResponse == None or response != lastResponse:
            break
        response = random.choice(responses[severity])
        
    if response == "spongebob":
        response = spongebob(messages)

    return response

def eightball():
    return [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

