import ast
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import re

intents = discord.Intents.default()
intents.members = True

embedcolor = 3407822
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

print('Starting...')

from discord.ext import tasks
import requests
import shutil
from datetime import date
import random


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    guildid = message.guild.id
    channel = message.channel.id
    guild = msgs_data.get(guildid)

    if guild is None:
        g_add = {guildid: {}}
        msgs_data.update(g_add)
        guild = msgs_data.get(guildid)

    chl = guild.get(channel)

    today = date.today()
    d = today.strftime('%d-%m-%Y')
    if chl is None:
        chl_add = {channel: {d: 0}}
        guild.update(chl_add)
        g_upd = {guildid: guild}
        msgs_data.update(g_upd)

        chl = guild.get(channel)

    today_count = chl.get(d)
    if today_count is None:
        date_add = {d: 1}
        chl.update(date_add)
        chla = {channel: chl}
        guild.update(chla)
        g_upd = {guildid: guild}
        msgs_data.update(g_upd)
        today_count = chl.get(d)

    pre_upd = msgs_data.get(guildid)
    dic = {d: today_count + 1}
    chl.update(dic)
    upd = {guildid: pre_upd}
    msgs_data.update(upd)

    temp_dict = msgs_data
    file = open('messages.txt', 'w')
    file.write(str(temp_dict))
    file.close()

    if message.author == bot.user:
        return

    global sendbot
    mentionlist = [
        'Yes I am alive! Say?',
        'Let me live, please!',
        'Bruh what is it now?',
        'Whoa I am here man, what now?',
        'Stop pinging me unnecessarily!'
    ]
    devlist = [
        'Yes master?',
        'I am here master!',
        'Yes Sir!?',
        'Present Sir!',
        'What can I do for you sir?'
    ]
    mention = '<@!{}>'.format(bot.user.id)
    if mention in message.content:
        if message.author.id != 771601176155783198:
            await message.reply(random.choice(mentionlist))
        else:
            await message.reply(random.choice(devlist))
    if message.guild.id == 766875360126042113:
        if message.channel.id == 795293822224695297:
            if message.content.startswith('g.apply'):
                actualid = message.author.id
                sendbot = True
                mychnl = bot.get_channel(795302460272279552)
                userid = message.author.name
                actualid = message.author.id
                if userid != 'GameBot':
                    time.sleep(5)
                    await message.channel.send('<@{}> Request recieved!'.format(actualid))
                    time.sleep(15)
                    await mychnl.send(
                        '@here\n**Sent by:** {}\n**Orignal Message by user:** {}'.format(message.author.mention,
                                                                                         message.content))

                if message.author == bot.user:
                    return
            else:
                if message.author.name != 'GameBot':
                    await message.delete()

            if message.author.name == 'GameBot':
                mychnl = bot.get_channel(795302460272279552)
                try:
                    image_url = message.attachments[0].url
                    filename = 'profile.png'
                    r = requests.get(image_url, stream=True)

                    if r.status_code == 200:
                        r.raw.decode_content = True
                        with open(filename, 'wb') as f:
                            shutil.copyfileobj(r.raw, f)

                    file = discord.File("profile.png", filename="profile.png")
                    msg = await mychnl.send(file=file)
                except:
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
        if message.channel.id == 798091588676747285:
            if message.author.id == 795334771718226010:
                thup = '\N{THUMBS UP SIGN}'
                thdown = '\N{THUMBS DOWN SIGN}'
                await message.add_reaction(emoji=thup)
                await message.add_reaction(emoji=thdown)

        myguild = bot.get_guild(766875360126042113)
        novice = discord.utils.get(myguild.roles, id=798215857096491068)
        active = discord.utils.get(myguild.roles, id=798215989450768394)
        devoted = discord.utils.get(myguild.roles, id=798216133605720114)
        legendary = discord.utils.get(myguild.roles, id=798216189167271986)
        nolife = discord.utils.get(myguild.roles, id=798216359057424394)

        if message.channel.id == 798225149019029524:
            msg = str(message.content)
            msg = msg.split(' ')
            _id = int(msg[0])
            level = int(msg[1])
            member_to_give = myguild.get_member(_id)
            print('id: {}, level: {}'.format(id, level))

            if level < 5:
                pass
            elif level < 10 and level >= 5:
                await member_to_give.add_roles(novice)
            elif level < 15 and level >= 10:
                await member_to_give.add_roles(active)
            elif level < 20 and level >= 15:
                await member_to_give.add_roles(devoted)
            elif level < 25 and level >= 20:
                await member_to_give.add_roles(legendary)
            elif level >= 25:
                await member_to_give.add_roles(nolife)

        guildid = message.guild.id
        links_file = links_data.get(guildid)
        if links_file is None:
            pass
        else:
            allowed_links = links_file.get('allowed')
            send_links = links_file.get('actual')

            if message.channel.id not in allowed_links:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                  message.content.lower())
                if owner in [y.id for y in message.author.roles] or mod in [y.id for y in message.author.roles]:
                    pass
                elif urls:
                    await message.delete()
                    await message.channel.send('<@{}> Links not allowed in this channel!\n'
                                               'Use <#{}> to send links.'.format(message.author.id, send_links))
    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    msg = message.content
    ghost_ping = re.findall('<@!(?<!\d)\d{18}(?!\d)>+', msg)
    id_finder = re.findall('(?<!\d)\d{18}(?!\d)+', msg)

    try:
        mem = bot.fetch_user(id_finder[0])
    except IndexError:
        return
    if mem is not None and int(id_finder[0]) != message.author.id:
        embed = discord.Embed(title='🚨 Oops!',
                              description='<@!{}> just ghost pinged {}!'.format(message.author.id, ghost_ping[0]),
                              color=16724787)
        await message.channel.send(embed=embed)


