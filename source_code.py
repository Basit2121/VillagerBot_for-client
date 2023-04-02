import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def VillagerBot_help(ctx):
    user = ctx.author
    if ctx.message.content.startswith('/VillagerBot_help'):
        await ctx.send(f"Commands :\n /freegen_eu \n /freegen_na \n /freegen_ap \n /stickgen_eu \n /stickgen_na \n /stickgen_ap \n /stackedgen_eu \n /stackedgen_na \n /stackedgen_ap \n")
        return

@client.command()
async def freegen_eu(ctx):
    user = ctx.author
    if ctx.message.content.startswith('/freegen_eu'):
        # Open the text document
        with open('Available_Accounts_freegen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" + "Free Account\nEurope 🇪🇺 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_freegen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_freegen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_freegen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> freegen_eu"+'\n')

@client.command()
async def freegen_na(ctx):
    user = ctx.author
    if ctx.message.content.startswith('/freegen_na'):
        # Open the text document
        with open('Available_Accounts_freegen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" +"Free Account\nNorth America 🇺🇸 🇨🇦 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_freegen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_freegen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_freegen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> freegen_eu"+'\n')

@client.command()
async def freegen_ap(ctx):
    user = ctx.author
    if ctx.message.content.startswith('/freegen_ap'):
        # Open the text document
        with open('Available_Accounts_freegen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" +"Free Account\nAsia Pacific 🇨🇳 🇯🇵 🇰🇷 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_freegen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_freegen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_freegen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> freegen_ap"+'\n')

@commands.bot_has_guild_permissions(manage_roles=True)
@client.command()
async def stickgen_eu(ctx):
    user = ctx.author

    guild = ctx.guild
    
    # Check if user is a server booster
    if user not in guild.premium_subscribers:
        await ctx.send(f"Sorry {user.mention}, only server boosters can use this command.")
        return
    
    # Open the text document
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        # Get the first line of text
        first_line = f.readline().strip()
    # Send the first line of text to the user via DM
    dm_channel = await user.create_dm()
    await dm_channel.send("-----------------------------------------\n" +"Server Booster Account\nEurope 🇪🇺 " + first_line + "\n-----------------------------------------")
    # Remove the first line from the text document and save it to UsedAccounts.txt
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        lines = f.readlines()
        used_account = lines[0]
    with open('Available_Accounts_stickgen.txt', 'w') as f:
        f.writelines(lines[1:])
    with open('Used_Accounts_stickgen.txt', 'a') as f:
        f.write(user.name + ': ' + used_account + "--> stickgen_eu"+'\n')
    
    
@commands.bot_has_guild_permissions(manage_roles=True)
@client.command()
async def stickgen_na(ctx):
    user = ctx.author

    guild = ctx.guild
    
    # Check if user is a server booster
    if user not in guild.premium_subscribers:
        await ctx.send(f"Sorry {user.mention}, only server boosters can use this command.")
        return
    
    # Open the text document
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        # Get the first line of text
        first_line = f.readline().strip()
    # Send the first line of text to the user via DM
    dm_channel = await user.create_dm()
    await dm_channel.send("-----------------------------------------\n" +"Server Booster Account\nNorth America 🇺🇸 🇨🇦 " + first_line + "\n-----------------------------------------")
    # Remove the first line from the text document and save it to UsedAccounts.txt
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        lines = f.readlines()
        used_account = lines[0]
    with open('Available_Accounts_stickgen.txt', 'w') as f:
        f.writelines(lines[1:])
    with open('Used_Accounts_stickgen.txt', 'a') as f:
        f.write(user.name + ': ' + used_account + "--> stickgen_na"+'\n')

@commands.bot_has_guild_permissions(manage_roles=True)
@client.command()
async def stickgen_ap(ctx):
    user = ctx.author

    guild = ctx.guild
    
    # Check if user is a server booster
    if user not in guild.premium_subscribers:
        await ctx.send(f"Sorry {user.mention}, only server boosters can use this command.")
        return
    
    # Open the text document
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        # Get the first line of text
        first_line = f.readline().strip()
    # Send the first line of text to the user via DM
    dm_channel = await user.create_dm()
    await dm_channel.send("-----------------------------------------\n" +"Server Booster Account\nAsia Pacific 🇨🇳 🇯🇵 🇰🇷 " + first_line + "\n-----------------------------------------")
    # Remove the first line from the text document and save it to UsedAccounts.txt
    with open('Available_Accounts_stickgen.txt', 'r') as f:
        lines = f.readlines()
        used_account = lines[0]
    with open('Available_Accounts_stickgen.txt', 'w') as f:
        f.writelines(lines[1:])
    with open('Used_Accounts_stickgen.txt', 'a') as f:
        f.write(user.name + ': ' + used_account + "--> stickgen_ap"+'\n')

@client.command()
async def stackedgen_eu(ctx):
    user = ctx.author

    with open("PremiumUsers.txt", "r") as f:
        premium_users = [line.strip() for line in f.readlines()]

    if user.name in premium_users:
        # Open the text document
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" +"Premium Account\nEurope 🇪🇺 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_stackedgen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_stackedgen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> stackedgen_eu"+'\n')
    else:
        await user.send("Sorry, you are not a premium user. Please contact the admins")

@client.command()
async def stackedgen_na(ctx):
    user = ctx.author

    with open("PremiumUsers.txt", "r") as f:
        premium_users = [line.strip() for line in f.readlines()]

    if user.name in premium_users:
        # Open the text document
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" +"Premium Account\nNorth America 🇺🇸 🇨🇦 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_stackedgen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_stackedgen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> stackedgen_na"+'\n')
    else:
        await user.send("Sorry, you are not a premium user. Please contact the admins")

@client.command()
async def stackedgen_ap(ctx):
    user = ctx.author

    with open("PremiumUsers.txt", "r") as f:
        premium_users = [line.strip() for line in f.readlines()]

    if user.name in premium_users:
        # Open the text document
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            # Get the first line of text
            first_line = f.readline().strip()
        # Send the first line of text to the user via DM
        dm_channel = await user.create_dm()
        await dm_channel.send("-----------------------------------------\n" +"Premium Account\nAsia Pacific 🇨🇳 🇯🇵 🇰🇷 " + first_line + "\n-----------------------------------------")
        # Remove the first line from the text document and save it to UsedAccounts.txt
        with open('Available_Accounts_stackedgen.txt', 'r') as f:
            lines = f.readlines()
            used_account = lines[0]
        with open('Available_Accounts_stackedgen.txt', 'w') as f:
            f.writelines(lines[1:])
        with open('Used_Accounts_stackedgen.txt', 'a') as f:
            f.write(user.name + ': ' + used_account + "--> stackedgen_ap"+'\n')
    else:
        await user.send("Sorry, you are not a premium user. Please contact the admins")


client.run('MTA5MTM2NDY1OTg3MDgzODgwNA.GJzfJ9.7dss5QxW133ZPHBF65Ndkfy8QJGsSmMxiGRYbU')