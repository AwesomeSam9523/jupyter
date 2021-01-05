import asyncio
import functools
import itertools
import math
import random
import discord
from async_timeout import timeout
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command('help')

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
    await client.process_commands(message)

@client.command()
async def sam(ctx):
    await ctx.send('Yea AwesomeSam is my Creator... **A True Legend!**')

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(client.latency, 1)))

import random
@client.command(aliases=['bal'], pass_context=True)
async def balance(ctx, p_id = None):
    replies = ['Yo <@{id}>, You\'ve got `{currency} Ð`',
               '<@{id}> You have `{currency} Ð` in your account!',
               'Ah! So... <@{id}> has got `{currency} Ð` in there!']
    if ctx.channel.id == 795906303884525569:
        if p_id is None:
            p_id = ctx.author.id
            await ctx.send(random.choice(replies).format(id=p_id, currency=config_dict.get(p_id)))
        else:
            p_id = str(p_id)
            p_id = p_id.split('!')
            p_id = p_id[1]
            p_id = list(p_id)
            p_id.pop(-1)
            p_id = ''.join(p_id)
            p_id = int(p_id)
            await ctx.send(random.choice(replies).format(id=p_id, currency=config_dict.get(p_id)))

@client.command(aliases = ['g'])
async def gamble(ctx, price : int):
    if ctx.channel.id == 795906303884525569:
        low_bal = ['Oops! <@{id}> You just have {currency} Ð. What were you thinking <:NepSmug:775572252145745920>',
                   '<@{id}> So you wanna gamble more than you have <:WierdChamp:775568297013411840>? Idiot.',
                   '<@{id}> You dont have enough Ðikes <:1391_pepe_joy:775568241904320572><:1391_pepe_joy:775568241904320572>']

        _id = ctx.author.id
        current_bal = config_dict.get(_id)

        if current_bal < price:
            await ctx.send(random.choice(low_bal).format(id=_id, currency=current_bal))
        elif price <= 0:
            await ctx.send('<@{}> Beta <:WierdChamp:775568297013411840>, Tumse na ho payega'.format(_id))
        else:
            win_loss = ['Won', 'Lost']
            take = random.choice(win_loss)
            if take == 'Won':
                await ctx.send('Wohoo! <@{id}> You gambled `{stake} Ð` and have won! 🎉🎉'.format(id=_id, stake=price))
                new_bal = current_bal + price
                dc = {_id:new_bal}
                config_dict.update(dc)
            else:
                await ctx.send('Damn! <@{id}> You just lost `{stake} Ð`. Sad? <:kekw:772091131596374017>'.format(id=_id, stake=price))
                new_bal = current_bal - price
                dc = {_id: new_bal}
                config_dict.update(dc)
        update_book()

def update_book():
    my = open('arcade_bal.txt', 'w')
    my.write(str(config_dict))
    my.close()

@client.command()
async def add(ctx, person_id : int, amt : int):
    print(person_id, amt)
    if ctx.author.id == 771601176155783198:
        current_bal = config_dict.get(person_id)
        print(current_bal)
        new_bal = current_bal + amt
        dc = {person_id: new_bal}
        config_dict.update(dc)
    update_book()

import job_print_bot
@client.command()
async def job(ctx):
    if ctx.channel.id == 795906303884525569:
        job_print_bot.job_list()

