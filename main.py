import os
import discord
import requests
import json
import random
from discord.ext import commands
from requests import get
from replit import db

client = discord.Client();
my = os.environ['TOKEN']

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there, soldier.",
  "You are a great soul."
]
appreciation = [
  "Thank You bot",
  "Thank you bot",
  "Thank You D-Bot",
  "Thank you D-Bot",
  "Thank You Bot",
  "Thank you Bot",
  "Thank You D-bot",
  "Thank you d-bot",
  "Thank you d-Bot",
  "Thank You D-BOT",
  "Thank you dbot",
  "Thank You dbot",
  "Thank You Dbot",
  "Thank you Dbot",
  "Thank you DBOT",
  "Thank You DBOT",

  "thank You bot",
  "thank you bot",
  "thank You D-Bot",
  "thank you D-Bot",
  "thank You Bot",
  "thank you Bot",
  "thank You D-bot",
  "thank you d-bot",
  "thank you d-Bot",
  "thank You D-BOT",
  "thank you dbot",
  "thank You dbot",
  "thank You Dbot",
  "thank you Dbot",
  "thank you DBOT",
  "thank You DBOT",

  "Thank u bot",
  "Thank u bot",
  "Thank u D-Bot",
  "Thank u D-Bot",
  "Thank u Bot",
  "Thank u Bot",
  "Thank u D-bot",
  "Thank u d-bot",
  "Thank u d-Bot",
  "Thank u D-BOT",
  "Thank u dbot",
  "Thank u dbot",
  "Thank u Dbot",
  "Thank u Dbot",
  "Thank u DBOT",
  "Thank u DBOT",

  "thank u bot",
  "thank u D-Bot",
  "thank u Bot",
  "thank u D-bot",
  "thank u d-bot",
  "thank u d-Bot",
  "thank u D-BOT",
  "thank u dbot",
  "thank u dbot",
  "thank u Dbot",
  "thank u Dbot",
  "thank u DBOT",
  "thank u DBOT",

  "Thanks bot",
  "Thanks bot",
  "Thanks D-Bot",
  "Thanks D-Bot",
  "Thanks Bot",
  "Thanks Bot",
  "Thanks D-bot",
  "Thanks d-bot",
  "Thanks d-Bot",
  "Thanks D-BOT",
  "Thanks dbot",
  "Thanks dbot",
  "Thanks Dbot",
  "Thanks Dbot",
  "Thanks DBOT",
  "Thanks DBOT",

  "thanks bot",
  "thanks bot",
  "thanks D-Bot",
  "thanks D-Bot",
  "thanks Bot",
  "thanks Bot",
  "thanks D-bot",
  "thanks d-bot",
  "thanks d-Bot",
  "thanks D-BOT",
  "thanks dbot",
  "thanks dbot",
  "thanks Dbot",
  "thanks Dbot",
  "thanks DBOT",
  "thanks DBOT",
]
thanks = [
  "Happy to help ya!",
  "Am always there for ya!",
  "Well that is part of my job, to bring smile to your face!",
  "I am always looking out for ya!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n" + " -" + json_data[0]['a']
  return (quote)

def update_encouragements(encouraging_msg):
  if("encouragements" in db.keys()):
    encouragements = db["encouragements"]
    encouragements.append(encouraging_msg)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_msg]

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if(len(encouragements) > index):
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  msg = message.content

  if msg.startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('Hey bot'):
    await message.channel.send('Howdy! champ.')

  if msg.startswith('hey bot'):
    await message.channel.send('Howdy! champ.')
  
  if msg.startswith('Hey D-Bot'):
    await message.channel.send('Howdy! champ.')

  if msg.startswith('hey D-Bot'):
    await message.channel.send('Howdy! champ.')

  if msg.startswith('Hello bot'):
    await message.channel.send('Howdy! champ.')

  if msg.startswith('hello bot'):
    await message.channel.send('Howdy! champ.')
  
  if msg.startswith('Hello D-Bot'):
    await message.channel.send('Howdy! champ.')

  if msg.startswith('hello D-Bot'):
    await message.channel.send('Howdy! champ.')

  # if msg.startswith('Thanks D-Bot'):
  #   await message.channel.send('Happy to help ya!')
  
  if msg.startswith('thanks bot'):
    await message.channel.send('Well that is part of my job!' + '\n' + 'To bring smile to your face')

  # if msg.startswith('Thanks bot'):
  #   await message.channel.send('I am always looking out for ya!')

  if db["responding"]:
    options = starter_encouragements
    # if encouragements in db.keys():
    #   options = options + db["encouragements"].value

    if (any(word in msg for word in sad_words)):
      await message.channel.send(random.choice(options))
 
  if (any(word in msg for word in appreciation)):
    await message.channel.send(random.choice(thanks))

  if msg.startswith("-new"):
    encouraging_msg = msg.split("-new ",1)[1]
    update_encouragements(encouraging_msg)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("-del"):
    encouragements = []
    if ("encouragements" in db.keys()):
     index = int(msg.split("-del",1)[1])
     delete_encouragements(index)
     encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("-list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("-responding"):
    value = msg.split("-responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is LIVE")
    else:
      db["responding"] = False
      await message.channel.send("Responding is OFF")

  if msg.startswith("-meme"):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await message.reply(embed=meme)

    


client.run(my)

