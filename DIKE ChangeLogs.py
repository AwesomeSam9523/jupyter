from discord_webhook import DiscordWebhook, DiscordEmbed

file = open('change.txt', 'r')
#clog = file.read()
file.close()

clog = '\n\n' \
       '**- Removed Music as it caused issues in the bot**\n' \
'- Added back Rythm in its place\n' \
'**- Added DIKE Arcade! It is below #general channel**\n' \
'- Added !help command to the bot\n' \
'**- Introduced New Discord Currency- Dikers (Ð). Can be earned through DIKE Arcade**\n'

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/795653622015983667/FA7-RBWYUjmLa1D7bzQMzV1eKdcOrYlIrM0MJMn7E5R4twTouo3Baw3VeObOUfHI7638')

embed = DiscordEmbed(title='DIKE Bot had an upgrade! v1.0.2',
                     description=clog,
                     color=16776704)
embed.set_footer(text='Bot by: AwesomeSam#0001')
webhook.add_embed(embed)

response = webhook.execute()