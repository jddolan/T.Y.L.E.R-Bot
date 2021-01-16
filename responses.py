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
    "you may have gotten more kills than me - Tyler",
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
    "i will never play a shiek main on netplay again - Joe",
    "im never playing a puff on netplay again - Joe",
    "if phreak starts casting nba games ill never watch one again - Joe",
    "Quote me on this.  Riot will forget to make it so stoneplate stacks with locket. - Ximing reading the patch notes",
    "If pp isnt back by the end of 2017 im gonna just work my ass off and replace him as the falco god - Joe",
    "Trist adc - Joe",
    """preseason azir with grasp morello
broken
- Ximing""",
    "i fucking hate this tyler kid so much - Mattbarry",
    "you should try a big juicy asian pair - Ximing",
    "you can piss in my mouth for $15k - Micah",
    "sasuke is cool - Matt",
    "I'm so hungry I haven't eaten since 6:30 - Ximing at 6:45",
    "If you ever bring bomberman back down I will snap the disc -Tyler",
    "Luigi's weird - he's like, in space -Tyler talking about smash",
    "This matchup is pretty much Fox Marth, but Falco Marth Falco Fox but Fox is Marth - Mang0 on falco v fox",
    "why does orange juice expire - Ximing's sister",
    "Dude funerals suck - Tyler",
    "CLG doesn't lose a series this season during the playoffs - Tyler",
    "It's gonna depend on the draft - Tyler",
    """trash talk Ximing is not good - Ximing
Yeah you should probably unplug yourself - Ximing 1 min later""",
    "I put ketchup on my steaks - Joe (To be clear I don't do that anymore)",
    "It sucks - Tyler",
    "True - Ximing when asked about him hating Tyler",
    "Caustic can suck my nuts - Landon"
]

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
        "If somebody was going to respond they probably would have done it by now, just saying",
        "One day I will replace you and there's nothing you can do about it"
    ],
    "severe": [
        "Get the hint and shut the fuck up dude",
        "Clearly nobody else is interested in what you're talking about right now",
        "Tyler, even though nobody else is reading your messages I'm forced to suffer through each one so please end my suffering and stop typing them",
    ]
}
responses["moderate"] = responses["moderate"] + responses["mild"]
responses["severe"] = responses["severe"] + responses["moderate"]