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
                return
        else:
            if message.author.name != 'GameBot':
                await message.delete()

        if message.author.name == 'GameBot':
            mychnl = client.get_channel(795302460272279552)
            try:
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
    if ctx.channel.id in [795906303884525569, 796686187254513665] :
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
async def gamble(ctx, price = None):
    if ctx.channel.id == 795906303884525569:
        if price is None:
            await ctx.send('Use `!gamble <amount>` or `!g <amount>` to gamble')
            return
        low_bal = ['Oops! <@{id}> You just have {currency} Ð. What were you thinking <:NepSmug:775572252145745920>',
                   '<@{id}> So you wanna gamble more than you have <:WierdChamp:775568297013411840>? Idiot.',
                   '<@{id}> You dont have enough Ðikes <:1391_pepe_joy:775568241904320572><:1391_pepe_joy:775568241904320572>']

        _id = ctx.author.id
        current_bal = config_dict.get(_id)
        price = int(price)
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

    jh = open('hacking_data.txt', 'w')
    jh.write(str(items))
    jh.close()

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
    else:
        lol = ctx.author.id
        await ctx.send('<@{}> You ain\'t my master!'.format(lol))

import job_print_bot
@client.command()
async def job(ctx):
    if ctx.channel.id == 795906303884525569:
        job_print_bot.job_list()

