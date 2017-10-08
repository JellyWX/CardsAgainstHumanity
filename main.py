import os
import sys
import time
import discord

from event_loop import event_loop
from get_help import get_help

from globalvars import *
from command import Command

@client.event
async def on_ready():
  print('Logged in as ' + client.user.name)
  print('ID: ' + client.user.id)

  await client.change_presence(game=discord.Game(name='cards against humanity'))

async def arg_test(args,message):
  await say(message.channel, 'Args {}'.format(args))

commands = [
  Command('help',[], get_help),
  Command('argtest',[('first',bool),('second',str),('third',int)],arg_test)
]


@client.event
async def on_message(message):
  if message.author == client.user or message.content in [None, False, '']:
    return

  prefix = '/'

  if not message.content[0] == prefix:
    return

  text = ''.join(list(message.content)[len(prefix):]) # removes the prefix from the message

  cmd = text.split(' ')[0]
  args = text.split(' ')[1:]

  for c in commands:
    if cmd == c.name: # if the keyword is the command
      if len(args) == len(c.args['names']): # if the correct number of args is sent
        for arg in range(len(args)):
          try:
            c.args['types'][arg](args[arg])

          except:
            await say(message.channel, 'Incorrect type of argument {} provided (should be {})'.format(arg + 1, c.args['types'][arg]))
            return
        ## CORRECT COMMAND AND ARGS DETECTED ##

        await c.function(args,message)

      else:
        await say(message.channel, 'Incorrect number of arguments provided (got {}, should be {})'.format(len(args), len(c.args['names'])))
      return

  else:
    await say(message.channel, 'Sorry, that command couldn\'t be recognised. Try `/help` for help.')

try:
  with open('token','r') as token_f:
    token = token_f.read().strip()

except FileNotFoundError:
  if len(sys.argv) < 2:
    print('Please remember you need to enter a token for the bot as an argument, or create a file called \'token\' and enter your token into it.')
  else:
    token = sys.argv[1]

else:
  try:
    client.loop.create_task(event_loop())
    client.run(token)
  except Exception as E:
    print(E)
    print('Error detected. Restarting in 15 seconds.')
    time.sleep(15)

    os.execl(sys.executable, sys.executable, *sys.argv)
