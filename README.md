<p align="center"><a href="https://github.com/fabston/Telegram-Airdrop-Bot" target="_blank"><img src="https://github.com/fabston/Telegram-Airdrop-Bot/blob/main/assets/logo.png?raw=true"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/fabston/Telegram-Airdrop-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/fabston/Telegram-Airdrop-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/fabston/Telegram-Airdrop-Bot/issues"><img src="https://img.shields.io/github/issues/fabston/Telegram-Airdrop-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/fabston/Telegram-Airdrop-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/fabston/Telegram-Airdrop-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/fabston/Telegram-Airdrop-Bot/stargazers"><img src="https://img.shields.io/github/stars/fabston/Telegram-Airdrop-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/fabston/Telegram-Airdrop-Bot/network/members"><img src="https://img.shields.io/github/forks/fabston/Telegram-Airdrop-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/fabston/Telegram-Airdrop-Bot/watchers"><img src="https://img.shields.io/github/watchers/fabston/Telegram-Airdrop-Bot?style=social" alt="GitHub watchers"></a>
</p>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#images">Images</a>
  •
  <a href="#how-can-i-help">Help</a>
</p>

## About
The **Telegram Airdrop Bot** 💰 helps you to manage your airdrops on ERC-20, BEP-20 etc. tokens.

### 🚀 Pro Version
The pro version is hosted on my server and includes features such as:

- Referral System
- Captcha Support
- Checks if the user joined a Telegram Group/Channel
- Export the airdrop list in CSV format

If you are interested message me on Telegram [@fabston](https://t.me/fabston). 

> _Don't DM me if you are having issue setting up the bot, instead open an [issue](https://github.com/fabston/Telegram-Airdrop-Bot/issues/new/choose)!_

## Features
- Check if the wallet length is correct
- Set a max cap
- Each wallet address can only be submitted once
- Users can change their wallet address after submission  
- Receive detailed notifications for new submissions
- Enable / disable the airdrop
- Admins can export the airdrop list by command (`/airdroplist`)

> 💡 Got a feature idea? Open an [issue](https://github.com/fabston/Telegram-Airdrop-Bot/issues/new?assignees=&labels=enhancement&template=feature-request---.md) and I might implement it.


## Installation
> ⚠️ Best to run the bot on a VPS. I can recommend <a href="https://hetzner.cloud/?ref=tQ1NdT8zbfNY" title="Get €20 in cloud credits">Hetzner</a>'s CX11 VPS for 2.89€/month. [Sign up](https://fabston.dev/hetzner) now and receive **€20 free** credits.
1. Log into MySQL (`sudo mysql`) and create a dedicated database and user with the following commands:
   1. `CREATE DATABASE TelegramAirdropBot;`
   1. `CREATE USER 'AirdropUser'@'localhost' IDENTIFIED BY '<YOUR PASSWORD>';`
   1. `GRANT ALL PRIVILEGES ON TelegramAirdropBot . * TO 'AirdropUser'@'localhost';`
   1. `exit;`
1. Clone this repository `git clone https://github.com/fabston/Telegram-Airdrop-Bot.git`
1. Create your virtual environment `python3 -m venv Telegram-Airdrop-Bot`
1. Activate it `source Telegram-Airdrop-Bot/bin/activate && cd Telegram-Airdrop-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. The bot runs behind a webhook, so you have to create a SSL cert first:
   1. `openssl genrsa -out webhook_pkey.pem 2048`
   1. `openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem`
      1. _When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply with your server ip._
1. Edit and update [`config.py`](https://github.com/fabston/Telegram-Airdrop-Bot/blob/master/config.py)
1. Run the bot `python main.py`


## Images
![Telegram Airdrop Bot](https://github.com/fabston/Telegram-Airdrop-Bot/blob/main/assets/about.jpg?raw=true)

## How can I help?
All kinds of contributions are welcome 🙌! The most basic way to show your support is to `⭐️ star` the project, or raise [`🐞 issues`](https://github.com/fabston/Telegram-Airdrop-Bot/issues/new/choose).

***

<p align="center">
    <a href="https://www.buymeacoffee.com/fabston"><img alt="Buy Me A Coffee" title="☕️" src="https://github.com/fabston/Telegram-Airdrop-Bot/blob/main/assets/bmac.png?raw=true" width=200px></a>
</p>