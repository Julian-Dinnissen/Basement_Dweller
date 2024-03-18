import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user} im in')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# a fucntion that prints the permissions of a user: 398769543482179585 in guild: 1073971508654899280
@client.event
async def on_ready():

    perms = []
    guild = client.get_guild(1073971508654899280)
    julian = await client.fetch_user(398769543482179585)
    spawn_island = await guild.fetch_channel(1073971512006164492)
    role = discord.utils.get(guild.roles, name="discord mod (fat mofo)")
    gestapo = discord.utils.get(guild.roles, name="Gestapo")

    perms_dict = {}
    
    # give the permissions:
# manage channels, manage server, manages roles, manage webhooks, MANAGE_GUILD_EXPRESSIONS, CREATE_GUILD_EXPRESSIONS, VIEW_AUDIT_LOG, READ_MESSAGE_HISTORY
# test for the 
    permissions = discord.Permissions(
        manage_channels=True,
        manage_guild=True,  # This is the "manage server" permission
        manage_roles=True,
        manage_webhooks=True,
        read_message_history=True,
        kick_members = True,
        mute_members = True,
        deafen_members = True
    )
    permissions.update(manage_messages = True)
    await role.edit(reason = None, permissions=permissions)

    for perm in gestapo.permissions:
        perms_dict[perm[0]] = perm[1]

    print(perms_dict["manage_threads"])

client.run(TOKEN)