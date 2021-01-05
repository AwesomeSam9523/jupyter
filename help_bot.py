from discord_webhook import DiscordWebhook, DiscordEmbed

def help_list():
    clog= '`1` --> `Apply to DIKE`\n\n' \
          '`2` --> `Arcade Commands`\n\n\n' \
          '**Type `!help <number>` to get info**'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/795963517361848321/cd7oTVM0niuX1ij3UAakIrMIH4oSmA5w2HWcaQDHHMgbmGaPY3HtRgjod5yYb4HeuUdt')


    embed = DiscordEmbed(title='DIKE Official Bot Help:',
                         description=clog,
                         color=16776704)
    embed.set_footer(text='Bot by: AwesomeSam#0001')
    webhook.add_embed(embed)

    response = webhook.execute()

def help_1():
    clog = 'Here are the minimum requirements:\n' \
           '```python\n' \
           '"--> Level:  30"\n' \
           '"--> KDR:   1.5"\n' \
           '"--> SPK:   100"\n' \
           '"--> KPG:    10"\n' \
           '"--> Nukes:   5"```'

    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/795963517361848321/cd7oTVM0niuX1ij3UAakIrMIH4oSmA5w2HWcaQDHHMgbmGaPY3HtRgjod5yYb4HeuUdt')

    embed = DiscordEmbed(title='DIKE Official Bot Help:',
                         description=clog,
                         color=16776704)
    embed.set_footer(text='Bot by: AwesomeSam#0001')
    webhook.add_embed(embed)

    response = webhook.execute()

def help_2():
    clog = 'Here are all the Arcade Commands!\n' \
           '```python\n' \
           '"--> !balance/!bal - View Balance"\n' \
           '"--> !gamble/!g    - Gamble to gain (or lose?) 50-50 Chances"\n' \
           '"--> !job          - Take up small tasks to gain Dikers!"\n' \
           '"--> !apply        - Apply for a particular job"\n' \
           '"--> !help         - View help"```'

    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/795963517361848321/cd7oTVM0niuX1ij3UAakIrMIH4oSmA5w2HWcaQDHHMgbmGaPY3HtRgjod5yYb4HeuUdt')

    embed = DiscordEmbed(title='DIKE Official Bot Help:',
                         description=clog,
                         color=16776704)
    embed.set_footer(text='Bot by: AwesomeSam#0001')
    webhook.add_embed(embed)

    response = webhook.execute()