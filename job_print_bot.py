from discord_webhook import DiscordWebhook, DiscordEmbed

def job_list():
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

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/795963517361848321/cd7oTVM0niuX1ij3UAakIrMIH4oSmA5w2HWcaQDHHMgbmGaPY3HtRgjod5yYb4HeuUdt')

    embed = DiscordEmbed(title='Jobs Available:',
                         description=clog,
                         color=16776704)
    embed.set_footer(text='Reply with !apply <job number> to opt for a job')
    webhook.add_embed(embed)

    response = webhook.execute()