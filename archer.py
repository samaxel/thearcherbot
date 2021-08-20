import discord
from discord.ext import commands

Client = discord.client
client = commands.Bot(command_prefix = '<')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
 print("Bot is on!")

client.run("ODc4MDk5NTcyNTY2NjcxNDQw.YR8P9A.5UX7uYP9aWlvFjIynnckViWctso")
