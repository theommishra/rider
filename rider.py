import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

client = discord.Client()
@client.event
async def on_ready():
    print("Tyaiyar hai")

@client.event
async def on_message(message):
    if message.content.startswith('add'):
        channel = message.channel
        await channel.send('You were registered to Event')
        user = message.author
        roleVer = 'EVENT PARTICIPANTS'
        role = roleVer
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))


client.run("NzM1MTg3NTMwMTYwNDA2NjU4.XxcsZw.5own1S9zEvSWUo4aWlPuThub7Wo")
