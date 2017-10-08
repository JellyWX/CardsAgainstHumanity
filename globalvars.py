import discord

client = discord.Client()


async def say(channel,message):
  await client.send_message(channel, embed=discord.Embed(description=message))
