import os
import random
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Make sure on Render/PythonAnywhere you set an Environment Variable 
# named GROUPME_BOT_ID with your actual string value!
BOT_ID = os.environ.get("GROUPME_BOT_ID")

# Your custom list of Chuck Norris jokes (Fixed syntax errors)
JOKES = [
    "Chuck Norris counted to infinity. Twice.",
    "When the Boogeyman goes to sleep every night, he checks under the bed for Chuck Norris.",
    "Chuck Norris can slam a revolving door.",
    "Death once had a near-Chuck-Norris experience.",
    "Chuck Norris doesn't wear a watch. He just decides.",
    "Chuck Norris was asked to write an essay on courage. He submitted a blank paper with his name on top.",
    "Chuck Norris didn't die. He leveled up.",
    "People once tried to name a bridge after Chuck Norris but changed their minds because no one will cross Chuck Norris.",
    "Chuck Norris isn't the chosen one. He chooses the chosen one.",
    "Chuck Norris makes onions cry.",
    "Chuck Norris has no reflection when he walks up to a mirror, because there is only one Chuck Norris.",
    "When God said 'Let there be light' Chuck Norris said 'Say please'.",
    "Chuck Norris can see John Cena.",
    "Chuck Norris can touch MC Hammer.",
    "Chuck Norris doesn't have a mouse for his PC. He uses a lion.",
    "Chuck Norris knows Victoria's Secret.",
    "Chuck Norris doesn't do pushups. He pushes the earth down.",
    "When Chuck Norris leaves the gym, the exercise machines are exhausted.",
    "Chuck Norris invented skydiving, and then invented the parachute, so everyone else could try.",
    "The dinosaurs only made Chuck Norris angry once.",
    "Chuck Norris lifts weights to give gravity a break.",
    "Chuck Norris is the reason Waldo is hiding.",
    "Chuck Norris can cut a knife using butter.",
    "The Great Wall of China was originally created to keep Chuck Norris out. It didn’t work.",
    "Chuck Norris once took a long nap. We call it 'The Dark Ages'.",
    "The Universe isn't expanding. It's fleeing Chuck Norris.",
    "Chuck Norris is the reason we are alone in the universe.",
    "Chuck Norris has no Ctrl key on his keyboard, because he is always in control.",
    "Chuck Norris can divide by zero.",
    "Chuck Norris once arm wrestled Superman. The loser had to wear their underwear outside their pants.",
    "Chuck Norris once gave a horse an uppercut. That's why we have giraffes.",
    "Chuck Norris can make minute rice in 30 seconds.",
    "Chuck Norris once challenged the sun to a staring contest. The sun blinked.",
    "Chuck Norris once fell into a pit of snakes. He climbed out with a new belt, vest, and pair of boots.",
    "Chuck Norris doesn't debug his code. He just stares it down until it confesses.",
    "Chuck Norris was in a heated debate with a lady, and he told her to calm down. And she did.",
    "Before he forgot a gift for Chuck Norris, Santa was real.",
    "Chuck Norris once laughed slightly. We now call this 'chuckling'.",
    "Chuck Norris doesn't flush the toilet. He scares the crap out of it.",
    "Chuck Norris doesn't mow his lawn. He just goes outside every morning and dares it to grow.",
    "While Jesus can walk on water, Chuck Norris can swim through dry land.",
    "Chuck Norris played in every Star Wars movie and spinoffs. He was the force.",
    "When Chuck Norris left his parents' house, he told his dad 'You're the man of the house now'.",
    "Chuck Norris has a diary. It's called 'The Guinness Book of World Records'.",
    "The quickest way to a man’s heart is with Chuck Norris’s fist.",
    "Chuck Norris was once bit by a king cobra. After 5 days of agonizing pain, the cobra died.",
    "Chuck Norris can rub 2 ice cubes together to create a fire.",
    "Time heals all wounds, unless they came from Chuck Norris.",
    "Don't offer a penny for Chuck Norris' thoughts, because you can't handle Chuck Norris' thoughts.",
    "Chuck Norris never goes back to the drawing board. He's always right the first time.",
    "Fear knocked. Chuck Norris answered. Fear ran screaming.",
    "Chuck Norris picks apples from an orange tree and makes lemonade.",
    "Chuck Norris can seesaw alone.",
    "When Chuck Norris puts money into the parking meter, a gumball comes out.",
    "When driving, Chuck Norris always has the right of way.",
    "Chuck Norris' guess is better than yours.",
    "Chuck Norris can't get a taste of his own medicine because he doesn't know what medicine tastes like.",
    "Chuck Norris can tango alone.",
    "Chuck Norris never wakes up on the wrong side of the bed because all sides of the bed are the right one for Chuck Norris.",
    "Chuck Norris can flex his hair.",
    "Chuck Norris can walk uphill both ways.",
    "When he was in school, Chuck Norris never went to recess because he doesn't play around.",
    "Orion admires Chuck Norris' belt.",
    "Chuck Norris won a staring contest with Medusa.",
    "Chuck Norris can find the end of a circle.",
    "Chuck Norris can single-handedly surround his opponents.",
    "Fear itself is afraid of Chuck Norris.",
    "If Chuck Norris has ten apples, and you take two apples away, you have one second to give them back.",
    "On the seventh day, God rested. Chuck Norris worked out.",
    "Chuck Norris can win an arm wrestle with both hands tied behind his back.",
    "Chuck Norris doesn't just drive cars, he flies trains.",
    "Chuck Norris can build a snowman out of rain.",
    "The shortest distance between 2 points is whichever route Chuck Norris takes.",
    "The Internet consults Chuck Norris for information.",
    "Chuck Norris is allowed to double-dip.",
    "How many pushups can Chuck Norris do? All of them.",
    "Chuck Norris doesn't need a knife sharpener. He just combs the knives through his beard.",
    "When ghosts go camping, they tell Chuck Norris stories.",
    "Chuck Norris can dance the two-step with one foot.",
    "When Chuck Norris practices origami, he uses plywood.",
    "Which came first, the chicken or the egg? Only Chuck Norris knows.",
    "Chuck Norris doesn't just win. He allows you to lose.",
    "God lists Chuck Norris as his emergency contact.",
    "Chuck Norris recorded the making of the first video camera.",
    "No one sees Bigfoot because Bigfoot saw Chuck Norris.",
    "Chuck Norris has been to Mars. That's why there are no signs of life there.",
    "Chuck Norris can unscramble a scrambled egg.",
    "Chuck Norris doesn't worry about his aim because his bullets know better than to miss.",
    "Chuck Norris can do a wheelie on a unicycle.",
    "Lightning doesn't strike Chuck Norris' house because his house is the source of the lightning.",
    "Chuck Norris can bowl a perfect game with a marble.",
    "Jack is nimble, Jack is quick, but Jack can't dodge Chuck Norris' roundhouse kick.",
    "Chuck Norris can pull a hat out of a rabbit.",
    "There are two kinds of people in this world. Chuck Norris and everyone else.",
    "Chuck Norris doesn't dial the wrong number. You pick up the wrong phone.",
    "When death came to Chuck Norris, he asked 'Is it time?'",
    "Chuck Norris didn't cheat death. He won fair and square until he decided it was time.",
    "Chuck Norris can choke someone with a cordless phone.",
    "Chuck Norris once walked away from a fight with two broken ribs and a dislocated arm. He didn't give them back.",
    "Chuck Norris' favorite winter sport is uphill skiing.",
    "When Chuck Norris is late, everyone else apologizes for being early.",
    "Chuck Norris is never early. Time just can't keep up with Chuck Norris.",
    "Chuck Norris can give a cyclops two black eyes.",
    "Chuck Norris can punch a cyclops between the eyes.",
    "Everyone loves Chuck Norris. There isn't another option.",
    "Newborn babies cry because they've just entered a world with Chuck Norris in it.",
    "When Chuck Norris enters a room, he doesn't turn on the lights. He turns off the dark.",
    "Chuck Norris once split a rock in half with his bare hands. We now call that rock 'The Grand Canyon'.",
    "Chuck Norris had to stop skydiving because he decided that one Grand Canyon is enough.",
    "Chuck Norris once picked up a rock and tossed it into the air. We now call that rock 'the Moon'.",
    "Chuck Norris can sit in the corner of a round room.",
    "The only time Chuck Norris was wrong was when he thought he made a mistake.",
    "When Chuck Norris plays dodgeball, the balls dodge him.",
    "If it looks like chicken, smells like chicken, and tastes like chicken but Chuck Norris says it's beef, it's beef.",
    "Chuck Norris doesn't use an oven to prepare meals because revenge is a dish best served cold.",
    "If Chuck Norris owned a restaurant, the only thing on the menu would be the Knuckle Sandwich.",
    "Chuck Norris doesn't read books. He just stares them down until they give him the information he wants.",
    "Chuck Norris didn't die. He decided heaven was ready for him.",
    "Chuck Norris once threw a grenade and killed fifty men. Then, the grenade finally exploded.",
    "Chuck Norris' tears can cure cancer, too bad he never cries.",
    "Chuck Norris admitted to using stunt doubles in his movies, but only for the crying parts.",
    "Chuck Norris isn't dead. We are just unworthy to live in his reality.",
    "Chuck Norris actually died twenty years ago, and death finally built up the courage to tell him.",
    "The amount of roundhouse kick related deaths has gone up 13000% since 1940. Guess who was born then?",
    "Chuck Norris didn't die. God just needed a new bodyguard, so Chuck Norris volunteered for the role.",
    "Chuck Norris didn't die. He just wanted to have a word with 'the management'.",
    "Chuck Norris didn't die. God just needed an angel of war, so he asked Chuck Norris.",
    "When Chuck Norris entered heaven, he told the people there 'Fear not'.",
    "Chuck Norris didn't die. He is just asleep, and everyone is too afraid to wake him up.",
    "Chuck Norris didn't die. He is just heading to his rematch with Bruce Lee.",
    "People said 'Chuck Norris cannot die' so he proved us all wrong yet again.",
    "Chuck Norris wears sunscreen to protect the sun.",
    "Chuck Norris can teach blind people Braille in sign language.",
    "Chuck Norris build sand castles when he was a kid. We call them 'the pyramids'.",
    "Chuck Norris can read QR codes.",
    "When Chuck Norris gets pulled over, the cops get off with a warning.",
    "When Alexander Graham Bell invented the phone, he had two missed calls from Chuck Norris.",
    "Chuck Norris once met Stephen Hawking. Stephen stood up to offer him a seat.",
    "Chuck Norris doesn't tell jokes because no one would survive the punchline.",
    "While Chuck Norris was learning CPR, he brought the dummy to life.",
    "Chuck Norris once beat a dead man to life.",
    "Chuck Norris has a beautiful bear skin rug in his bedroom. The bear isn't dead, it's just too afraid to move.",
    "Chuck Norris once said 'come here' and the here came.",
    "Love once stared Chuck Norris in the eyes, now love is blind.",
    "Eclipses happen when the sun wants to hide from Chuck Norris.",
    "If you have $5 and Chuck Norris has $5, Chuck Norris has more money than you.",
    "Chuck Norris once heard that nothing can kill him so he tracked down nothing and killed it.",
    "Chuck Norris 'warming up' is the main cause of global warming.",
    "Chuck Norris once playfully punched a wall. That was the day Germany was reunified.",
    "Chuck Norris once skipped school for two days. Those days are now known as Saturday and Sunday.",
    "Chuck Norris plays Russian roulette with a full mag and always wins.",
    "Chuck Norris has no doors in his house. When he wants to go somewhere, he just looks at the wall, and the wall apologizes and moves out of his way.",
    "Chuck Norris once attended a feminist rally. He left with a sandwich and his shirt ironed.",
    "Chuck Norris has a petting zoo. It's called Australia.",
    "When Chuck Norris calls 911, he asks them what their emergency is.",
    "Chuck Norris was once bit by a rabid dog. The dog got better.",
    "Chuck Norris doesn't turn the shower on. He makes it cry.",
    "There is no such thing as natural selection, just a list of animals Chuck Norris allows to live."
]

@app.route('/', methods=['GET', 'POST'])
def webhook():
    # If it's just Cron-Job waking us up with a GET request
    if request.method == 'GET':
        return "Bot is awake!", 200
        
    # If it's GroupMe sending a message via POST
    data = request.get_json()
    if data.get('text') and data.get('sender_type') != 'bot':
        text_received = data['text'].strip().lower()

        if text_received == '/chucknorris':
            random_joke = random.choice(JOKES)
            send_message(random_joke)

    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id': BOT_ID,
        'text': msg
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
