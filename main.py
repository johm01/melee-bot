import discord 
import json 
from find_set import *
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

'''
@client.event
async def on_message(message):
    guild_id = message.guild_id
    guild = discord.utils.find(lambda g:g.id==guild_id,client.guilds)
    if message.author.id != bot_id:
        await message.reply(message.created_at)
        pass
'''

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
    msg = get_move(char,move)
    gif = f'./gifs/{char}/{move}.gif'

    await ntx.send(str(msg))
    await ntx.send(file=discord.File(gif))

@client.command()
async def find_set(ntx: str,match: str):
    msg = get_set("SSBM tournament "+match)
    await ntx.send(msg)

def load_moveset(char: str):
    char_data = f'./framedata-json/{char}.json'
    with open(char_data,encoding="utf-8") as f:
        data = json.load(f)
        data = list(data.items())
    
    if data:
        return data
    else:
        return None 

def get_move(data,move: str):
    move_found = None
    
    for i in range(len(data)):
        if data[i][0] == move:
            msg = data[i][1]['totalFrames']
            # Total frames
            print(data[i][1]['totalFrames'])
           
            # A moves properties  
            print(data[i][0])

            # All hit frames for a move 
            for i in data[i][1]['hitFrames']:
                print(i['start'])
                print(i['end'])
        else:
            move_found = False

    return msg
         
move_set = load_moveset('Fox')
print(get_move(move_set,'dair'))
client.run(token)