@bot.command()
async def changelogs(ctx):
    if ctx.author.id != 771601176155783198:
        return
    embed = discord.Embed(title='DIKE Bot v1.0.0')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{} ms`'.format(int(bot.latency * 1000)))


from matplotlib.patches import Rectangle


@bot.command()
async def stats(ctx, channel: str = None):
    embed = discord.Embed(description='<a:loading:807883748791156737>  Loading...', color=embedcolor)
    loading = await ctx.send(embed=embed)

    import matplotlib.pyplot as plt
    if channel is None:
        guildid = ctx.guild.id
        g = msgs_data.get(guildid)

        overall = 0
        keys = []
        for i in g.values():
            for j in i.values():
                overall += j
            for k in i.keys():
                if k not in keys:
                    keys.append(k)
            print('keys=', keys)
            keys.sort()
            print(keys)
        months = {1: 'Jan',
                  2: 'Feb',
                  3: 'Mar',
                  4: 'Apr',
                  5: 'May',
                  6: 'Jun',
                  7: 'Jul',
                  8: 'Aug',
                  9: 'Sep',
                  10: 'Oct',
                  11: 'Nov',
                  12: 'Dec'}
        days = []
        msgs = []
        for char in keys:
            char = str(char)
            conv = char.split('-')
            day = conv[0]
            mon = months.get(int(conv[1]))

            final = day + '-' + mon
            days.append(final)

        msgs_rec = {}
        for i in g.values():
            for char in keys:
                a = i.get(char)
                b = msgs_rec.get(char)
                if b is None:
                    b = 0
                if a is None:
                    a = 0
                msgs_rec.update({char: a + b})
                print(msgs_rec)
        for i in msgs_rec.values():
            msgs.append(i)
        print(days)
        print(msgs)
        today = date.today()
        d = today.strftime('%d-%m-%Y')

        graphchl = bot.get_channel(807881486807334913)
        x = days
        y = msgs
        COLOR = 'yellow'
        plt.rcParams['text.color'] = COLOR
        plt.rcParams['axes.labelcolor'] = COLOR
        plt.rcParams['xtick.color'] = COLOR
        plt.rcParams['ytick.color'] = COLOR
        plt.plot(x, y)
        plt.xlabel('Day')
        plt.ylabel('Messages')
        plt.rc('grid', linestyle="-", color='white')
        plt.scatter(x, y)
        plt.grid(True)

        plt.savefig('graph.png', transparent=True)
        plt.close()
        file = discord.File("graph.png", filename="graph.png")
        msg = await graphchl.send(file=file)
        for attachment in msg.attachments:
            a = attachment.url
        os.remove('graph.png')

        embed = discord.Embed(title='Stats',
                              description='Here are the stats for `{}`:'.format(ctx.guild.name),
                              color=embedcolor)
        embed.add_field(name='Total Messages', value=str(overall))
        embed.add_field(name='Messages sent today', value=str(msgs_rec.get(d)))
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        embed.set_image(url=a)
    else:
        chl = channel.split('#')
        chl = chl[1]
        chl = list(chl)
        chl.pop(-1)
        chlid = ''.join(chl)

        guildid = ctx.guild.id
        g = msgs_data.get(guildid)
        chan = g.get(int(chlid))

        if chan is not None:
            overall = 0
            keys = []
            msgs_rec = {}
            for i in chan.values():
                overall += i
            for j in chan.keys():
                if j not in keys:
                    keys.append(j)

            for char in keys:
                number = chan.get(char)
                msgs_rec.update({char: number})
            months = {1: 'Jan',
                      2: 'Feb',
                      3: 'Mar',
                      4: 'Apr',
                      5: 'May',
                      6: 'Jun',
                      7: 'Jul',
                      8: 'Aug',
                      9: 'Sep',
                      10: 'Oct',
                      11: 'Nov',
                      12: 'Dec'}
            days = []
            msgs = []
            for char in keys:
                char = str(char)
                conv = char.split('-')
                day = conv[0]
                mon = months.get(int(conv[1]))

                final = day + '-' + mon
                days.append(final)
                msgs.append(msgs_rec.get(char))

            today = date.today()
            d = today.strftime('%d-%m-%Y')

            graphchl = bot.get_channel(807881486807334913)
            x = days
            y = msgs
            COLOR = 'yellow'
            plt.rcParams['text.color'] = COLOR
            plt.rcParams['axes.labelcolor'] = COLOR
            plt.rcParams['xtick.color'] = COLOR
            plt.rcParams['ytick.color'] = COLOR
            plt.plot(x, y)
            plt.xlabel('Day')
            plt.ylabel('Messages')
            plt.title('')
            plt.rc('grid', linestyle="-", color='white')
            plt.scatter(x, y)
            plt.grid(True)

            plt.savefig('graph.png', transparent=True)
            plt.close()
            file = discord.File("graph.png", filename="graph.png")
            msg = await graphchl.send(file=file)
            for attachment in msg.attachments:
                a = attachment.url
            os.remove('graph.png')

            embed = discord.Embed(title='Stats',
                                  description='Here are the stats for <#{}>:'.format(chlid),
                                  color=embedcolor)
            embed.add_field(name='Total Messages', value=str(overall))
            embed.add_field(name='Messages sent today', value=str(msgs_rec.get(d)))
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            embed.set_image(url=a)
        else:
            embed = discord.Embed(title='Stats',
                                  description='Here are the stats for <#{}>:'.format(chlid),
                                  color=embedcolor)
            embed.add_field(name='Total Messages', value=str(0))
            embed.add_field(name='Messages sent today', value=str(0))
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            embed.set_image(
                url='https://media.discordapp.net/attachments/807969244200304643/807969327579660288/go_chat.jpeg')

    await loading.delete()
    await ctx.send(embed=embed)


@bot.command()
async def save(ctx):
    temp_dict = msgs_data
    file = open('messages.txt', 'w')
    file.write(str(temp_dict))
    file.close()


@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Info..?',
                          description='Here is the url to invite me: [Link](https://discord.com/api/oauth2/authorize?client_id=795334771718226010&permissions=8&scope=bot)\n'
                                      'Join official discord: [Join](https://discord.gg/C3XVJk7H8k)',
                          color=embedcolor)
    await ctx.send(embed=embed)


@bot.command()
async def rule(ctx):
    if ctx.author.id != 771601176155783198:
        return
    ava = await bot.fetch_user(795334771718226010)
    avaurl = ava.avatar_url

    myguild = bot.get_guild(ctx.guild.id)
    a = myguild.get_member(795334771718226010)
    dname = a.display_name
    print(dname)
    web = await ctx.channel.create_webhook(name=dname)
    WEBHOOK_URL = web.url

    async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        embed = discord.Embed(title='Server Rules',
                              description='Here are the mandatory rules:\n'
                                          'If you witness someone breaking ANY of these rules please contact any active Moderator/Admib immediately with proof!',
                              color=embedcolor)
        embed.add_field(
            name='[1] Discord Terms of Service and Community Guidelines, as well Krunker\'s Terms & Conditions apply to this server',
            value='You must follow both of these in order to stay in the server! If you\'re caught breaking them you will be removed')
        embed.add_field(name='[2] Account Trading or Selling',
                        value='If you\'re caught attempting to sell accounts you will be removed from the server!',
                        inline=False)
        embed.add_field(name='[3] Communicate using English only',
                        value='All other languages in <#781071181314392064>\n'
                              'Communicate in English around the server, even in Pickups Chat', inline=False)
        embed.add_field(inline=False, name='[4] No Self Promotion or Advertisement',
                        value='DM an admin to get Content Creator role, this will allow you to Promote your Twitch/Youtube in <#786956059495104554>.\n'
                              'Otherwise any Self Promotion or Advertisement will be removed and you will be punished!')
        embed.add_field(inline=False, name='[5] Use an appropriate Name and Profile Picture',
                        value='Avoid any Special Characters and Emojis\n'
                              'There must be at least 3 standard characters in your nickname, so that you can be pinged')
        embed.add_field(inline=False, name='[6] No Personal Information',
                        value='Protect your privacy and the privacy of others\n'
                              'Don\'t reveal any personal info of others without their prior consent')
        embed.add_field(inline=False, name='[7] No Political or Religious topics',
                        value='We do not want to offend any users on the server so please stay away from these topics\n'
                              'Religious topics includes racial slurs. No swearing or being toxic against a specific nationality!')
        embed.add_field(inline=False, name='[8] Use common sense',
                        value='Attempting to use loopholes/bypasses can result in a larger punishment')
        embed.add_field(inline=False, name='[9] No Harassing, Abusing, or Bullying',
                        value='We have zero-tolerance for harming others\n'
                              'Jokes may be let off depending on the severity')
        embed.add_field(inline=False, name='[10] Do not spam',
                        value='Avoid excessive messages, images, formatting, emojis, commands, and @mentions\n'
                              'Avoid Ghost Pinging, if you do so by accident let the pinged user know')
        embed.add_field(inline=False, name='[11] No hackusating',
                        value='DM a staff member with adequate proof\n'
                              'Don\'t accuse another person of hacks in public chats')
        embed.add_field(inline=False, name='[12] Don\'t disobey staff',
                        value='When asked to stop, stop!')
        embed.add_field(inline=False, name='[13] Do Not DM any Staff Members until asked',
                        value='Do not DM any Admin/Mod for any reason whatsoever, until asked, even if they are active in chat')
        embed.add_field(
            name='Violation of this rule will lead to a irrevocable mute of 12 hours which will be incremented to kick/ban if you are found guilty again.',
            value='Thank You')
        embed.set_footer(text='Bot by: AwesomeSam#0001')

        await webhook.send(embed=embed, username=dname, avatar_url=avaurl)
        await web.delete()
        return


@bot.command()
@commands.has_permissions(manage_channels=True)
async def links(ctx):
    thisguild = links_data.get(ctx.message.guild.id)
    file2 = thisguild.get('allowed')
    if file2 is None:
        embed = discord.Embed(title='Whoops!',
                              description='Links are not configured for this server!',
                              color=embedcolor)
        await ctx.send(embed=embed)
        return
    main = ''
    for i in range(len(file2)):
        main = main + '<#' + str(file2[i]) + '>\n'
    embed = discord.Embed(title='List of channel with links **allowed**:',
                          description=main,
                          color=embedcolor)
    await ctx.send(embed=embed)


import time
from aiohttp import ClientSession


@bot.command()
@commands.has_permissions(administrator=True)
async def p(ctx, *, toprint: str):
    print(toprint)


@bot.command()
async def setup(ctx, *, setupid: str = None):
    if setupid is None:
        embed = discord.Embed(title='Features Setup',
                              description='You can setup the following:',
                              color=embedcolor)
        embed.add_field(name='`rr`', value='Reaction Roles')
        embed.add_field(name='`applications`', value='Krunker applications extended support')
        embed.add_field(name='`arcade`', value='DIKE Arcade- Play fun games with your friends!')
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
        return
    if setupid == 'applications':
        embed = discord.Embed(title='Enter the Message Type:',
                              description='`1- Group Roles`\n'
                                          '`2- Single Role`',
                              color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        m1 = await ctx.send(embed=embed)
    if setupid == 'rr':
        embed = discord.Embed(title='Enter the Message Type:',
                              description='`1- Group Roles`\n'
                                          '`2- Single Role`',
                              color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        m1 = await ctx.send(embed=embed)

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await bot.wait_for("message", check=check, timeout=120)

            if msg.content == '1':
                await m1.delete()
                await msg.delete()
                embed = discord.Embed(title='Enter the Message Type:',
                                      description='Enter how many roles you want to add in 1 single message. (Recommended: Maximum 10)',
                                      color=embedcolor)
                embed.set_footer(text='Bot by: AwesomeSam#0001')
                m1 = await ctx.send(embed=embed)

                while True:
                    msg = await bot.wait_for("message", check=check, timeout=120)

                    try:
                        mesg = int(msg.content)
                        await m1.delete()
                        await msg.delete()
                    except ValueError:
                        embed = discord.Embed(title='Enter the Message Type:',
                                              description='Incorrect Input. Please try again.',
                                              color=embedcolor)
                        embed.set_footer(text='Bot by: AwesomeSam#0001')
                        await ctx.send(embed=embed)
                    else:
                        break

                while True:
                    messages = {ctx.channel.id: []}
                    temp = []
                    desc = ''
                    for i in range(1, mesg + 1):
                        embed = discord.Embed(title='Role ({}/{})'.format(i, mesg),
                                              description='__Step I:__ Enter the Message (Exact will be displayed after creation beside the Emoji)',
                                              color=embedcolor)
                        embed.set_footer(text='Bot by: AwesomeSam#0001')
                        m1 = await ctx.send(embed=embed)

                        message_to_display = await bot.wait_for("message", check=check, timeout=120)

                        embed = discord.Embed(title='Role ({}/{})'.format(i, mesg),
                                              description='__Step II:__ Enter the Emoji (The emoji should be default/from this server only!)',
                                              color=embedcolor)
                        embed.set_footer(text='Bot by: AwesomeSam#0001')
                        m2 = await ctx.send(embed=embed)

                        emoji_to_display = await bot.wait_for("message", check=check, timeout=120)

                        embed = discord.Embed(title='Role ({}/{})'.format(i, mesg),
                                              description='__Step III:__ **Tag** the role you want to give',
                                              color=embedcolor)
                        embed.set_footer(text='Bot by: AwesomeSam#0001')
                        m3 = await ctx.send(embed=embed)

                        role_to_give = await bot.wait_for("message", check=check, timeout=120)

                        roleid = role_to_give.content.split('&')
                        roleid = roleid[1]
                        roleid = list(roleid)
                        roleid.pop(-1)
                        roleid = ''.join(roleid)

                        fakedict = {emoji_to_display.content: roleid}
                        mydict = messages.get(ctx.channel.id)
                        mydict.append(fakedict)
                        mainfake = {ctx.channel.id: mydict}
                        messages.update(mainfake)

                        temp.append(emoji_to_display.content)
                        desc += '{} --> {}\n'.format(emoji_to_display.content, message_to_display.content)

                        await m1.delete()
                        await message_to_display.delete()
                        await m2.delete()
                        await emoji_to_display.delete()
                        await m3.delete()
                        await role_to_give.delete()
                    break

                embed = discord.Embed(title='React here to Add/Remove your role:',
                                      description=desc,
                                      color=embedcolor)
                embed.set_footer(text='Bot by: AwesomeSam#0001')
                m = await ctx.send(embed=embed)

                for i in temp:
                    await m.add_reaction(i)

                to_translate = messages.get(ctx.channel.id)
                messages.pop(ctx.channel.id)
                finaldict = {str(m.id): to_translate}
                messages.update(finaldict)
                rr_data.update(messages)

                file = open('rr.txt', 'w', encoding='utf8', errors='ignore')
                file.write(str(rr_data))
                file.close()
                print(messages)

        except TimeoutError:
            embed = discord.Embed(title='Times Up',
                                  description='Sorry, you didn\'t reply in time.',
                                  color=embedcolor)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await ctx.send(embed=embed)
            return
    else:
        embed = discord.Embed(description='**Coming Soon...**',
                              color=embedcolor)
        await ctx.send(embed=embed)


@bot.event
async def on_raw_reaction_add(payload):
    try:
        roledata = rr_data.get(str(payload.message_id))
    except:
        return

    try:
        for i in roledata:
            role_id = i.get(payload.emoji.name)
            if role_id is not None:
                break
    except TypeError:
        return
    guild_id = payload.guild_id
    myguild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
    role = discord.utils.get(myguild.roles, id=int(role_id))
    member = discord.utils.find(lambda m: m.id == payload.user_id, myguild.members)

    try:
        await member.add_roles(role)
    except PermissionError:
        embed = discord.Embed(title='Whoops!',
                              description='Looks like I am missing permissions. Try:\n'
                                          '1. Granting me required permissions\n'
                                          '2. Making sure that my role is above the reaction role.',
                              color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await payload.channel.send(embed=embed)


@bot.event
async def on_raw_reaction_remove(payload):
    try:
        roledata = rr_data.get(str(payload.message_id))
    except:
        return

    try:
        for i in roledata:
            role_id = i.get(payload.emoji.name)
            if role_id is not None:
                break
    except TypeError:
        return
    guild_id = payload.guild_id
    myguild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
    role = discord.utils.get(myguild.roles, id=int(role_id))
    member = discord.utils.find(lambda m: m.id == payload.user_id, myguild.members)

    try:
        await member.remove_roles(role)
    except PermissionError:
        embed = discord.Embed(title='Whoops!',
                              description='Looks like I am missing permissions. Try:\n'
                                          '1. Granting me required permissions\n'
                                          '2. Making sure that my role is above the reaction role.',
                              color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await payload.channel.send(embed=embed)


@bot.command(pass_context=True, aliases=['clean'])
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)


@bot.command()
async def help(ctx, *, help_id: str = None):
    ava = await bot.fetch_user(795334771718226010)
    avaurl = ava.avatar_url
    name = ava.display_name

    myguild = bot.get_guild(ctx.guild.id)
    a = myguild.get_member(795334771718226010)
    dname = a.display_name
    print(dname)
    web = await ctx.channel.create_webhook(name=dname)

    WEBHOOK_URL = web.url
    if help_id is None:
        clog = '[Join Support Server](https://discord.gg/C3XVJk7H8k) | ' \
               '[Invite Me](https://discord.com/api/oauth2/authorize?client_id=795334771718226010&permissions=8&scope=bot)\n'

        embed = discord.Embed(title='DIKE Official Bot Help:',
                              description=clog,
                              color=embedcolor)
        chelp = help_data.get(ctx.guild.id)
        if chelp is not None:
            embed.add_field(name='`apply`', value='Minimum Requirements to join clan')
        embed.add_field(name='`stats`', value='Show stats related to server or channel')
        embed.add_field(name='`mod`', value='Moderation Commands')
        embed.add_field(name='`arcade`', value='Have fun with others in DIKE Arcade!')
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
        await web.delete()
        return

    if help_id == 'apply':
        chelp = help_data.get(ctx.guild.id)
        if chelp is None:
            return
        level = chelp.get('level')
        kpg = chelp.get('kpg')
        kdr = chelp.get('kdr')
        nukes = chelp.get('nukes')
        spk = chelp.get('spk')
        add = chelp.get('additional')
        if add is not None:
            clog = 'Here are the minimum requirements:\n' \
                   '```python\n' \
                   '"--> Level:     {}"\n' \
                   '"--> KDR:       {}"\n' \
                   '"--> SPK:       {}"\n' \
                   '"--> KPG:       {}"\n' \
                   '"--> Nukes:     {}"```\n\n' \
                   '{}'.format(level, kdr, spk, kpg, nukes, add)
        else:
            clog = 'Here are the minimum requirements:\n' \
                   '```python\n' \
                   '"--> Level:     {}"\n' \
                   '"--> KDR:       {}"\n' \
                   '"--> SPK:       {}"\n' \
                   '"--> KPG:       {}"\n' \
                   '"--> Nukes:     {}"```\n\n'.format(level, kdr, spk, kpg, nukes)

        embed = discord.Embed(title='DIKE Official Bot Help:',
                              description=clog,
                              color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif help_id == 'arcade' or help_id == 'arcade 1':
        clog = '[Join Support Server](https://discord.gg/C3XVJk7H8k) | ' \
               '[Invite Me](https://discord.com/api/oauth2/authorize?client_id=795334771718226010&permissions=8&scope=bot)\n'
        embed = discord.Embed(title='DIKE Official Bot Help:',
                              description=clog,
                              color=embedcolor)
        embed.add_field(name='`!balance`', value='View your balance', inline=False)
        embed.add_field(name='`!inventory`', value='View your inventory', inline=False)
        embed.add_field(name='`!gamble`', value='Gamble your coins for a 50-50 win/lose chance', inline=False)
        embed.add_field(name='`!rich`', value='See the richest people in your server!', inline=False)
        embed.add_field(name='`!give`', value='Donate some of your coins to your friend', inline=False)
        embed.set_footer(text='Page 1 out of 2')
        await ctx.send(embed=embed)
    elif help_id == 'arcade 2':
        clog = '[Join Support Server](https://discord.gg/C3XVJk7H8k) | ' \
               '[Invite Me](https://discord.com/api/oauth2/authorize?client_id=795334771718226010&permissions=8&scope=bot)\n'
        embed = discord.Embed(title='DIKE Official Bot Help:',
                              description=clog,
                              color=embedcolor)
        embed.add_field(name='`!shop`', value='View all the items in the shop', inline=False)
        embed.add_field(name='`!buy`', value='Buy some stuff from the shop', inline=False)
        embed.add_field(name='`!job`', value='View all available jobs', inline=False)
        embed.add_field(name='`!apply`', value='Apply for a job to earn coins', inline=False)
        embed.set_footer(text='Page 2 out of 2')
        await ctx.send(embed=embed)
    elif help_id == 'mod':
        clog = '[Join Support Server](https://discord.gg/C3XVJk7H8k) | ' \
               '[Invite Me](https://discord.com/api/oauth2/authorize?client_id=795334771718226010&permissions=8&scope=bot)\n'

        async with ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
            embed = discord.Embed(title='DIKE Official Bot Help:',
                                  description=clog,
                                  color=embedcolor)
            embed.add_field(name='`warn`', value='Warns the user\n   Syntax: `!warn <user> <reason>`', inline=False)
            embed.add_field(name='`mute`', value='Mutes the user\n   Syntax: `!mute <user> [time]`', inline=False)
            embed.add_field(name='`unmute`', value='Unmutes the user\n   Syntax: `!unmute <user>`', inline=False)
            embed.add_field(name='`slowmode`', value='Puts the current channel in slowmode\n   Syntax: `!sm <time>`',
                            inline=False)
            embed.add_field(name='`clean`', value='Cleans certain number of messages\n   Syntax: `!clean <number>`',
                            inline=False)
            embed.add_field(name='Note:', value='<> = Required | [ ] = Optional', inline=False)
            embed.set_footer(text='Bot by: AwesomeSam#0001')
            await webhook.send(embed=embed, username=dname, avatar_url=avaurl)
    await web.delete()


@bot.command(aliases=['feedback'])
async def suggest(ctx, *, text: str = None):
    if text is None:
        await ctx.send(
            '<@{}> The format for suggestion command is: `!suggest <Your-Suggestion-Here>` (without `<` or `>`)'.format(
                ctx.author.id))
        return
    feedback_chl = bot.get_channel(798091588676747285)
    await ctx.send('<@{}> Suggestion sent in <#{}> successfully!'.format(ctx.author.id, feedback_chl.id))
    compile = text + '\n\nSent by: {}'.format(ctx.author)
    await feedback_chl.send('<@&805752064067633203> \n' + '```\n' + compile + '\n```')


owner = 769543339627249714
mod = 773629756570599454
admin = 781377928898412564


@bot.command(aliases=['sm'])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    if seconds == 0:
        await ctx.send(
            "<#{}> is no longer in slowmode.".format(ctx.channel.id))
    elif seconds < 0:
        pass
    else:
        await ctx.send(
            "<#{}> is in `s l o w m o d e`.\nUsers will be able to post every {} seconds!".format(ctx.channel.id,
                                                                                                  seconds))


@bot.command()
@commands.has_permissions(manage_channels=True)
async def say(ctx, channel: str, *, tosay: str):
    chlid = channel.split('#')
    chlid = chlid[1]
    chlid = list(chlid)
    chlid.pop(-1)
    chlid = ''.join(chlid)

    chl = bot.get_channel(int(chlid))
    await chl.send(tosay)


@bot.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def warn(ctx, user: discord.Member, *, reason=None):
    warnings = {'war1': 796249188832509953,
                'war2': 796249230774763540,
                'war3': 796249281295024178,
                'war4': 796249305391562782,
                'war5': 796249325877461033,
                'war6': 796249348991614976,
                'war7': 796249379110649856,
                'war8': 796249402527711303,
                'war9': 796249425965350913,
                'war10': 796249447255900171,
                'war11': 796249469041508393}

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


@bot.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def mute(ctx, member: discord.Member, mtime=None):
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

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if mtime is None:
        await member.add_roles(muted_role)
        await ctx.send('☑️ User Muted Successfully')
    else:
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempmute = int(mtime[:-1]) * time_convert[mtime[-1]]
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


@bot.command()
async def id(ctx):
    await ctx.send(ctx.channel.id)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def addlink(ctx):
    myguild = dict(eval(str(links_data.get(ctx.message.guild.id))))
    allowed_links = myguild.get('allowed')
    if ctx.channel.id in allowed_links:
        await ctx.send('☑️ <#{}> already in in allowed links.'.format(ctx.channel.id))
        return
    allowed_links.append(ctx.channel.id)
    fakedict = {"allowed": allowed_links}
    fakemain = {ctx.message.guild.id: myguild}
    links_data.update(fakemain)

    links_file = open('allowed_links.txt', 'w')
    links_file.write(str(links_data))
    links_file.close()

    await ctx.send('☑️ <#{}> added in allowed links.'.format(ctx.channel.id))


@bot.command()
@commands.has_permissions(manage_channels=True)
async def removelink(ctx):
    myguild = links_data.get(ctx.message.guild.id)
    allowed_links = myguild.get('allowed')

    if ctx.channel.id in allowed_links:
        allowed_links.remove(ctx.channel.id)
        fakedict = {"allowed": allowed_links}
        fakemain = {ctx.message.guild.id: myguild}
        links_data.update(fakemain)

        links_file = open('allowed_links.txt', 'w')
        links_file.write(str(links_data))
        links_file.close()
        await ctx.send('❌ <#{}> removed from allowed links successfully!'.format(ctx.channel.id))
    else:
        await ctx.send('<#{}> is not in allowed links!'.format(ctx.channel.id))


@bot.command()
@commands.has_permissions(administrator=True)
async def autoroles(ctx):
    embed = discord.Embed(title='Auto Roles Setup',
                          description='__Step I:__ Enter how many roles you want to give',
                          color=embedcolor)
    m1 = await ctx.send(embed=embed)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=120)

        number = int(msg.content)

        await msg.delete()
        await m1.delete()

        roles = []
        for i in range(1, number + 1):
            embed = discord.Embed(title='Tag Role ({}/{})'.format(i, number + 1),
                                  color=embedcolor)
            m1 = await ctx.send(embed=embed)
            msg = await bot.wait_for("message", check=check, timeout=120)

            chl = msg.content.split('&')
            chl = chl[1]
            chl = list(chl)
            chl.pop(-1)
            chlid = ''.join(chl)

            roles.append(int(chlid))
            await msg.delete()
            await m1.delete()

        mydict = {ctx.guild.id: roles}
        ar_data.update(mydict)
        file = open('autoroles.txt', 'w')
        file.write(str(ar_data))
        file.close()

        embed = discord.Embed(title='☑️ Done',
                              color=embedcolor)
        m1 = await ctx.send(embed=embed)

    except TimeoutError:
        embed = discord.Embed(title='Whoops! Times Up.',
                              description='Sorry, you ran out of time.',
                              color=embedcolor)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    await ctx.send('☑️ User Unmuted Successfully')


@bot.event
async def on_member_join(member):
    allusers = 0
    for guild in bot.guilds:
        allusers += len(guild.members)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing,
                                  name="!help with {} people in {} servers".format(allusers, len(bot.guilds))))
    if member.guild.id == 766875360126042113:
        welcom_chl = bot.get_channel(773401123389440011)
        welmsg = '<a:hello:786862994381471766> Hyy <@{user}> Welcome to Official DIKE Clan <a:hello:786862994381471766> **Type `!help` to get help**\n' \
                 '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                 '<a:ARR:786863234736455680> MUST READ AND FOLLOW <#773626644324810762>  <a:ARR:786863090670239744>\n' \
                 '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                 '<a:ARR:786863234736455680> CHECK <#773404953377112104> TO KNOW HOW TO GET ROLES <a:ARR:786863090670239744>\n' \
                 '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                 '<a:ARR:786863234736455680> MUST BE UPDATED AND READ DAILY <#773876008725905420> <a:ARR:786863090670239744>\n' \
                 '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                 '<a:ARR:786863234736455680> MUST BE ACTIVE IN CHAT <#766875360595410946>  AND UNLOCK LEVEL AND ROLES <a:blueflame:786863090670239744>\n' \
                 '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                 '<a:yldz:786863153454645269> <:line:798799010088747008> <:line:798799010088747008> HOPE YOU WILL ENJOY <:line:798799010088747008> <:line:798799010088747008> <a:yldz:786863153454645269>'.format(
            user=member.id)
        await welcom_chl.send(welmsg)
        myguild = bot.get_guild(766875360126042113)

        member_count = 0
        for member in myguild.members:
            member_count += 1
        true_member_count = len([m for m in myguild.members if not m.bot])
        bot_count = len([m for m in myguild.members if m.bot])

        total = bot.get_channel(798053370925023282)
        mem = bot.get_channel(798053462281420870)
        bots = bot.get_channel(798053532477161532)

        await total.edit(name='All Members: {}'.format(member_count))
        await mem.edit(name='Members: {}'.format(true_member_count))
        await bots.edit(name='Bots: {}'.format(bot_count))

    roles_to_give = ar_data.get(member.guild.id)
    if roles_to_give is None:
        return
    for i in roles_to_give:
        get_role = discord.utils.get(member.guild.roles, id=i)
        await member.add_roles(get_role)


@bot.event
async def on_member_leave(member):
    allusers = 0
    for guild in bot.guilds:
        allusers += len(guild.members)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="!help with {} people".format(allusers)))

    leaving_chl = bot.get_channel(800683977207840798)
    leave_msg = '{} just left the server.'.format(member.name)
    print(leave_msg)
    await leaving_chl.send(leave_msg)
    myguild = bot.get_guild(766875360126042113)

    member_count = 0
    for member in myguild.members:
        member_count += 1
    true_member_count = len([m for m in myguild.members if not m.bot])
    bot_count = len([m for m in myguild.members if m.bot])

    total = bot.get_channel(798053370925023282)
    mem = bot.get_channel(798053462281420870)
    bots = bot.get_channel(798053532477161532)

    await total.edit(name='All Members: {}'.format(member_count))
    await mem.edit(name='Members: {}'.format(true_member_count))
    await bots.edit(name='Bots: {}'.format(bot_count))

@bot.event
async def on_server_join(ctx):
    allusers = 0
    for guild in bot.guilds:
        allusers += len(guild.members)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing,
                                  name="!help with {} people in {} servers".format(allusers, len(bot.guilds))))

@bot.event
async def on_ready():
    allusers = 0
    for guild in bot.guilds:
        allusers += len(guild.members)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing,
                                  name="!help with {} people in {} servers".format(allusers, len(bot.guilds))))
    myguild = bot.get_guild(766875360126042113)
    if myguild is None:
        print('Ready!')
        return
    member_count = 0
    for member in myguild.members:
        member_count += 1
    true_member_count = len([m for m in myguild.members if not m.bot])
    bot_count = len([m for m in myguild.members if m.bot])

    total = bot.get_channel(798053370925023282)
    mem = bot.get_channel(798053462281420870)
    bots = bot.get_channel(798053532477161532)

    await total.edit(name='All Members: {}'.format(member_count))
    await mem.edit(name='Members: {}'.format(true_member_count))
    await bots.edit(name='Bots: {}'.format(bot_count))
    print('Ready!')


links_file = open('allowed_links.txt', 'r')
links_data = dict(eval(str(links_file.read())))
links_file.close()

import json

reactionrole = open('rr.txt', 'r', encoding='utf8', errors='ignore')
rr_data = ast.literal_eval(reactionrole.read())
reactionrole.close()

messages = open('messages.txt', 'r')
msgs_data = dict(eval(str(messages.read())))
messages.close()

autor = open('autoroles.txt', 'r')
ar_data = dict(eval(str(autor.read())))
autor.close()

autor = open('customhelp.txt', 'r')
help_data = dict(eval(str(autor.read())))
autor.close()

bot.run(TOKEN)

dikemod = 799521293673168898
'''my = open('arcade_bal.txt', 'r')
data = my.read()
config_dict = eval(data)
config_dict = dict(config_dict)

my2 = open('hacking_data.txt', 'r')
data2 = my2.read()
items = eval(data2)
items = dict(items)'''

'''@bot.command()
async def apply(ctx, job_id=None):
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
                await ctx.send(
                    '<@{}> Unjumble the following sentence in 25 secs:\n`{}`'.format(ctx.author.id, jumbled_sen))

                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                try:
                    msg = await bot.wait_for("message", check=check, timeout=25)  # 30 seconds to reply
                    print(msg, sentence)
                    if msg.content.lower() == jumbled_sen:
                        await ctx.send('<@{}> **No Cheating!!**'.format(ctx.author.id))
                        return
                    if msg.content.lower() == sentence.lower():
                        await ctx.send(
                            '<@{}> And you are absolutely correct! Here are your `20 Ð`'.format(ctx.author.id))
                        curr_bal = config_dict.get(ctx.author.id)
                        new_b = curr_bal + 20
                        mydict = {ctx.author.id: new_b}
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

                        amt = int((point / length) * 20)
                        if amt == 20:
                            amt = 19
                        await ctx.send(
                            '<@{}> Unfortunately, you aren\'t 100% correct. Still, I give you `{} Ð`.'.format(
                                ctx.author.id, amt))
                        curr_bal = config_dict.get(ctx.author.id)
                        new_b = curr_bal + amt
                        mydict = {ctx.author.id: new_b}
                        config_dict.update(mydict)
                        update_book()
                except asyncio.TimeoutError:
                    await ctx.send("<@{}> Oops! You ran out of time 🕑".format(ctx.author.id))
            elif int(job_id) == 2:
                emoji_list = ['😅', '🙂', '😛', '😞', '😠', '🤯', '🤓', '😟', '🤥', '🥱', '😪', '😑', '🤔', '🤨', '🧐',
                              '😎', '🤩', '🥳', '😤']
                link_dict = {
                    'https://media.discordapp.net/attachments/795906303884525569/796022790393167932/unknown.png': '🤯 😑 🧐 😞 😛 🤓',
                    'https://media.discordapp.net/attachments/795906303884525569/796022997868871710/unknown.png': '😤 😠 🤨 😞 🙂 😎',
                    'https://media.discordapp.net/attachments/795906303884525569/796023227532443648/unknown.png': '🥱 😪 🤥 😞 😠 😤',
                    'https://media.discordapp.net/attachments/795906303884525569/796023386949025812/unknown.png': '🤨 😟 🤔 😅 🤓 😎',
                    'https://media.discordapp.net/attachments/795906303884525569/796023549482631168/unknown.png': '🤩 🤓 🥳 🧐 😅 😟',
                    'https://media.discordapp.net/attachments/795906303884525569/796023762549473280/unknown.png': '🥳 😞 😅 😟 🤥 🙂',
                    'https://media.discordapp.net/attachments/795906303884525569/796023892649050123/unknown.png': '😟 😛 🤓 🧐 😤 😑',
                    'https://media.discordapp.net/attachments/795906303884525569/796024114698649660/unknown.png': '🤥 😎 😑 😠 😟 🥱',
                    'https://media.discordapp.net/attachments/795906303884525569/796024315497152562/unknown.png': '🤩 😑 🧐 😪 😟 🤓',
                    'https://media.discordapp.net/attachments/795906303884525569/796024461845200926/unknown.png': '🧐 🙂 😞 🤔 😪 🤨'
                    }
                link_list = [
                    'https://media.discordapp.net/attachments/795906303884525569/796022790393167932/unknown.png',
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
                    msg = await bot.wait_for("message", check=check, timeout=120)
                    msgg = msg
                    msg = msg.content.split()
                    msg2 = msgg.content.split(' ')
                    try:
                        for b in range(6):
                            if msg[b] in dictemo:
                                emo_pt += 1
                    except:
                        pass
                    dikeamt = int((emo_pt / 6) * 50)
                    if dictemo == msg or dictemo == msg2:
                        await ctx.send(
                            '<@{}> Your Score: 6/6 \n**Congratulation! You got extra `10 Ð` for putting them in same order!**\n**You have been credited with `60 Ð`**'.format(
                                ctx.author.id))
                        cur_bal = config_dict.get(ctx.author.id)
                        nbal = cur_bal + 60
                        dictt = {ctx.author.id: nbal}
                        config_dict.update(dictt)
                        update_book()
                    else:
                        await ctx.send(
                            '<@{}> Your Score: {}/6 \n**You have been credited with `{} Ð`. Have Fun :)**'.format(
                                ctx.author.id, emo_pt, dikeamt))
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
                if 799164121589088277 in [y.id for y in ctx.author.roles]:
                    await ctx.send('<@{}> Your 6 hrs ain\'t completed. Please wait.')
                    return
                dict_to_update = items.get(ctx.author.id)
                if dict_to_update.get('comp') == 'False':
                    await ctx.send('<@{}> You don\'t have a 💻 Computer. Go to shop and buy it to start hacking'.format(
                        ctx.author.id))
                    return
                await ctx.send('<@{}> **Basic Rules:-**\n'
                               '1. If you get caught, you lose your computer\n'
                               '2. Type `!use <item-code>` to use your 🧭 Trace Lower (`trace`) or 🖲️ Emergency Escape (`esc`)'.format(
                    ctx.author.id))
                hackvalue = random.randint(1000, 5000)
                await ctx.send('**Estimated Value Gain: {}**\n'
                               'Type `y` to start or `n` to cancel. You will be able to apply after 2 hrs if cancelled'.format(
                    hackvalue))

                def check2(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                myguild = bot.get_guild(766875360126042113)
                msg = await bot.wait_for("message", check=check2, timeout=30)
                try:
                    if msg.content.lower() == 'n':
                        await ctx.send(
                            '<@{}> You cancelled the job. You will be eligible in **2 hours and 0 minutes**'.format(
                                ctx.author.id))
                        role = discord.utils.get(myguild.roles, id=timedout)
                        await ctx.author.add_roles(role)
                        await asyncio.sleep(2 * 60 * 60)
                        await ctx.author.remove_roles(role)

                    elif msg.content.lower() == 'y':
                        decodetime = 15
                        trace = 30
                        qboard = dict_to_update.get('qboard')
                        vpn = dict_to_update.get('vpn')
                        pc = dict_to_update.get('pc')

                        if pc == 'True':
                            decodetime = 8
                        if vpn == 'True':
                            trace = trace * 1.3
                        if qboard == 'True':
                            slowinput = False
                        else:
                            slowinput = True
                        starttime = time.time()
                        try:
                            while True:
                                await ctx.send('<@{}> ❗ You have {time} secs till the 👮 police traces you ❗\n'
                                               'Type `brew install heroku-toolbel`'.format(ctx.author.id, time = int(trace)))

                                def check2(msg):
                                    return msg.author == ctx.author and msg.channel == ctx.channel

                                msg = await bot.wait_for("message", check=check2, timeout=trace)
                                if slowinput:
                                    time.sleep(4)
                                else:
                                    time.sleep(1.5)
                                if msg.content == 'brew install heroku-toolbel':
                                    emerescape = False
                                    break
                                elif msg.content == '!use trace':
                                    dict_to_update = items.get(ctx.author.id)
                                    before = dict_to_update.get('trace')
                                    if before == 0:
                                        await ctx.send('You dont own any!')
                                        return
                                    newdict = {'trace': before - 1}
                                    print(dict_to_update, type(dict_to_update))
                                    dict_to_update.update(newdict)
                                    items.update(dict_to_update)
                                    update_book()
                                    loop1time = time.time()
                                    trace = trace - (loop1time - starttime) + 11
                                    await ctx.send('Added 10 secs! Be quick!!')
                                elif msg.content == '!use esc':
                                    dict_to_update = items.get(ctx.author.id)
                                    before = dict_to_update.get('esc')
                                    if before == 0:
                                        await ctx.send('You dont own any!')
                                        return
                                    newdict = {'esc': before - 1}
                                    print(dict_to_update, type(dict_to_update))
                                    dict_to_update.update(newdict)
                                    items.update(dict_to_update)
                                    update_book()
                                    emerescape = True
                                    break
                                else:
                                    loop1time = time.time()
                                    trace = trace - (loop1time - starttime)
                                    await ctx.send('<@{}> **Incorrect Command! Remember commands are case-sensitive**'.format(ctx.author.id))
                            endtime = time.time()
                            newt = trace - int(endtime-starttime)
                            if emerescape:
                                await ctx.send(
                                    'You have dodged the police, and are now safe. But the client is not happy and has charged you `1500 Ð`')
                                cur_bal = config_dict.get(ctx.author.id)
                                nbal = cur_bal - 1500
                                dictt = {ctx.author.id: nbal}
                                config_dict.update(dictt)
                                update_book()
                                return

                            while True:
                                await ctx.send('<@{}>You have {} secs remaining.\n'
                                               'Now type `heroku create hacker-chet`'.format(ctx.author.id ,int(newt)))

                                def check2(msg):
                                    return msg.author == ctx.author and msg.channel == ctx.channel

                                msg = await bot.wait_for("message", check=check2, timeout=newt)

                                if slowinput:
                                    time.sleep(4)
                                else:
                                    time.sleep(1.5)
                                if msg.content == 'heroku create hacker-chet':
                                    emerescape = False
                                    break
                                elif msg.content == '!use trace':
                                    dict_to_update = items.get(ctx.author.id)
                                    before = dict_to_update.get('trace')
                                    if before == 0:
                                        await ctx.send('You dont own any!')
                                        return
                                    newdict = {'trace': before - 1}
                                    print(dict_to_update, type(dict_to_update))
                                    dict_to_update.update(newdict)
                                    items.update(dict_to_update)
                                    update_book()
                                    loop1time = time.time()
                                    trace = trace - (loop1time - newt) + 10
                                    await ctx.send('Added 10 secs! Be quick!!')
                                elif msg.content == '!use esc':
                                    dict_to_update = items.get(ctx.author.id)
                                    before = dict_to_update.get('esc')
                                    if before == 0:
                                        await ctx.send('You dont own any!')
                                        return
                                    newdict = {'esc': before - 1}
                                    print(dict_to_update, type(dict_to_update))
                                    dict_to_update.update(newdict)
                                    items.update(dict_to_update)
                                    update_book()
                                    emerescape = True
                                    break
                                else:
                                    loop2time = time.time()
                                    newt = newt - (loop2time - endtime)
                                    await ctx.send(
                                        '<@{}> **Incorrect Command! Remember commands are case-sensitive**'.format(
                                            ctx.author.id))
                            endtime2 = time.time()
                            if emerescape:
                                await ctx.send('You have dodged the police, and are now safe. But the client is not happy and has charged you `1500 Ð`')
                                cur_bal = config_dict.get(ctx.author.id)
                                nbal = cur_bal - 1500
                                dictt = {ctx.author.id: nbal}
                                config_dict.update(dictt)
                                update_book()
                                return
                            while True:
                                await ctx.send('<@{}> Decoding the files.. This will take approximately {} secs'.format(ctx.author.id, decodetime))
                                if int(endtime2-endtime) <= decodetime:
                                    time.sleep(int(endtime2-endtime))
                                    failed = True
                                    break
                                time.sleep(int(decodetime))
                                await ctx.send('<@{}> Hacker tast completed Sccessfully!!\nYou can apply again after 6 hrs.'.format(ctx.author.id))
                                cur_bal = config_dict.get(ctx.author.id)
                                nbal = cur_bal + int(hackvalue) + 250
                                dictt = {ctx.author.id: nbal}
                                config_dict.update(dictt)
                                update_book()
                                role = discord.utils.get(myguild.roles, id=799164121589088277)
                                await ctx.author.add_roles(role)
                                await asyncio.sleep(6 * 60 * 60)
                                await ctx.author.remove_roles(role)
                                failed = False
                                break
                            if failed:
                                raise TypeError
                        except:
                            await ctx.send('<@{}> **Times Up!** Oh no you are caught by 👮 Cyber Police. They have taken away your Laptop!!\n'
                                     'Better Luck next time..'.format(ctx.author.id))
                            newdict = {'comp': 'False'}
                            print(dict_to_update, type(dict_to_update))
                            dict_to_update.update(newdict)
                            items.update(dict_to_update)
                            update_book()
                    else:
                        await ctx.send(
                            '<@{}> Invalid Response. Assuming it to be `n`. You will be eligible in **2 hours and 0 minutes**'.format(
                                ctx.author.id))
                        role = discord.utils.get(myguild.roles, id=timedout)
                        await ctx.author.add_roles(role)
                        await asyncio.sleep(2 * 60 * 60)
                        await ctx.author.remove_roles(role)
                except:
                    await ctx.send(
                        'Response Timed Out. You will be eligible in **2 hours and 0 minutes** to apply again')
                    role = discord.utils.get(myguild.roles, id=timedout)
                    await ctx.author.add_roles(role)
                    await asyncio.sleep(2 * 60 * 60)
                    await ctx.author.remove_roles(role)

            elif int(job_id) in [3, 5]:
                await ctx.send('<@{}> **Coming Soon...**'.format(ctx.author.id))

            else:
                await ctx.send('<@{}> Invalid Option <:WierdChamp:775568297013411840>'.format(ctx.author.id))

@bot.command(aliases=['inv'])
async def inventory(ctx):
    list_of_items = [
        ['laptop', items.get(ctx.author.id).get('comp')],
        ['pc', items.get(ctx.author.id).get('pc')],
        ['qboard', items.get(ctx.author.id).get('qboard')],
        ['vpn', items.get(ctx.author.id).get('vpn')],
        ['escape', items.get(ctx.author.id).get('esc')],
        ['tracel', items.get(ctx.author.id).get('trace')]
    ]

    print_list = ''
    for char in range(len(list_of_items)):
        for char2 in range(1, len(list_of_items[char])):
            try:
                if list_of_items[char][1] == 'True':
                    print_list = print_list + list_of_items[char][0] + '\n\n'
                elif int(list_of_items[char][1]) > 0:
                    print_list = print_list + list_of_items[char][0] + '\nQty: `' + str(
                        list_of_items[char][1]) + '`\n\n'
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
        await ctx.send('<@' + str(ctx.author.id) + '> **Here is your inventory:**\n\n' + final_list)
    else:
        await ctx.send('<@' + str(ctx.author.id) + '> **You dont own anything 😂😂**\n\n' + final_list)