import time
@client.command()
async def apply(ctx, job_id = None):
    if ctx.channel.id == 795906303884525569:
        if job_id is None:
            await ctx.send('<@{}> Please type the job id as well.\nExample: `!apply 1`'.format(ctx.author.id))
        else:
            types = ['I don\'t usually have to work on Sundays',
                     'My father is very particular about food',
                     'I\'ll pick you up and we can go to the Thai restaurant',
                     'She answered my letter right away',
                     'I was telling Jim about it the other day',
                     'She advised him to stop taking that medicine',
                     'I bought a pen for your birthday present',
                     'Would you like to go to the library with me?',
                     'it was thundering yesterday when we were in class',
                     'In the end we all felt like we are too much pizza']
            sentence = random.choice(types)
            jumble = sentence.split(' ')
            lenlist = []

            length = len(jumble)
            for i in range(length):
                lenlist.append(i)
            jumbled_list = []
            for k in range(length):
                index = random.choice(lenlist)
                lenlist.remove(index)
                jumbled_list.append((jumble[index]).lower())

            jumbled_sen = ' / '.join(jumbled_list)

            if int(job_id) == 1:
                await ctx.send('<@{}> Unjumble the following sentence in 25 secs:\n`{}`'.format(ctx.author.id, jumbled_sen))

                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                try:
                    msg = await client.wait_for("message", check=check, timeout=25)  # 30 seconds to reply
                    print(msg, sentence)
                    if msg.content.lower() == sentence.lower():
                        await ctx.send('<@{}> And you are absolutely correct! Here are your `20 Ð`'.format(ctx.author.id))
                        curr_bal = config_dict.get(ctx.author.id)
                        new_b = curr_bal + 20
                        mydict = {ctx.author.id:new_b}
                        config_dict.update(mydict)
                        update_book()
                    else:
                        msg = str(msg.content)
                        msg = msg.split(' ')
                        point = 0
                        for l in range(length):
                            try:

                                if msg[l] in jumble:
                                    point += 1
                            except:
                                pass

                        amt = int((point/length)*20)
                        if amt == 20:
                            amt = 19
                        await ctx.send('<@{}> Unfortunately, you aren\'t 100% correct. Still, I give you `{} Ð`.'.format(ctx.author.id, amt))
                        curr_bal = config_dict.get(ctx.author.id)
                        new_b = curr_bal + amt
                        mydict = {ctx.author.id: new_b}
                        config_dict.update(mydict)
                        update_book()
                except asyncio.TimeoutError:
                    await ctx.send("<@{}> Oops! You ran out of time 🕑".format(ctx.author.id))
            elif int(job_id) == 2:
                emoji_list = ['😅','🙂','😛','😞','😠','🤯','🤓','😟','🤥','🥱','😪','😑','🤔','🤨','🧐','😎','🤩','🥳','😤']
                link_dict = {'https://media.discordapp.net/attachments/795906303884525569/796022790393167932/unknown.png':'🤯 😑 🧐 😞 😛 🤓',
                             'https://media.discordapp.net/attachments/795906303884525569/796022997868871710/unknown.png':'😤 😠 🤨 😞 🙂 😎',
                             'https://media.discordapp.net/attachments/795906303884525569/796023227532443648/unknown.png':'🥱 😪 🤥 😞 😠 😤',
                             'https://media.discordapp.net/attachments/795906303884525569/796023386949025812/unknown.png':'🤨 😟 🤔 😅 🤓 😎',
                             'https://media.discordapp.net/attachments/795906303884525569/796023549482631168/unknown.png':'🤩 🤓 🥳 🧐 😅 😟',
                             'https://media.discordapp.net/attachments/795906303884525569/796023762549473280/unknown.png':'🥳 😞 😅 😟 🤥 🙂',
                             'https://media.discordapp.net/attachments/795906303884525569/796023892649050123/unknown.png':'😟 😛 🤓 🧐 😤 😑',
                             'https://media.discordapp.net/attachments/795906303884525569/796024114698649660/unknown.png':'🤥 😎 😑 😠 😟 🥱',
                             'https://media.discordapp.net/attachments/795906303884525569/796024315497152562/unknown.png':'🤩 😑 🧐 😪 😟 🤓',
                             'https://media.discordapp.net/attachments/795906303884525569/796024461845200926/unknown.png':'🧐 🙂 😞 🤔 😪 🤨'
                            }
                link_list = ['https://media.discordapp.net/attachments/795906303884525569/796022790393167932/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796022997868871710/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796023227532443648/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796023386949025812/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796023549482631168/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796023762549473280/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796023892649050123/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796024114698649660/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796024315497152562/unknown.png',
                             'https://media.discordapp.net/attachments/795906303884525569/796024461845200926/unknown.png']

                emojis = random.choice(link_list)
                dictemo = link_dict.get(emojis)

                dictemo = dictemo.split(' ')
                await ctx.send('<@{}> Remember these 6 emojis carefully:'.format(ctx.author.id))
                botmsg = await ctx.send('{}'.format(emojis))
                await asyncio.sleep(6)
                await botmsg.delete()

                await ctx.send('Enter the 6 emojis. You have 120 secs to find them')
                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                try:
                    emo_pt = 0
                    msg = await client.wait_for("message", check=check, timeout=120)
                    msgg = msg
                    msg = msg.content.split()
                    msg2 = msgg.content.split(' ')
                    try:
                        for b in range(6):
                            if msg[b] in dictemo:
                                emo_pt += 1
                    except:
                        pass
                    dikeamt = int((emo_pt/6)*50)
                    if dictemo == msg or dictemo == msg2:
                        await ctx.send('<@{}> Your Score: 6/6 \n**Congratulation! You got extra `10 Ð` for putting them in same order!**\n**You have been credited with `60 Ð`**'.format(ctx.author.id))
                        cur_bal = config_dict.get(ctx.author.id)
                        nbal = cur_bal + 60
                        dictt = {ctx.author.id:nbal}
                        config_dict.update(dictt)
                        update_book()
                    else:
                        await ctx.send('<@{}> Your Score: {}/6 \n**You have been credited with `{} Ð`. Have Fun :)**'.format(ctx.author.id, emo_pt, dikeamt))
                        cur_bal = config_dict.get(ctx.author.id)
                        nbal = cur_bal + dikeamt
                        dictt = {ctx.author.id: nbal}
                        config_dict.update(dictt)
                        update_book()
                except asyncio.TimeoutError:
                    await ctx.send("<@{}> Oops! You ran out of time 🕑".format(ctx.author.id))

            elif int(job_id) in [3, 4, 5]:
                await ctx.send('<@{}> **Coming Soon...**'.format(ctx.author.id))

            else:
                await ctx.send('<@{}> Invalid Option <:WierdChamp:775568297013411840>'.format(ctx.author.id))

import help_bot
@client.command()
async def help(ctx, help_id = None):
    if ctx.channel.id != 795906303884525569:
        await ctx.send('Help Message Arrived in <#795906303884525569>')
    else:
        if help_id is None:
            help_bot.help_list()
        elif int(help_id) == 1:
            help_bot.help_1()
        elif int(help_id) == 2:
            help_bot.help_2()


@client.command()
async def config(ctx):
    if ctx.author.id == 771601176155783198:
        mem = discord.utils.get(ctx.guild.channels, id=795906303884525569)
        print(mem.members)
        dict = {}
        for user in mem.members:
            mydict = {user.id:500}
            dict.update(mydict)
            mydict.clear()
        await ctx.send('Config Done!')
        my = open('arcade_bal.txt', 'w')
        my.write(str(dict))
        my.close()
    else:
        lol = ctx.author.id
        await ctx.send('<@{}> You ain\'t my master!'.format(lol))

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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DIKE Clan become better"))

my = open('arcade_bal.txt', 'r')
data = my.read()
config_dict = eval(data)
config_dict = dict(config_dict)

client.run(TOKEN)