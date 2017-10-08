from globalvars import *

async def get_help(args,message):

  help_msg = '''
   > `help`: get a PM of this page
   > more to come
   '''

  try:
    await say(message.author, help_msg)

    await say(message.channel, '{}, please check your DMs.'.format(message.author.mention))

  except:
    await say(message.channel, help_msg)
