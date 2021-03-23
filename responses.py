import random
import os

adminId: int = int(os.environ.get('JOEID'))

def validCommands():
    return {
        '!8ball': """**!8ball** <question: Optional> provides an answer from the magic 8-ball""",
        '!about': """**!about** provides information about the bot""",
        '!addquote': """**!addquote** <quote> <user> submits the quote to be added to the bot's list of
    randomly generated quotes. Must be approved by Joe and the person
    being quoted""",
        '!coinflip': """**!coinflip** <choice: Optional> flip a coin, optionally choose heads or tails""",
        '!crush': """**!crush** generates a random Crush tweet""",
        '!help': """**!help** <command: Optional> provides a list of valid commands for the bot""",
        '!joke': """**!joke** generates a funny joke""",
        '!lenny': """**!lenny** generates a random lenny face ( ͡° ͜ʖ ͡°)""",
        '!link': """**!link** provides a link to a piece of content significant to the Flat Earf Rules
    discord server""",
        '!poll': """**!poll** <amount> <unit> "<prompt>" <answers> creates a poll that will end after the specified amount of time
        Example: !poll 1 day "Should we kick Mattbarry from the server?" Hell yeah, Yes, Definitely, Yep, For sure""",
        '!quote': """**!quote** [<name: Optional> <number: Optional>] provides a quote, if a name is not provided the
    quote will be randomly selected from all stored quotes""",
        '!reminder': """**!reminder** <amount> <unit> "<reminder>" sets a reminder that the bot will notify you about after the specified amount of time
        Example: !reminder 1 day "remind me to replace Tyler" """,
        '!response': """**!response** <name: Optional> generates a random response, optionally
    include the name of the person the response is for""",
        '!roll': """**!roll** <XdY> will roll a Y-sided die X times""",
        '!rps': """**!rps** <choice> choose rock paper or scissors and play against the bot""",
        '!scan': """**!scan** is not recommended to use unless you have access to the bot's logs, as
    it will serve no purpose without them. Will scan a server and find
    messages that contain the passed string.""",
        '!test': """**!test** this command will generally do nothing aside from showing a message
    related to something in development"""
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
    "nice play fucking idiot - Tyler"
]

