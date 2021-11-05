import discord
import os
import json
from discord.ext import commands
from keep_alive import keep_alive

with open('dictionary_sed_to_eng.json') as f:
    se = json.load(f)
with open('dictionary_eng_to_sed.json') as f:
    es = json.load(f)    

bot = commands.Bot(command_prefix="!!")
client = discord.Client()

#not important, just debugging
@bot.event
async def on_start():
  print('Bot is ready...')

@bot.command()
async def test(ctx):
  await ctx.Send("DicSedelishBot just landed.")

@client.event
async def on_ready():
  print('DicSedelishBot Joined as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(message.content)
  translate_to = "";
  if message.content.startswith('!!!'):
    translate_to = "sedelish"
  elif message.content.startswith('!!'):
      translate_to = "english"

  words_list = message.content.replace('!','').split()
  
  if len(words_list) == 0:
    return

  output = ""
  for idx, word in enumerate(words_list):
    if translate_to == "sedelish":
        search_value = es.get(word, "**not found**")

    if translate_to == "english":
        search_value = se.get(word, "**not found**")

    
    if idx == 0:
      output+=search_value
    else:
      output+=" "+search_value

  await message.channel.send(output)  

keep_alive()
client.run(os.getenv('TOKENTEMP'))
bot.run(os.getenv('TOKENTEMP'))