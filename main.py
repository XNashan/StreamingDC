import discord

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)


@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "SHARE SOURCE CODE STREAMING DISCORD | LANG PYTHON", url = "https://twitch.tv/zxuanrev"))


client.run("Bot Token Lu", bot=False)