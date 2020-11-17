<p align="center"><a href="https://github.com/vsnz/Telegram-Airdrop-Bot" target="_blank"><img src="https://i.imgur.com/nYqDUX0.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/vsnz/Telegram-Airdrop-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/vsnz/Telegram-Airdrop-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/vsnz/Telegram-Airdrop-Bot/issues"><img src="https://img.shields.io/github/issues/vsnz/Telegram-Airdrop-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/vsnz/Telegram-Airdrop-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/vsnz/Telegram-Airdrop-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/vsnz/Telegram-Airdrop-Bot/stargazers"><img src="https://img.shields.io/github/stars/vsnz/Telegram-Airdrop-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/vsnz/Telegram-Airdrop-Bot/network/members"><img src="https://img.shields.io/github/forks/vsnz/Telegram-Airdrop-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/vsnz/Telegram-Airdrop-Bot/watchers"><img src="https://img.shields.io/github/watchers/vsnz/Telegram-Airdrop-Bot?style=social" alt="GitHub watchers"></a>
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


## Features
- Check if a correct ERC-20 address has been provided
- Set a max cap
- Each wallet address can only be submitted once
- Receive detailed notifications for new submissions
- Enable / disable the airdrop
- Admins can export the airdrop list by command (`/airdroplist`)

> 💡 Got a feature idea? Open an [issue](https://github.com/vsnz/Telegram-Airdrop-Bot/issues/new) and I might implement it.


## Installation
> ⚠️ Best to run the bot on a VPS. I can recommend [Hetzner](https://hetzner.cloud/?ref=tQ1NdT8zbfNY).
1. Log into MySQL (`sudo mysql`) and create a dedicated database and user with the following commands:
   1. `CREATE DATABASE TelegramAirdropBot;`
   1. `CREATE USER 'abuser'@'localhost' IDENTIFIED BY 'your-password';`
   1. `GRANT ALL PRIVILEGES ON TelegramAirdropBot . * TO 'abuser'@'localhost';`
   1. `exit;`
1. Clone this repository `git clone https://github.com/vsnz/Telegram-Airdrop-Bot.git`
1. Create your virtual environment `python3 -m venv Telegram-Airdrop-Bot`
1. Activate it `source Telegram-Airdrop-Bot/bin/activate && cd Telegram-Airdrop-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. Edit and update [`config.py`](https://github.com/vsnz/Telegram-Airdrop-Bot/blob/master/config.py)
1. Run the bot `python main.py`


## Images
![Telegram Airdrop Bot](https://i.imgur.com/00kB4AI.jpg)

## How can I help?
All kinds of contributions are welcome!
The most basic way to show your support is to `⭐️star` the project, or to raise [`🐞issues`](https://github.com/vsnz/Telegram-Airdrop-Bot/issues/new).