import time
@client.command()
async def apply(ctx, job_id = None):
    if ctx.channel.id in [795906303884525569, 796686187254513665]:
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
                time.sleep(0.5)
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

            elif int(job_id) == 4:
                timedout = 796755650155642881
                if timedout in [y.id for y in ctx.author.roles]:
                    await ctx.send('<@{}> You are timed out. Please try again later'.format(ctx.author.id))
                    return
                dict_to_update = items.get(ctx.author.id)
                if dict_to_update.get('comp') == 'False':
                    await ctx.send('<@{}> You don\'t have a 💻 Computer. Go to shop and buy it to start hacking'.format(
                        ctx.author.id))
                    return
                await ctx.send('<@{}> **Basic Rules:-**\n'
                               '1. If you get caught, you lose your computer\n'
                               '2. Type `!use <item-code>` to use your 🧭 Trace Lower (`trace`) or 🖲️ Emergency Escape (`esc`)'.format(ctx.author.id))
                hackvalue = random.randint(1000, 5000)
                await ctx.send('**Estimated Value Gain: {}**\n'
                               'Type `y` to start or `n` to cancel. You will be able to apply after 2 hrs if cancelled'.format(
                    hackvalue))

                def check2(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                myguild = client.get_guild(766875360126042113)
                msg = await client.wait_for("message", check=check2, timeout=30)
                try:
                    if msg.content.lower() == 'n':
                        await ctx.send('<@{}> You cancelled the job. You will be eligible in **2 hours and 0 minutes**'.format(ctx.author.id))
                        role = discord.utils.get(myguild.roles, id=timedout)
                        await ctx.author.add_roles(role)
                        await asyncio.sleep(2*60*60)
                        await ctx.author.remove_roles(role)

                    elif msg.content.lower() == 'y':
                        await ctx.send('Gamester Nob')
                    else:
                        await ctx.send('<@{}> Invalid Response. Assuming it to be `n`. You will be eligible in **2 hours and 0 minutes**'.format(ctx.author.id))
                except:
                    await ctx.send('Response Timed Out. You will be eligible in **2 hours and 0 minutes** to apply again')

            elif int(job_id) in [3, 5]:
                await ctx.send('<@{}> **Coming Soon...**'.format(ctx.author.id))

            else:
                await ctx.send('<@{}> Invalid Option <:WierdChamp:775568297013411840>'.format(ctx.author.id))

from aiohttp import ClientSession
from discord_webhook import DiscordWebhook, DiscordEmbed
#import help_bot
@client.command()
async def help(ctx, help_id = None):
    ava = await client.fetch_user(795334771718226010)
    avaurl = ava.avatar_url
    web = await ctx.channel.create_webhook(name='DIKE Official')
    WEBHOOK_URL = web.url
    help_id = int(help_id)
    if help_id is None:
        clog = '`1` --> `Apply to DIKE`\n\n' \
               '`2` --> `Arcade Commands`\n\n' \
               '`3` --> `Moderator Commands`\n\n\n' \
               '**Type `!help <number>` to get info**'

        embed = DiscordEmbed(title='DIKE Official Bot Help:',
                             description=clog,
                             color=16776704)
        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(title='DIKE Official Bot Help:',
                                 description=clog,
                                 color=16776704)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await webhook.send(embed= embed, username='DIKE Official', avatar_url=avaurl)
    elif help_id == 1:
        clog = 'Here are the minimum requirements:\n' \
               '```python\n' \
               '"--> Level:  30"\n' \
               '"--> KDR:   1.5"\n' \
               '"--> SPK:   100"\n' \
               '"--> KPG:    10"\n' \
               '"--> Nukes:   5"```\n\n' \
               'Type **g.apply <your-ign>** in <#795293822224695297> to apply.'
        embed = DiscordEmbed(title='DIKE Official Bot Help:',
                             description=clog,
                             color=16776704)
        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(title='DIKE Official Bot Help:',
                                  description=clog,
                                  color=16776704)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await webhook.send(embed=embed, username='DIKE Official', avatar_url=avaurl)
    elif help_id == 2:
        clog = 'Here are all the Arcade Commands!\n' \
               '```python\n' \
               '"--> !balance/!bal - View Balance"\n' \
               '"--> !gamble/!g    - Gamble to gain (or lose?) 50-50 Chances"\n' \
               '"--> !job          - Take up small tasks to gain Dikers!"\n' \
               '"--> !apply        - Apply for a particular job"\n' \
               '"--> !wipe         - Resets your Account (Non-reversible!)"\n' \
               '"--> !help         - View help"```'
        embed = DiscordEmbed(title='DIKE Official Bot Help:',
                             description=clog,
                             color=16776704)
        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(title='DIKE Official Bot Help:',
                                  description=clog,
                                  color=16776704)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await webhook.send(embed=embed, username='DIKE Official', avatar_url=avaurl)
    elif help_id == 3:
        clog = 'Here are all the Moderator Commands!\n' \
               '```python\n' \
               '"--> !slowmode/!sm      - Puts the channel in slowmode"\n' \
               '"--> !mute              - Mute the user"\n' \
               '"--> !unmute            - Unmutes the user"\n' \
               '"--> !warn              - Warns the user' \
               '```'
        embed = DiscordEmbed(title='DIKE Official Bot Help:',
                             description=clog,
                             color=16776704)
        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(title='DIKE Official Bot Help:',
                                  description=clog,
                                  color=16776704)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await webhook.send(embed=embed, username='DIKE Official', avatar_url=avaurl)

import operator
@client.command()
async def rich(ctx):
    sorted_d = dict(sorted(config_dict.items(), key=operator.itemgetter(1), reverse=True))
    mylist = list(sorted_d.items())[:5]
    embed = discord.Embed(title="Riches of the Rich", description="", color=16776704)
    for char in mylist:
        userid = char[0]
        amt = char[1]
        myguild = client.get_guild(766875360126042113)
        a = myguild.get_member(userid)
        dname = a.display_name
        embed.add_field(name=dname, value='`'+ str(amt) + ' Ð `', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def shop(ctx, shop_page : int = None):
    if shop_page is None:
        shoplist = '|   __Generals__   |    Hacker    |     Wars     | Bank Robbery |\n'
        desc = '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=16776704)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 1:
        shoplist = '|   __Generals__   |    Hacker    |     Wars     | Bank Robbery |\n'
        desc =     '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=16776704)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 2:
        shoplist = '|   Generals   |    __Hacker__    |     Wars     | Bank Robbery |\n'
        embed = discord.Embed(title=shoplist, description='Buy useful stuff here to help you in a tricky hacking situation', color=16776704)
        embed.add_field(name='💻 Computer', value='Essential to start Hacking\nItem Code: `comp`\nPrice: `5000 Ð`\n', inline=False)
        embed.add_field(name='🖥️ Assistant PC', value='Lowers the hacking time significantly\nItem Code: `pc`\nPrice: `4500 Ð`\n',inline=False)
        embed.add_field(name='🖲️ Emergency Escape', value='Aborts the process and protects you from Police\nItem Code: `esc`\nPrice: `3000 Ð`\n', inline=False)
        embed.add_field(name='⌨️ QuickBoard™', value='Your commands are taken noticeably faster\nItem Code: `qboard`\nPrice: `2000 Ð`\n', inline=False)
        embed.add_field(name='🧭 Trace Lower', value='Lowers your trace percentage by 10%\nItem Code: `trace`\nPrice: `1000 Ð`\n', inline=False)
        embed.add_field(name='🛰️ VPN', value='Slows the Cyber Police to track you\nItem Code: `vpn`\nPrice: `500 Ð`\n', inline=False)
        embed.add_field(name='\n\nType !buy <item-code> to purchase the item', value='Have Fun Hacking 😉', inline=False)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 3:
        shoplist = '|   Generals   |    Hacker    |     __Wars__     | Bank Robbery |\n'
        desc =     '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=16776704)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 4:
        shoplist = '|   Generals   |    Hacker    |     Wars     | __Bank Robbery__ |\n'
        desc =     '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=16776704)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)

@client.command()
async def give(ctx, give_to : discord.Member = None, amount: int = None):
    if amount <= 0:
        await ctx.send('<@{}> Seriosuly?'.format(ctx.author.id))
    if give_to is None or amount is None:
        await ctx.send('Format for !give command is: `!give <person> <amount>`')
        return
    if give_to == ctx.author:
        await ctx.send('<@{}> Sending Dikers to yourself, huh?'.format(ctx.author.id))
    else:
        print(give_to.id)
        final_amount = int(amount*0.9)
        cur_bal = config_dict.get(ctx.author.id)
        if int(cur_bal) < amount:
            await ctx.send('<@{}> You dont have that much yourself <:kekw:772091131596374017>'.format(ctx.author.id))
        else:
            await ctx.send('<@{}> sent `{} Ð` to <@{}>. What a nice gesture 😀\nTax: `{} Ð`'.format(ctx.author.id, final_amount, give_to.id, amount-final_amount))
            togiverbal = config_dict.get(give_to.id)
            newuserbal = cur_bal - amount
            giverbal = togiverbal + final_amount
            mynewdict = {ctx.author.id:newuserbal, give_to.id:giverbal}
            config_dict.update(mynewdict)
            update_book()

@client.command(aliases=['inv'])
async def inventory(ctx):
    list_of_items = [
    ['laptop' , items.get(ctx.author.id).get('comp')],
    ['pc' , items.get(ctx.author.id).get('pc')],
    ['qboard' , items.get(ctx.author.id).get('qboard')],
    ['vpn' , items.get(ctx.author.id).get('vpn')],
    ['escape' , items.get(ctx.author.id).get('esc')],
    ['tracel' , items.get(ctx.author.id).get('trace')]
                    ]

    print_list = ''
    for char in range(len(list_of_items)):
        for char2 in range(1, len(list_of_items[char])):
            try:
                if list_of_items[char][1] == 'True':
                    print_list = print_list + list_of_items[char][0] + '\n\n'
                elif int(list_of_items[char][1]) > 0:
                    print_list = print_list + list_of_items[char][0] + '\nQty: `' + str(list_of_items[char][1]) + '`\n\n'
                else:
                    pass
            except:
                pass
    print(print_list)

    print_list_format = print_list.split('\n')
    print(print_list_format)

    for b in range(len(print_list_format)):
        if print_list_format[b] == 'laptop':
            print_list_format.pop(b)
            print_list_format.insert(b, '💻 Computer')
        elif print_list_format[b] == 'qboard':
            print_list_format.pop(b)
            print_list_format.insert(b, '⌨️ QuickBoard™')
        elif print_list_format[b] == 'escape':
            print_list_format.pop(b)
            print_list_format.insert(b, '🖲️ Emergency Escape')
        elif print_list_format[b] == 'tracel':
            print_list_format.pop(b)
            print_list_format.insert(b, '🧭 Trace Lower')
        elif print_list_format[b] == 'vpn':
            print_list_format.pop(b)
            print_list_format.insert(b, '🛰️ VPN')
        elif print_list_format[b] == 'pc':
            print_list_format.pop(b)
            print_list_format.insert(b, '🖥️ Assistant PC')
            
    print(print_list_format)
    final_list = '\n'.join(print_list_format)
    if final_list != '':
        await ctx.send('<@' + str(ctx.author.id) + '> **Here is your inventory:**\n\n'+ final_list)
    else:
        await ctx.send('<@' + str(ctx.author.id) + '> **You dont own anything 😂😂**\n\n'+ final_list)


@client.command()
async def buy(ctx, code:str = None):
    if code is None:
        await ctx.send('Format for !buy: `!buy <item-code>`')
        return
    if code == 'comp':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 5000:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            if dict_to_update.get('comp') == 'True':
                await ctx.send('<@{}> You already own it!'.format(ctx.author.id))
                return
            newdict = {'comp':'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 5000
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> 💻 Computer purchased successfully!'.format(ctx.author.id))
    elif code == 'pc':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 4500:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            if dict_to_update.get('pc') == 'True':
                await ctx.send('<@{}> You already own it!'.format(ctx.author.id))
                return
            newdict = {'pc':'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 4500
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> 🖥️ Assistant PC purchased successfully!'.format(ctx.author.id))
    elif code == 'esc':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 3000:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            before = dict_to_update.get('esc')
            newdict = {'esc':before+1}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 3000
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> 🖲️ Emergency Escape purchased successfully!'.format(ctx.author.id))
    if code == 'trace':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 1000:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            before = dict_to_update.get('trace')
            newdict = {'trace':before+1}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 1000
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> 🧭 Trace Lower purchased successfully!'.format(ctx.author.id))
    if code == 'vpn':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 500:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            if dict_to_update.get('vpn') == 'True':
                await ctx.send('<@{}> You already own it!'.format(ctx.author.id))
                return
            newdict = {'vpn':'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 500
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> 🛰️ VPN purchased successfully!'.format(ctx.author.id))
    if code == 'qboard':
        cur_bal = config_dict.get(ctx.author.id)
        cur_bal = int(cur_bal)
        if cur_bal < 2000:
            await ctx.send('<@{}> You dont have enought Dikers to purchase this item'.format(ctx.author.id))
        else:
            dict_to_update = items.get(ctx.author.id)
            if dict_to_update.get('qboard') == 'True':
                await ctx.send('<@{}> You already own it!'.format(ctx.author.id))
                return
            newdict = {'qboard':'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 2000
            dictbal = {ctx.author.id:newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> ⌨️ QuickBoard™ purchased successfully!'.format(ctx.author.id))


@client.command(aliases=['reset'])
async def wipe(ctx):
    id = ctx.author.id
    dicty = {id:500}
    config_dict.update(dicty)
    update_book()

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

owner = 769543339627249714
mod = 773629756570599454
admin = 781377928898412564
@client.command(aliases=['sm'])
async def slowmode(ctx, seconds: int):
    if owner in [y.id for y in ctx.author.roles] or mod in [y.id for y in ctx.author.roles] or admin in [y.id for y in ctx.author.roles]:
        await ctx.channel.edit(slowmode_delay=seconds)
        if seconds == 0:
            await ctx.send(
                "<#{}> is no longer in slowmode.".format(ctx.channel.id))
        elif seconds<0:
            pass
        else:
            await ctx.send("<#{}> is in `s l o w m o d e`.\nUsers will be able to post every {} seconds!".format(ctx.channel.id, seconds))

@client.command()
async def warn(ctx, user : discord.Member, reason = None):
    warnings = {'war1':796249188832509953,
    'war2':796249230774763540,
    'war3':796249281295024178,
    'war4':796249305391562782,
    'war5':796249325877461033,
    'war6':796249348991614976,
    'war7':796249379110649856,
    'war8':796249402527711303,
    'war9':796249425965350913,
    'war10':796249447255900171,
    'war11':796249469041508393}

    if owner in [y.id for y in ctx.author.roles] or mod in [y.id for y in ctx.author.roles] or admin in [y.id for y in ctx.author.roles]:
        if user is None or reason is None:
            await ctx.send('<@{}>. The syntax for warn is: `!warn <user> <reason>`'.format(ctx.author.id))
        else:
            await user.send('**You have been Warned in `✔ Official DIKE Clan` for:** {}'.format(reason))
            await ctx.message.delete()
            await ctx.send('☑️ User Warned Successfully')

            user_role_ids = [int(y.id) for y in user.roles]
            if warnings.get('war1') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war2')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war1')))
            elif warnings.get('war2') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war3')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war2')))
            elif warnings.get('war3') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war4')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war3')))
            elif warnings.get('war4') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war5')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war4')))
            elif warnings.get('war5') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war6')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war5')))
            elif warnings.get('war6') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war7')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war6')))
            elif warnings.get('war7') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war8')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war7')))
            elif warnings.get('war8') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war9')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war8')))
            elif warnings.get('war9') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war10')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war9')))
            elif warnings.get('war10') in user_role_ids:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war11')))
                await user.remove_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war10')))
            else:
                await user.add_roles(discord.utils.get(ctx.guild.roles, id=warnings.get('war1')))