@bot.command()
async def buy(ctx, code: str = None):
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
            newdict = {'comp': 'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 5000
            dictbal = {ctx.author.id: newbal}
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
            newdict = {'pc': 'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 4500
            dictbal = {ctx.author.id: newbal}
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
            newdict = {'esc': before + 1}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 3000
            dictbal = {ctx.author.id: newbal}
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
            newdict = {'trace': before + 1}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 1000
            dictbal = {ctx.author.id: newbal}
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
            newdict = {'vpn': 'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 500
            dictbal = {ctx.author.id: newbal}
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
            newdict = {'qboard': 'True'}
            print(dict_to_update, type(dict_to_update))
            dict_to_update.update(newdict)
            items.update(dict_to_update)
            newbal = cur_bal - 2000
            dictbal = {ctx.author.id: newbal}
            config_dict.update(dictbal)
            update_book()
            await ctx.send('<@{}> ⌨️ QuickBoard™ purchased successfully!'.format(ctx.author.id))


@bot.command(aliases=['reset'])
async def wipe(ctx):
    id = ctx.author.id
    dicty = {id: 500}
    config_dict.update(dicty)
    mydict = {
        ctx.author.id: {'comp': 'False', 'pc': 'False', 'vpn': 'False', 'esc': 0, 'qboard': 'False', 'trace': 0}}
    items.update(mydict)
    update_book()


@bot.command()
async def config(ctx):
    if ctx.author.id == 771601176155783198:
        mem = discord.utils.get(ctx.guild.channels, id=795906303884525569)
        print(mem.members)
        dict = {}
        for user in mem.members:
            mydict = {user.id: 500}
            dict.update(mydict)
            mydict.clear()
        await ctx.send('Config Done!')
        my = open('arcade_bal.txt', 'w')
        my.write(str(dict))
        my.close()
    else:
        lol = ctx.author.id
        await ctx.send('<@{}> You ain\'t my master!'.format(lol))

@bot.command()
async def rich(ctx):
    sorted_d = dict(sorted(config_dict.items(), key=operator.itemgetter(1), reverse=True))
    mylist = list(sorted_d.items())[:5]
    embed = discord.Embed(title="Riches of the Rich", description="", color=embedcolor)
    for char in mylist:
        userid = char[0]
        amt = char[1]
        myguild = bot.get_guild(766875360126042113)
        a = myguild.get_member(userid)
        dname = a.display_name
        embed.add_field(name=dname, value='`' + str(amt) + ' Ð `', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def shop(ctx, shop_page: int = None):
    if shop_page is None:
        shoplist = '|   __Generals__   |    Hacker    |     Wars     | Bank Robbery |\n'
        desc = '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 1:
        shoplist = '|   __Generals__   |    Hacker    |     Wars     | Bank Robbery |\n'
        desc = '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 2:
        shoplist = '|   Generals   |    __Hacker__    |     Wars     | Bank Robbery |\n'
        embed = discord.Embed(title=shoplist,
                              description='Buy useful stuff here to help you in a tricky hacking situation',
                              color=embedcolor)
        embed.add_field(name='💻 Computer', value='Essential to start Hacking\nItem Code: `comp`\nPrice: `5000 Ð`\n',
                        inline=False)
        embed.add_field(name='🖥️ Assistant PC',
                        value='Lowers the hacking time significantly\nItem Code: `pc`\nPrice: `4500 Ð`\n', inline=False)
        embed.add_field(name='🖲️ Emergency Escape',
                        value='Aborts the process and protects you from Police\nItem Code: `esc`\nPrice: `3000 Ð`\n',
                        inline=False)
        embed.add_field(name='⌨️ QuickBoard™',
                        value='Your commands are taken noticeably faster\nItem Code: `qboard`\nPrice: `2000 Ð`\n',
                        inline=False)
        embed.add_field(name='🧭 Trace Lower',
                        value='Lowers your trace percentage by 10%\nItem Code: `trace`\nPrice: `1000 Ð`\n',
                        inline=False)
        embed.add_field(name='🛰️ VPN', value='Slows the Cyber Police to track you\nItem Code: `vpn`\nPrice: `500 Ð`\n',
                        inline=False)
        embed.add_field(name='\n\nType !buy <item-code> to purchase the item', value='Have Fun Hacking 😉',
                        inline=False)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 3:
        shoplist = '|   Generals   |    Hacker    |     __Wars__     | Bank Robbery |\n'
        desc = '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)
    elif shop_page == 4:
        shoplist = '|   Generals   |    Hacker    |     Wars     | __Bank Robbery__ |\n'
        desc = '\n\n                         **Coming Soon!**'
        embed = discord.Embed(title=shoplist, description=desc, color=embedcolor)
        embed.set_footer(text='Bot by: AwesomeSam#0001')
        await ctx.send(embed=embed)


@bot.command()
async def give(ctx, give_to: discord.Member = None, amount: int = None):
    if amount <= 0:
        await ctx.send('<@{}> Seriosuly?'.format(ctx.author.id))
        return
    if amount <= 10:
        await ctx.send('<@{}> Minimum amount is `10 Ð`')
        return
    if give_to is None or amount is None:
        await ctx.send('Format for !give command is: `!give <person> <amount>`')
        return
    if give_to == ctx.author:
        await ctx.send('<@{}> Sending Dikers to yourself, huh?'.format(ctx.author.id))
        return
    if amount >= 1000:
        final_amount = int(amount * 0.9)
    else:
        final_amount = amount
    cur_bal = config_dict.get(ctx.author.id)
    if int(cur_bal) < amount:
        await ctx.send('<@{}> You dont have that much yourself <:kekw:772091131596374017>'.format(ctx.author.id))
    else:
        await ctx.send(
            '<@{}> sent `{} Ð` to <@{}>. What a nice gesture 😀\nTax: `{} Ð`'.format(ctx.author.id, final_amount,
                                                                                     give_to.id,
                                                                                     amount - final_amount))
        togiverbal = config_dict.get(give_to.id)
        newuserbal = cur_bal - amount
        giverbal = togiverbal + final_amount
        mynewdict = {ctx.author.id: newuserbal, give_to.id: giverbal}
        config_dict.update(mynewdict)
        update_book()

@bot.command(aliases=['bal'], pass_context=True)
async def balance(ctx, p_id=None):
    replies = ['Yo <@{id}>, You\'ve got `{currency} Ð`',
               '<@{id}> You have `{currency} Ð` in your account!',
               'Ah! So... <@{id}> has got `{currency} Ð` in there!']
    if ctx.channel.id in [795906303884525569, 796686187254513665]:
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


@bot.command(aliases=['g'])
async def gamble(ctx, price=None):
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
                dc = {_id: new_bal}
                config_dict.update(dc)
            else:
                await ctx.send('Damn! <@{id}> You just lost `{stake} Ð`. Sad? <:kekw:772091131596374017>'.format(id=_id,
                                                                                                                 stake=price))
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

from datetime import datetime
@bot.command()
async def add(ctx, person_id: int, amt: int):
    if dikemod in [y.id for y in ctx.author.roles]:
        current_bal = config_dict.get(person_id)
        new_bal = current_bal + amt
        dc = {person_id: new_bal}
        config_dict.update(dc)
        update_book()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        myfile = open('modlogs.txt', 'a+')
        myfile.write('{}: Used by: `{}` Amount: `{}`\n'.format(dt_string, ctx.author.name, amt))
        myfile.close()
        await ctx.send('Added `{} Ð` Successfully!'.format(amt))
    else:
        lol = ctx.author.id
        await ctx.send('<@{}> You dont have permission to use this command.'.format(lol))

@bot.command()
async def logs(ctx):
    if dikemod in [y.id for y in ctx.author.roles]:
        with open("modlogs.txt", "rb") as file:
            await ctx.author.send("Here is the logs file:", file=discord.File(file))


import job_print_bot
@bot.command()
async def job(ctx):
    clog='🟢  `1`- `Jumbled Words` 🔠\n' \
         '    Pay: `20 Ð`\n\n' \
         '🟢  `2`- `Memory Game` 🧠\n' \
         '    Pay: `50 Ð`\n\n' \
         '🔴  `3`- `Salesman` 🙋‍♂️\n' \
         '    Pay: `100 Ð` \n\n' \
         '🟢  `4`- `Hacking` 🕵️‍♂️\n' \
         '    Pay: `250 Ð`\n\n' \
         '🔴  `5`- `Bank Robbery` 🏦\n' \
         '    Pay: `25% of money + 1000 Ð`\n\n' \
         'The Jobs with 🟢 are available for now'

    embed = discord.Embed(title='Jobs Available:',
                         description=clog,
                         color=embedcolor)
    embed.set_footer(text='Reply with !apply <job number> to opt for a job')
    await ctx.send(embed=embed)


@bot.command()
async def setuphack(ctx):
    if ctx.author.id == 771601176155783198:
        mem = discord.utils.get(ctx.guild.channels, id=795906303884525569)
        print(mem.members)
        dicti = {}
        for user in mem.members:
            mydict = {
                user.id: {'comp': 'False', 'pc': 'False', 'vpn': 'False', 'esc': 0, 'qboard': 'False', 'trace': 0}}
            dicti.update(mydict)
            mydict.clear()
        await ctx.send('Hacking Config Done!')
        myf = open('hacking_data.txt', 'w')
        myf.write(str(dicti))
        myf.close()
    else:
        lol = ctx.author.id
        await ctx.send('<@{}> You ain\'t my master!'.format(lol))
        '''
