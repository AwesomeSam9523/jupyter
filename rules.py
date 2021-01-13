from discord_webhook import DiscordWebhook, DiscordEmbed

def rules_print(n):
    if n == 1:
        clog='If you witness someone breaking ANY of these rules please contact any active Moderator/Admib immediately with proof!\n' \
             '**[1] Discord Terms of Service and Community Guidelines, as well Krunker\'s Terms & Conditions apply to this server**\n' \
             '- You must follow both of these in order to stay in the server! If you\'re caught breaking them you will be removed\n' \
             '**[2] Account Trading or Selling**\n' \
             '- If you\'re caught attempting to sell accounts you will be removed from the server!\n' \
             '**[3] Communicate using English only**\n' \
             '- All other languages in #regional-chat.\n' \
             '- Communicate in English around the server, even in Pickups Chat.\n' \
             '**[4] No Self Promotion or Advertisement**\n' \
             '- DM an admin to get Content Creator role, this will allow you to Promote your Twitch/Youtube in #video-or-streams. Otherwise any Self Promotion or Advertisement will be removed and you will be punished!\n' \
             '**[5] Use an appropriate Name and Profile Picture**\n' \
             '- Avoid any Special Characters and Emojis.\n' \
             '- There must be at least 3 standard characters in your nickname, so that you can be pinged.\n' \
             '**[6] No Personal Information**\n' \
             '- Protect your privacy and the privacy of others.\n' \
             '- Don\'t reveal any personal info of others without their prior consent.'
    else:
        clog = '**[7] No Political or Religious topics**\n' \
               '- We do not want to offend any users on the server so please stay away from these topics.\n' \
               '- Religious topics includes racial slurs.\n' \
               '- No swearing or being toxic against a specific nationality.\n' \
               '**[8] Use common sense.**\n' \
               '- Attempting to use loopholes/bypasses can result in a larger punishment.\n' \
               '**[9] No Harassing, Abusing, or Bullying**\n' \
               '- We have zero-tolerance for harming others.\n' \
               '- Jokes may be let off depending on the severity.\n' \
               '**[10] Do not spam**\n' \
               '- Avoid excessive messages, images, formatting, emojis, commands, and @mentions.\n' \
               '- Avoid Ghost Pinging, if you do so by accident let the pinged user know.\n' \
               '**[11] No bypassing banned words**\n' \
               '- Bypassing banned words will result in a Mute even if it was deleted.\n' \
               '**[12] No hackusating**\n' \
               '- DM a staff member with adequate proof.\n' \
               '- Don\'t accuse another person of hacks in public chats.\n' \
               '**[13] Don\'t disobey staff**\n' \
               '- When asked to stop, stop.\n' \
               '**[14] Do Not DM any Staff Members until asked**\n' \
               '-Do not DM any Admin/Mod for any reason whatsoever, until asked, even if they are active in chat.\n' \
               '- Violation of this rule will lead to a irrevocable mute of 12 hours which will be incremented to kick/ban if you are found guilty again.'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/798811828351795231/b1CqgT_VrYZ3acJxFuEUY4jLGpi_aodn99peuWWlrqj0QQ6UEKxO-GQZzZfsUaUyV5f0')

    embed = DiscordEmbed(title='Server Rules',
                         description=clog,
                         color=16776704)
    embed.set_footer(text='Bot by: AwesomeSam#9523')
    webhook.add_embed(embed)

    response = webhook.execute()