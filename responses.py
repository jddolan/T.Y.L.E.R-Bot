import random
from bot import spongebob

async def validCommands():
    return {
    '!8ball': """**!8ball** <question: Optional> provides an answer from the magic 8-ball""",
    '!about': """**!about** provides information about the bot""",
    '!addquote': """**!addquote** <quote> <user> submits the quote to be added to the bot's list of randomly
generated quotes. Must be approved by Joe and the person being quoted""",
    '!coinflip': """**!coinflip** <choice: Optional> flip a coin, optionally choose heads or tails""",
    '!help': """**!help** <command: Optional> provides a list of valid commands for the bot""",
    '!joke': """**!joke** generates a funny joke""",
    '!lenny': """**!lenny** generates a random lenny face ( ͡° ͜ʖ ͡°)""",
    '!link': """**!link** provides a link to a piece of content significant to the Flat Earf Rules discord server""",
    '!quote': """**!quote** <name: Optional> provides a quote, if a name is not provided the quote will be
randomly selected from all stored quotes""",
    '!response': """**!response** <name: Optional> generates a random response, optionally include the name
of the person the response is for""",
    '!roll': """**!roll** <XdY> will roll a Y-sided die X times""",
    '!rps': """**!rps** <choice> choose rock paper or scissors and play against the bot""",
    '!scan': """**!scan** is not recommended to use unless you have access to the bot's logs, as it will serve
no purpose without them. Will scan a server and find messages that contain the passed
string.""",
    '!test': """**!test** this command will generally do nothing aside from showing a message related to
something in development"""
}

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
\*Mumbles in Australian\*""",
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

def jokes():
    return [
        """Why did the chicken go to the library?
To check out a bawk.""",
        """What’s a parasite?
A place you go in Paris.""",
        """What did the horse say when he fell down?
Help, I’ve fallen and I can’t giddyup!""",
        """Why did the basketball player bring a duck to the game?
He wanted to shoot a foul shot.""",
        """How do you communicate with a fish?
You drop it a line.""",
        """How do billboards talk?
Sign language.""",
        """What do you call a grandmother who tells jokes?
A gram cracker.""",
        """What did the lunch lady say to Luke Skywalker?
Use the forks, Luke.""",
        """Why was the cat afraid of the tree?
Because of it’s bark!""",
        """What do you call a horse that likes arts & crafts?
A hobby horse.""",
        """Why do shoemakers go to heaven?
They have good soles.""",
        """What did one shoe say to the other?
Don’t stick your tongue out at me!""",
        """Why don’t lobsters share?
Because they are shellfish.""",
        """What is thin, white, and scary?
Homework.""",
        """Did you hear the joke about the toilet?
Never mind, it’s too dirty.""",
        """Do you know what’s really odd?
Numbers not divisible by 2.""",
        """When do you stop at green and go at red?
When you’re eating a watermelon""",
        """What word is always spelled incorrectly?
Incorrectly.""",
        """What do you call a happy cowboy?
A jolly rancher.""",
        """Why do we not tell secrets in a corn patch?
Too many ears.""",
        """Where does a penguin keep his money?
A snow bank.""",
        """What do you call a baby with a drum?
A baby boomer.""",
        """When does it rain money?
When there’s a change in the weather.""",
        """What kind of bean can’t grow?
A jellybean.""",
        """What did the buffalo say to his kid when he went to work?
Bison.""",
        """What should you do if your dog is missing?
The lost and hound.""",
        """What planet is like a circus?
Saturn, it has three rings!""",
        """What’s green and fluffy and comes from mars?
A martian mellow.""",
        """Why do phones ring?
Because they can’t talk!""",
        """How do you turn soup into gold?
Add 24 carrots.""",
        """What kind of bear has no teeth?
A gummy bear.""",
        """What do you call a sad strawberry?
A blueberry.""",
        """What runs around a soccer field but never moves?
A fence.""",
        """Why did they bury the battery?
Because it was dead.""",
        """What’s a parasite?
A place you go in Paris.""",
        """What is the raddest aircraft?
The hella-copter.""",
        """What do you call a car that never sleeps?
Cargo!""",
        """How does the moon cut his hair?
