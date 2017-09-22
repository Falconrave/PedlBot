import discord
import asyncio
import markovify
import random
import re

client = discord.Client()
# invalid token
bot_token = 'MzQ1Njc3OTg0OTgxNTgxODI3.DG-zxA.ilaNlz-MKma2S-vt7wM4YlPZ3'

# Get raw text as string.
with open("text.txt", "r+", encoding="utf8") as f:
  text = f.read()

# Build model.
text_model = markovify.NewlineText(text)


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.event
async def on_message(message):
  msg_string = re.search(r'^\w', message.content)
  print(str(msg_string))
  if message.content.startswith('*ai'):
    print(message.author)
    # Generate a sentence with a random overlap ratio for variety
    new_mes = text_model.make_short_sentence(340, tries=100, max_overlap_ratio=random.randrange(10, 35))
    await client.send_message(message.channel, new_mes)
  elif message.content.startswith('*money'):
    await client.send_message(message.channel, 'Give jeremiah his fucking runescape money back dork you fucking imbeccile.')
  elif msg_string and message.author != "PedlBot#2293" and not message.content.startswith('`'):
    # append the text of message to the text.txt file
    with open("text.txt", "a+", encoding="utf8") as f:
      f.write(str(message.content) + "\n")
    print(message.author, "sent a message: ", message.content)

    

client.run(bot_token, bot=True)