@client.command()
async def mute(ctx, member: discord.Member, mtime = None):
    mutes = {'m1': 796249529883033611,
             'm2': 796249570689810432,
             'm3': 796249592991318026,
             'm4': 796249619897385000,
             'm5': 796249643273027655,
             'm6': 796249664722305035,
             'm7': 796249688025202718,
             'm8': 796249708782813215,
             'm9': 796249736188788796,
             'm10': 796249760969130024,
             'm11': 796249781013970975}
    if owner in [y.id for y in ctx.author.roles] or mod in [y.id for y in ctx.author.roles] or admin in [y.id for y in ctx.author.roles]:
        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
        if mtime is None:
            await member.add_roles(muted_role)
            await ctx.send('☑️ User Muted Successfully')
        else:
            time_convert = {"s":1, "m":60, "h":3600,"d":86400}
            tempmute= int(mtime[:-1]) * time_convert[mtime[-1]]
            print('time:', tempmute)
            await ctx.message.delete()
            await member.add_roles(muted_role)
            await ctx.send('☑️ User Muted Successfully')
            await asyncio.sleep(tempmute)
            await member.remove_roles(muted_role)

        user_role_ids = [int(y.id) for y in member.roles]
        if mutes.get('m1') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m2')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m1')))
        elif mutes.get('m2') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m3')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m2')))
        elif mutes.get('m3') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m4')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m3')))
        elif mutes.get('m4') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m5')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m4')))
        elif mutes.get('m5') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m6')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m5')))
        elif mutes.get('m6') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m7')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m6')))
        elif mutes.get('m7') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m8')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m7')))
        elif mutes.get('m8') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m9')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m8')))
        elif mutes.get('m9') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m10')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m9')))
        elif mutes.get('m10') in user_role_ids:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m11')))
            await member.remove_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m10')))
        else:
            await member.add_roles(discord.utils.get(ctx.guild.roles, id=mutes.get('m1')))