Eclipse it.""",
        """Where do kittens go on their class trip?
To the meowseum.""",
        """Why did the orange lose the race?
It ran out of juice.""",
        """Why don’t birds follow directions?
They like to wing it.""",
        """What do sneezes wear on their feet?
Their ahhhh-shoes.""",
        """Why did the farmer bury all his money?
To make his soil rich.""",
        """Why did the banana go to the doctor?
He wasn’t peeling well.""",
        """What kind of shoes do frogs wear?
Open toed.""",
        """What do you call a lazy kangaroo?
A pouch potato.""",
        """What falls down but never gets hurt?
Snow!""",
        """What did zero say to 8?
Nice belt.""",
        """What do wolves say when they are introduced?
Howl do you do?""",
        """Why do marsupials make such good tea?
It’s koala tea.""",
        """What do you call a cat that eats lemons?
A sour puss.""",
        """What did the bee say to the flower?
Hi bud!""",
        """What building has the most stories?
The library.""",
        """What do you call a pile of cats?
A meowtain.""",
        """What do you call a fake noodle?
An impasta.""",
        """What lies at the bottom of the ocean and twitches?
A nervous wreck.""",
        """What is ten and ten?
Numbers.""",
        """Who took the frog’s car?
It was toad.""",
        """What has no legs but can do a split?
A banana.""",
        """What is the best way to raise a child?
In an elevator.""",
        """Where do hamsters go on vacation?
Hamsterdam.""",
        """Why was the tomato blushing?
It saw the salad dressing.""",
        """What is always behind the time?
The back of the clock.""",
        """What do you call an avid gardener?
Herb.""",
        """Why should you never use a dull pencil?
It’s pointless.""",
        """What did the fork say to the spoon?
Who’s that sharp guy next to you?""",
        """What should you do if you don’t have any rubber bands?
See if you can find a plastic orchestra.""",
        """Why did the skeleton go to the movie by itself?
It had no body.""",
        """What do you get if you cross a stereo and a fridge?
Very cool music!""",
        """Why didn’t the little girl want to leave nursery school?
She wanted to be a nurse when she grew up.""",
        """What do frogs order at a restaurant?
French flies.""",
        """What event do spiders love to attend?
Webbings.""",
        """Why do ducks have tail feathers?
To cover their buttquacks.""",
        """What kind of shoes do private investigators wear?
Sneak-ers.""",
        """What game does the sky love to play?
Twister.""",
        """What do astronauts eat for dinner?
Launch meat.""",
        """What did one campfire say to the other?
Let’s go out one of these days!""",
        """What does a car run on?
Wheels.""",
        """Can February march?
No, but April May.""",
        """What did Tennessee?
The same thing Arkansas.""",
        """What did the egg say to the frying pan?
You crack me up.""",
        """How do bulls write?
With a bullpen.""",
        """How do you get an alien baby to sleep?
You rocket.""",
        """What did the hurricane say to the island?
I’ve got my eye on you!""",
        """What do you all a fancy sea creature?
Sofishticated.""",
        """Why did the bones cross the street?
They didn’t, the dogs ate them.""",
        """Why did the student eat his homework?
The teacher said it was a piece of cake.""",
        """What prize do you get for putting your phone on vibrate?
The no bell prize.""",
        """What is a tree’s favorite drink?
Root beer.""",
        """Why don’t ducks tell jokes while they are flying?
Because they would quack up.""",
        """What is the biggest room in the world?
Room for improvement.""",
        """What room can never be entered?
A mushroom.""",
        """Why couldn’t the shoes go out and play?
They were all tied up.""",
        """Why didn’t the leopard go on vacation?
He couldn’t find the right spot.""",
        """What did the skunk say when the wind changed?
It’s all coming back to me now.""",
        """What do you get when you cross a pig with a Christmas tree?
A porcupine.""",
        """Why is a pancake like the sun?
Because it rises in the yeast and rests in the vest.""",
        """Why do hamburgers fly south for the winter?
So they won’t freeze their buns.""",
        """What kind of tree grows in your hand?
A palm tree.""",
        """Why do we not tell secrets in a corn patch?
Too many ears."""
    ]