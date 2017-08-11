#!/usr/bin/env python3

import discord
import asyncio
import markovify
import random

client = discord.Client()
bot_token = 'MzQ1Njc3OTg0OTgxNTgxODI3.DG-zxA.ilaNlz-MKma2S-vt7wM4YlPZ3_0'

# Get raw text as string.
with open("text.txt", encoding="utf8") as f:
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
  if message.content.startswith('p!ping'):
    await client.send_message(message.channel, 'pedl pedl')
  elif message.content.startswith('p!ai'):
    # Generate a sentence with a random overlap ratio for variety
    new_mes = text_model.make_short_sentence(140, tries=100, max_overlap_ratio=random.randrange(10, 55))
    await client.send_message(message.channel, new_mes)

client.run(bot_token, bot=True)



