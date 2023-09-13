import discord 
from discord.ext import commands 
import json

#todo-list 
# Get a youtube vid from a given msg 
# Get a role from a given reaction to a message 


token = ''

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True 

client = commands.Bot(command_prefix='?',intents=intents)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1151324588911898634 or 1151331784399798382:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id== guild_id,client.guilds)

        if payload.emoji.name == 'Mario':
            role = discord.utils.get(guild.roles, name='Mario')
        else:
            role = discord.utils.get(guild.roles,name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print('Member Not found')
        else:
            print('Role is not found')

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 1151331784399798382 or 1151324588911898634:
        guildid = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guildid,client.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role != None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,guild.members)
            await member.remove_roles(role)

@client.command()
async def find_move(ntx: str,char: str,move: str):
    msg = get_move(char,move)
    gif = f'./gifs/{char}/{move}.gif'

    try:
        await ntx.send(str(msg))
        await ntx.send(file=discord.File(gif))
    except Exception:
        await ntx.send('Please enter a move')

def get_move(char,move):
    data = f'./framedata-json/{char}.json'
    with open(data,encoding="utf-8") as f:
        d = json.load(f)
        d = list(d.items())

    for i in range(len(d)):
        if d[i][0] == move:

            # Total frames
            print(d[i][1]['totalFrames'])
           
            # A moves properties  
            print(d[i][1])

            # All hit frames for a move 
            for i in d[i][1]['hitFrames']:
                print(i['start'])
                print(i['end'])
           
get_move('Fox','dair')
client.run(token)

