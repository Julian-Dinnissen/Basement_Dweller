import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.guild != client.get_guild(1065705816105160704):
        return

    await check_role(message)
    
    if message.content.startswith('save'):
        perms = await save_perms(message.author.roles[0])
        await save_json(perms, message)

    if message.content.startswith('update'):
        perms = await save_perms(message.author.roles[0])
        await save_json(perms, message)

    # del json file
    if message.content.startswith('del') and message.author.id == 398769543482179585:
        os.remove(f'{message.author.name}.json')

# a fucntion that prints the permissions of a user: 398769543482179585 in guild: 1073971508654899280
@client.event
async def on_ready():
    print(f'{client.user} im in')

    perms = []
    #guild = client.get_guild(1073971508654899280)
    julian = await client.fetch_user(398769543482179585)
    #spawn_island = await guild.fetch_channel(1073971512006164492)
    #role = discord.utils.get(guild.roles, name="discord mod (fat mofo)")
    #gestapo = discord.utils.get(guild.roles, name="Gestapo")

    # permissions = discord.Permissions(
    #     manage_channels=True,
    #     manage_guild=True,  # This is the "manage server" permission
    #     manage_roles=True,
    #     manage_webhooks=True,
    #     read_message_history=True,
    #     kick_members = True,
    #     mute_members = True,
    #     deafen_members = True,
        
    # )
    # permissions.update(manage_messages = True)
    # await role.edit(reason = None, permissions=permissions)


async def check_role(message):
    role = discord.utils.get(message.guild.roles, name="Gestapo")
    if role in message.author.roles:
        print(f"{message.author} has the role {role.name}")
    else:
        print(f"{message.author} does not have the role {role.name}")

    roles = [role for role in message.guild.roles if not role.managed]
    for role in roles:
        print(role.name)

async def save_perms(role):
    dict1 = {}
    for perm in role.permissions:
        dict1[perm[0]] = perm[1]
    return dict1
    

# async def print_audit_log(message):
#     async for entry in message.guild.audit_logs(limit=10):
#         print(entry)

#save perms dictionary as a json file
async def save_json(dict, message):
    with open(f'{message.author.name}.json', 'w') as json_file:
        json.dump(dict, json_file)

client.run(TOKEN)