# Instagram to discord post images
![1*cXNgzu0Pvj4HwOLw4Akwqg](https://markb4.files.wordpress.com/2021/01/discordinstagram.png?w=640)

<p align="center">
  <a href="https://www.instagram.com/">Instagram To Discord</a>
  <br/>
  Easiest to use instagram to discord bot with Python.
</p>
<br/>
This script executes 2 actions:

1. Monitors for new image posted in a instagram account.
2. If found new image, a bot posts new instagram image in a discord channel.
3. Repeat after set interval.

## Requirements:

- Python v3
- Python module re, json, requests,config,time,numpy
- pip install numpy or pip3 install numpy
- pip install request or pip3 install request
- pip install config or pip3 install config
- pip install time or pip3 install time

## Usage:

Set environment variables in config:
- Set USERNAME to Discord Bot Username. Example: Izzy Bot
- Set AVATAR_URL to Discord Bot Photo. Example: (https://cdn.pixabay.com/photo/2022/04/01/20/37/moon-7105626_640.jpg)
- Set USERNAMES to usernames accounts you want to monitor. Example: ['nike','adidas']
- Set WEBHOOK to Discord account webhook url. To know how, just Google: "how to create webhook discord".
- Set SLEEPTIME to the time in seconds in between each check for a new post. 600 is 10 minutes The time you recommend is 10 minutes per account 2 account 20 minutes. Using otherwise, you will exceed the Instagram limit and you will have to wait for a while.

If your config is okey just do it and run your bot.

- py instagramtodiscord.py or python instagramtodiscord.py or python3 instagramtodiscord.py


## Collaborations:

Easiest to use instagram to discord bot.
