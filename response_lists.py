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

quotes = [
    "You add a meet and cheese board to anything and you up the class by 3 points",
    "Im a top 3 defender at my home courts quote it",
    "Water electric quote it - Tyler speculating on the typing of Sobble",
    "Knicks making room for kyrie and KD quote me on it",
    "Lebron is dropping 55 in game 7 quote me",
    "leffen's not dropping a GAME tomorrow quote it",
    "I just want to wear a fucking kimono",
    "3 Danish teams in the top 10 by the end of 2017 for csgo",
    "belgium vs france in the world cup final quote it",
    "G2 is winning world's quote me on it",
    """Liquid vs EG grand final
EG from losers
Quote it""",
    """LFY that team who fucked shit up in the groups
out in semis
actually quarters
quote it""",
    "DND was the best game mode quote that one",
    "this is the time g2 won't choke at an international event",
    "you may have gotten more kills than me",
    "ill have it done by tonight quote me on that",
    "quote me on this im gonna win joe's family group",
    """corey we're playing tonight
ok
?
quote me on that""",
    "I guess I'm just a weeb guys.",
    "Piss play is to 2021 as eating ass was to 2019",
    "JUST WAIT TIL THEY MAKE A SPELL ONLY AGENT",
]

commands: dict = {
    '!about': "This is a bot designed to respond to Tyler when other people aren't. Created by Joe",
    '!quote': "provides a quote"
    '!help': '''Valid Commands: 

!about: More information about the bot
!help: A list of valid commands for the bot
!quote: Provides a random quote from a time when Tyler said quote me on it, pin it, or something along those lines'''
}

responses = {
    "mild": [
        f"stfu {'Tyler' if random.random() < 0.75 else 'Richard'}",
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
        "Good shit dude",
        "Why would you say that?",
        "spongebob",
        "I appreciate you taking the time to write that, Tyler.",
        "That's a cool story Tyler, you should tell it at parties",
        "That's not very Pog of you, Tyler",
        "?",
        "Wow!",
        "nmn",
        "Looks like you got DonoWalled, Tyler",
        "nice play fucking idiot",
        "Tyler, try to be more positive. You are a good player, just dont insult other for nothing and you'll have better game",
        f"Shouldn't you be {random.choice(activities)} or something, Tyler?"
    ],
    "moderate": [
        "Why are you like this?",
        "Seriously, Tyler, you need to stop",
        "Looking like a Trump supporter out here with this wall of text you're building",
        "Will you stop, pretty please?",
        "If somebody was going to respond they probably would have done it by now, just saying"
    ],
    "severe": [
        "Get the hint and shut the fuck up dude",
        "Clearly nobody else is interested in what you're talking about right now",
        "Tyler, even though nobody else is reading your messages I'm forced to suffer through each one so please end my suffering and stop typing them",
    ]
}
responses["moderate"] = responses["moderate"] + responses["mild"]
responses["severe"] = responses["severe"] + responses["moderate"]