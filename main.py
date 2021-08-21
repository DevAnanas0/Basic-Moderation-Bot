import discord
from discord.ext import commands


# setup commands

Token = ""
presence = "Ananas#1226"
Prefix = ""
#########################

Embed = discord.Embed

client = commands.Bot(command_prefix=Prefix, intents=discord.Intents.all()) 

@client.event
async def on_ready():
    print("Name: " +client.user.name)
    print("ID: " +client.user.id)
    print("Token: " + Token)
    print("Presence: " +presence)
    print("Prefix: " +Prefix)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence))

@client.command()
async def kick(ctx, member:discord.Member, reason="Not Given"):
    await member.kick(reason=reason)
    emb = Embed(title="Kick")
    emb.add_field(name=f"Who", value=f"{member.mention}")
    emb.add_field(name=f"Mod", value=f"{ctx.author.mention}")
    emb.add_field(name=f"Reason", value=f"{reason}")
    await ctx.send(embed=emb)

@client.command()
async def ban(ctx, member:discord.Member, reason="Not Given"):
    await member.ban(reason)
    emb = Embed(title="Ban")
    emb.add_field(name=f"Who", value=f"{member.mention}")
    emb.add_field(name=f"Mod", value=f"{ctx.author.mention}")
    emb.add_field(name=f"Reason", value=f"{reason}")
    await ctx.send(embed=emb)

client.run(Token)