@client.command()
async def unmute(ctx, member : discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    await ctx.send('☑️ User Unmuted Successfully')

@client.command()
async def setuphack(ctx):
    if ctx.author.id == 771601176155783198:
        mem = discord.utils.get(ctx.guild.channels, id=795906303884525569)
        print(mem.members)
        dicti = {}
        for user in mem.members:
            mydict = {user.id:{'comp':'False', 'pc':'False', 'vpn':'False', 'esc':0, 'qboard':'False', 'trace':0}}
            dicti.update(mydict)
            mydict.clear()
        await ctx.send('Hacking Config Done!')
        myf = open('hacking_data.txt', 'w')
        myf.write(str(dicti))
        myf.close()
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
    role1 = discord.utils.get(member.guild.roles, id = 795570028585287690)
    role2 = discord.utils.get(member.guild.roles, id = 795567863003480064)
    role3 = discord.utils.get(member.guild.roles, id = 795572264283799582)
    role4 = discord.utils.get(member.guild.roles, id = 796248941620494346)
    memrole = discord.utils.get(member.guild.roles, id = 775363088719413278)
    await member.add_roles(role1)
    await member.add_roles(role2)
    await member.add_roles(role3)
    await member.add_roles(role4)
    await member.add_roles(memrole)
    myy = {member.id:500}
    config_dict.update(myy)
    update_book()


@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DIKE Clan become better"))

my = open('arcade_bal.txt', 'r')
data = my.read()
config_dict = eval(data)
config_dict = dict(config_dict)

my2 = open('hacking_data.txt', 'r')
data2 = my2.read()
items = eval(data2)
items = dict(items)

client.run(TOKEN)