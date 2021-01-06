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

            elif int(job_id) in [3, 4, 5]:
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
    print(web.url)
    WEBHOOK_URL = web.url
    help_id = int(help_id)
    if help_id is None:
        print('Sending0')
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
    print(list(sorted_d.items())[:4])

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
    print(type(member))
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

client.run(TOKEN)