import asyncio
from discord import Member, Guild, User
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("der Bot {} ist nun Online!" .format(client.user.id))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("developed by Pyzoh"), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game("Management"), status=discord.Status.online)
        await asyncio.sleep(5)

def is_not_pinned(mess):
    return not mess.pinned

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "!help" in message.content:
        await message.channel.send("**!help**\r\n"
                                    "!help - alle commands")   #...    
    if message.content.startswith('!clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{} Nachrichten gelöscht.'.format(len(deleted)-1))
    if message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.ban
                await message.channel.send(f'Member {member.naem} wurde gebannt!')
            else:
                await message.channel.send(f'Dieser Member existiert nicht!')
    if message.content.startswith('!kick') and message.author.guild_permissions.kick_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await member.kick()
                await message.channel.send(f'Member {member.naem} wurde gekick!')
            else:
                await message.channel.send(f'Dieser Member existiert nicht!')
    if message.content.startswith('!unban') and message.author.guild_permissions.kick_members:
        args = message.content.split(' ')
        if len(args) == 2:
            user: User













    





client.run("OTM4ODU3OTA3MzQ3NDE1MDkw.YfwZkA.lWCECu3tWBSnlr1KrJfObEDfw_0")