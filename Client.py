# Discord Bot Version 1.000.001 (Beta)
# Python Version (3.12.1)
# Discord Version (2.3.2)
# Github URL
# Discord Bot Owner (CodeData)
# Discord Bot Development Team (CodeData)

#importing the required libraries
from typing import Optional
import discord
from discord.ext import commands
import os
import time
import platform
from colorama import Back, Fore, Style

# Defining the bot as client and assigning the command prefix and intents as all
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Discord Event: When the bot starts up, it will display various information in the console and change the bot's activity and status.
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="CodeDataDev.Online"), status=discord.Status.do_not_disturb)
    prfx = (Back.BLACK + Fore.GREEN + time.strftime('%H:%M:%S EST', time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(f"{prfx} Logged in as {Fore.YELLOW}{bot.user.name}")
    print(f"{prfx} Bot ID {Fore.YELLOW}{bot.user.id}")
    print(f"{prfx} Discord Version {Fore.YELLOW}{discord.__version__}")
    print(f"{prfx} Python Version {Fore.YELLOW}{platform.python_version()}")
    print(f"{prfx} CodeDataDev {Fore.YELLOW}CodeDataDev is Online")

# Discord Event: When a member joins the discord server, it will send a welcome message in the a channel.
@bot.event
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f"{member.mention} Hello, Welcome to CodeDataDev")

# Discord Event: When a member leaves the discord server, it will send a leave message in the a channel.
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel()
    await channel.send(f"{member.mention} Goodbye, Sorry to see you leave CodeDataDev")

# Discord Command: Shuts down the bot and sends a closed message in the console.
@bot.command() #Add name and desc.
async def shutdown(ctx):
    await ctx.send("Shutting down the bot")
    await bot.close()

# Discord Command: Displays info about a discord member in the channel where the command was used.
@bot.command() #Add name and desc.
async def who(ctx: commands.Context, member: Optional[discord.Member] = None):
    embed = discord.Embed(title="User info", description=f"Here is the user info {member.mention}", color=discord.Color.red())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value=member.id)
    await ctx.send(embed=embed)

@bot.command() #Add name and desc. Also add a code header to explain what this section of code does.
async def userinfo(ctx, member: Optional[discord.Member]):
    member = member or ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(title="User info", description=f"Here is the user info {member.mention}",
                          color=discord.Color.red(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Name", value=f'{member.name}#{member.discriminator}')
    embed.add_field(name="Nickname", value=member.display_name)
    embed.add_field(name="Status", value=member.status)
    created_at = member.created_at.strftime('%a, %d %b %Y, %H:%M:%S') if member.created_at is not None else "N/A"
    joined_at = member.joined_at.strftime('%a, %d %b %Y, %H:%M:%S') if member.joined_at is not None else "N/A"
    embed.add_field(name="Account Created At", value=created_at)
    embed.add_field(name="Account Joined At", value=joined_at)
    embed.add_field(name=f"Roles ({len(roles)})", value="".join([role.mention for role in roles]))
    embed.add_field(name="Top Role", value=member.top_role.mention)
    embed.add_field(name="Messages", value="0")
    embed.add_field(name="Bot?", value=member.bot)
    await ctx.send(embed=embed)

# Discord Command: Displays server info in the channel where the command was used.
@bot.command() #Add name and desc.
async def serverinfo(ctx):
    embed = discord.Embed(title="Server Info", description=f"Here's the server info, {ctx.guild.name}",
                          color=discord.Color.green(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name="Members", value=ctx.guild.member_count)
    embed.add_field(name="Owner", value=ctx.guild.owner.mention)
    embed.add_field(name="Description", value=ctx.guild.description)
    embed.add_field(name="Created At", value=ctx.guild.created_at.strftime('%a, %d %b %Y, %H:%M:%S'))
    await ctx.send(embed=embed)

# Discord Command: Sends a message with a URL to claim the 'Active Developer Badge' in the channel where the command was used.
@bot.command() #Add name and desc.
async def activedevbadge(ctx):
    await ctx.send("Click the link and follow the steps to claim the 'Active Developer Badge'")
    await ctx.send("https://discord.com/developers/active-developer")

# Discord Command: Sends a message with the discord bot's GitHub URL.
@bot.command() #Add name and desc.
async def github(ctx):
    await ctx.send("https://github.com/CodeData1/") #Add github link

# Discord Command: Pings the discord bot and displays its latency in the channel where the command was used.
@bot.command(name="ping", description="It will show ping")
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latency: {bot_latency}ms")

# Discord Command: Sends a "Hello!" message in the channel where the command was used.
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name="Invite", description="Discord Invite Link")
async def invite(ctx):
    await ctx.send('') #Add discord invite link.

# Run the bot with the Discord token
Discord_token = os.getenv("Discord_Token")
async def bot_run(Discord_token):
    bot.run(Discord_token)