import discord 
import json 
from find_set import *
from get_frames import * 
from discord.ext import commands 

#todo-list 

role_emojis = ['Shiek','Mewtwo','Yoshi','Kirby','Game & Watch','Bowser','Ganondorf','Peach','Marth','Roy','Ice Climbers','DK'
            ,'Mario','Luigi','Ness','Link','Young Link','Dr.Mario','Falco','Fox','Captain Falcon','Zelda','Samus','Jigglypuff','Pikachu','Pichu']

with open('tokens.json') as d:
    data = json.load(d)

token = data['disc-token'] 

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True 

client = commands.Bot(command_prefix='?',intents=intents)

# Bot id
bot_id = '1150638542062637086'

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1151324588911898634 or 1151331784399798382:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id== guild_id,client.guilds)

        if payload.emoji.name in role_emojis:
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
    try:
        gif = f'./gifs/{char}/{move}.gif'
        await ntx.send(file=discord.File(gif))
    except:
        await ntx.send('Move not found try putting the entire move into one word like this utilt/usmash')

@client.command()
async def how_to_use(ntx: str):
    await ntx.send("To find a set type by two players like ?find_set ZainVsMango To find a moves data type it as ?find_move dtilt")

@client.command()
async def find_set(ntx: str,match: str):
    msg = get_set('melee '+match)
    await ntx.sennd(msg)

client.run(token)
