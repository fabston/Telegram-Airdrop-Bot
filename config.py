# --------------------------------------------- #
# Plugin Name           : TelegramAirdropBot    #
# Author Name           : vsnz                  #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Telegram
token           = '<YOUR BOT TOKEN>'        # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot
log_channel     = 0                         # Channel ID. Example: -1001355597767
admins          = []                        # Telegram User ID's. Admins are able to execute command "/airdroplist"
airdrop_cap     = 100                       # Max airdrop submissions that are being accepted

# MySQL Database
mysql_host = 'localhost'
mysql_db   = 'TelegramAirdropBot'
mysql_user = 'abuser'
mysql_pw   = '<YOUR PASSWORD>'

texts = {
    'start_1': 'Hi {} and welcome to our Airdrop!\n\nGet started by clicking the button below.\n\n',
    'start_2': 'Hi {},\n\nYour address has been added to the airdrop list!\n\n',
    'airdrop_start': 'The airdrop didn\'t start yet.',
    'airdrop_address': 'Type in your $ETH address:',
    'airdrop_max_cap': 'ℹ️ The airdrop reached its max cap.',
    'airdrop_walletused': '⚠️ That address has already been used. Use a different one.',
    'airdrop_confirmation': '✅ Your address has been added to airdrop list.',
}