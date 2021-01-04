import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    global sendbot
    if message.channel.id == 795293822224695297:
        if message.author == client.user:
            print('returned')
            return

        if message.content.startswith('g.apply'):
            actualid = message.author.id
            sendbot = True
            mychnl = client.get_channel(795302460272279552)
            userid = message.author.name
            actualid = message.author.id
            if userid != 'GameBot':
                await mychnl.send('@here\nSent by: {}'.format(message.author.mention))
                await message.channel.send('<@{}> Request recieved!'.format(actualid))

            if message.author == client.user:
                print('returned')
                return
        else:
            if message.author.name != 'GameBot':
                await message.delete()

        if message.author.name == 'GameBot':
            mychnl = client.get_channel(795302460272279552)
            try:
                print('tryna send')
                print(message.id)
                await mychnl.send(message.attachments[0].url)
            except IndexError:
                pass
        await message.delete()
    if message.channel.id == 795302460272279552:
        if message.content.startswith('@here') or message.author.id != 795334771718226010:
            pass
        else:
            thup = '\N{THUMBS UP SIGN}'
            thdown = '\N{THUMBS DOWN SIGN}'
            await message.add_reaction(emoji=thup)
            await message.add_reaction(emoji=thdown)
    if message.content.startswith('!sam'):
        await message.channel.send('Yea AwesomeSam is my Creator... **A True Legend!**')

@client.event
async def on_member_join(member):
    welcom_chl = client.get_channel(773401123389440011)
    welmsg = '<a:hello:786862994381471766> Hyy <@{user}> Welcome to Official DIKE Clan <a:hello:786862994381471766>\n' \
             '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
             '<a:ARR:786863234736455680> MUST READ AND FOLLOW <#773626644324810762>  <a:ARR:786863090670239744>\n' \
             '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
             '<a:ARR:786863234736455680> CHECK <#773404953377112104> TO KNOW HOW TO GET ROLES <a:ARR:786863090670239744>\n' \
             '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
             '<a:ARR:786863234736455680> MUST BE UPDATED AND READ DAILY <#773876008725905420> <a:ARR:786863090670239744>\n' \
             '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
             '<a:ARR:786863234736455680> MUST BE ACTIVE IN CHAT <#766875360595410946>  AND UNLOCK LEVEL AND ROLES <a:blueflame:786863090670239744>\n' \
             '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
             '<a:yldz:786863153454645269> <:line:786867516253274134> <:line:786867516253274134> HOPE YOU WILL ENJOY <:line:786867516253274134> <:line:786867516253274134> <a:yldz:786863153454645269>'.format(user=member.id)
    await welcom_chl.send(welmsg)


@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DIKE Clan Applications"))

client.run(TOKEN)