def joe():
    return [
    "i will never play a shiek main on netplay again - Joe",
    "im never playing a puff on netplay again - Joe",
    "if phreak starts casting nba games ill never watch one again - Joe",
    "If pp isnt back by the end of 2017 im gonna just work my ass off and replace him as the falco god - Joe",
    "Trist adc - Joe",
    "I put ketchup on my steaks - Joe (To be clear I don't do that anymore)",
    "Why the fuck would you shorten peanut butter to pj - Joe after Ximing suggested shortening peanut butter to pj",
    "It's not gay to like cum, It's gay to like men. I don't like the men, I just like their cum. - Joe"
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
        "sasuke is cool - Matt",
        "I make bombs - Matt"
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
        """https://www.youtube.com/watch?v=d18s1VpnOHQ
I love building bricks with minecrap""",
        """https://www.youtube.com/watch?v=Z0Uh3OJCx3o
We can be pro Fornite gamers!"""
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
                f"{name}, try to be more positive. You are a good player, just dont insult other for nothing and you'll have better game",
                f"He's just trying his best, {name}"
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
            f"Nobody cares, {name}"
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

def eightball():
    return [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – absolutely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Yeah, probably.",
        "Fuck yeah.",
        "Hell yeah.",
        "I like to think so.",
        "For sure.",
        "100%.",
        "There's no way that that isn't not what the case isn't.",
        "For sure for sure.",
        "I'm leaning toward yes.",
        "I'm not completely sure but probably.",
        "Definitely.",
        "I think so.",
        "You shouldn't have even consulted me, the answer is obviously yes.",
        "Of course.",
        "I'm afraid so.",
        "It surely must be so.",
        f"I'll leave that up to <@{adminId}>",
        "I have no clue, sorry.",
        "Fuck if I know.",
        "Concentrate and ask again.",
        f"Answer not definitive, but I'm leaning towards {'yes' if random.random() < 0.5  else 'no'}",
        f"Let's flip a coin! Heads is yes, tails is no. Result: ***{'Heads' if random.random() < 0.5 else 'Tails'}***!",
        "That could go either way, there are too many variables to say for sure.",
        f"I'm not able to definitively answer that question, but if getting an answer will make you feel better, then {'yes' if random.random() < 0.5 else 'no'}.",
        "Idk.",
        r'¯\\_ツ_/¯',
        "If only that were the case.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Fuck no.",
        "No.",
        "Nah.",
        "Nope.",
        "Unfortunately no.",
        "Never.",
        "There's no way that that isn't not what the case is.",
        "No shot.",
        "Probably not.",
        "I'm leaning toward no.",
        "I'm not completely sure but probably not.",
        "Absolutely not. Are you out of your mind?"
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

def crush():
    # https://www.youtube.com/watch?v=G708_N5yQT8
    return [
        """we have a 15 year old wobbler that gets 5th place at our locals while smoking cigs outside the venue between every round and he can undoubtedly beat any of the grown ass men on vgbootcamp trying to tell you melee is a game of self expression""",
        """i’m the only decent player that doesn’t get asked by the hotel check-in person if i’m “here for the local video game expo""",
        """call me “late to the party” or “old” or “a puritan” or “morally compromised” but xxx tentacion has a couple good songs""",
        """it’s so admirable how committed and determined i am to not work together with my teammate at all in doubles""",
        """i was actually pretty sheltered growing up. whenever i was drunk and wanted chick fil a my parents wouldn’t let me drive there because they didn’t want me being exposed to homophobia""",
        """the key to twitter fame is insulting enough people in 140 characters that it becomes social commentary and not a subtweet""",
        """why do all ice climbers players look like they collect rare insects""",
        """just had a very fruitful call with @Sora_Sakurai. UCF is here to stay""",
        """once you get to the ~95th percentile of eyebrows... that’s when these very real and deeply personal connections are made. like speaking a language only you can understand""",
        """i look like your dad dude why do you want beef with me. are you really tryna beef with your dad""",
        """none of these guiltless fucks are washing their hands i can’t do this""",
        """my goal is to be a late 20s white guy w/ a beard that has “*position* @currentcompany, previous: @bigsoullesscompany @failedstartup @evenshittierbigcompany” in their twitter bio. bonus points for “tweets are my own” or if i RT/reply to things you find in the twitter moments tab""",
        """I don’t “give up clout” anymore. I’m too old to give up clout. If I’m giving up clout we gotta be building or working on something together.""",
        """i lose part of my soul every time someone speaks in twitch emotes to me""",
        """this applies to every aspect of tournaments... i used to be this underground avant indie noir heartthrob... nowadays i don’t even have the heart to cross out reptilian signatures in place of writing my own""",
        """being less known+rank 49 was sick cause every time i got flown out to regionals/locals they were hosted by very competent TOs with impeccable taste in melee players. now i have to vet everyone or else i end up indirectly supporting random nerds that don’t understand the vision""",
        """redman’s mtv cribs episode has had such a profound impact on my ideas in every area of life""",
        """smash at IUD was great. gg to all my very formidable and multidimensional opponents. will definitely be back for full bloom 5 provided my mason dixon force field doesn’t get any stronger""",
        """i’m out here being nice to people saying hi and shit""",
        """playing chu dat feels like yugioh playing wizzrobe feels like baseball""",
        """here’s something special about doing team combos with one of your close pals... really hope doubles gets more of a spotlight in the future""",
        """i like to listen to house of balloons on plane rides to flyover states for juxtaposition""",
        """i wish the average melee spectators were 14 year old girls instead of 14 year old boys so i could actually have some fans""",
        """way too good at rick ross ad libs to be doing them for free""",
        """i like how melee top 8s these days alternate between sets where melee looks glorious and sets where melee looks godawful""",
        """my entire high level melee experience is me minding my own business dashdancing in the middle of battlefield while some sweaty dude 8 years older than me spams low execution high reward options""",
        """teams is garbage and exacerbates all of melee's flaws btw
it devolves to marths/peaches/shieks corner/float/ledgestalling while foxes and honor code shieks play watered down 1v1s. pppl usually settle as self identifying "teams specialists" after getting bodied in singles for years""",
        """i'd like to apologize for dodging so many messages and inquiries... but the only interviews i give are to god""",
        """every smash game other than melee is just brawl. don't let the marketing fool you""",
        """didn't opt in for trash summit because i'm above that shit""",
        """i got it for $14 on bigcartel back when that was a thing tbh but i will resell it for 100 for summit funds once i get unbanned from grailed""",
        """you look better with the crt off""",
        """all your favorite players would lose to your local high school wobbler bro""",
        """i can't talk to girls unless UCF is on""",
        """i wish i wasn't a top player so i could spell competitive completely wrong in my bio and none of my 59 followers would call me out""",
        """tfw you have the most woke neutral game of all time but still lose to robots wearing bootcut jeans that have been spamming fadeback aerials and shieldgrab for the past decade""",
        """I deleted my Twitter. Finding my opinions became too easy.""",
        """someone get me a fake id that says i'm > 25. i won't try to run for president i promise""",
        """i swear i have the necessary clout to rent a car. the feds would never know""",
        """if u put a non negligible amount of money on my compendium goal i promise to pretend to be interested when u tell me how u went 3-2 in pools""",
        """all my acts of kindness to others can be attributed to me seeing myself in everyone""",
        """it's honestly pretty crazy how much people's personalities (or lack thereof usually) are reflected in the way they play melee""",
        """i wish people would put in as much effort into their compliments as i do in giving people reasons to compliment me""",
        """who crosses out other people's signatures before signing their own? basically me and kanye west""",
        """most cost-effective way to fill an entire wall with mirrors? asking for a friend""",
        """don't really talk much cause i have trouble speaking in anything other than poetry""",
        """i'm like king midas except everything i touch turns to xanax""",
        """people still pretending that having low testosterone isn't an advantage in melee when the average height of the MIOM top 40 is 5'7""" + '"',
        """lost a stock 4 times and made eye contact 3 times. made it out of my pool winners side""",
        """to win in melee u must be very critical of who u are while somehow still having a completely delusional and exaggerated sense of self worth""",
        """being a public figure is all about the balance of maintaining your mystique and bragging about drug use""",
        """dropped from genesis red
not plaing in tourneys ran by ppl who rig brackets/compromise the integrity of competition to get stream viewers""",
        """beat nicholas m titty to make it out of pools. if the TOs have any sort of morals they'll reseed but if not peace out norcal""",
        """@ seeders: there are so many imperfect things in this world for you to fuck up with your terrible standards. why's it gotta be melee?""",
        """when I drink fiji water it's supposed to be self parody but nobody gets it so I just end up looking like more of an asshole""",
        """vanilla ice cream is the sluttiest flavor and nothing else comes close. it's the most honest too"""
    ]