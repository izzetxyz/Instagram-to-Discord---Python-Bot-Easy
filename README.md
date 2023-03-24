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
- pip install request or pip3 install request
- pip install time or pip3 install time

## Usage:

1- Check https://developers.facebook.com/docs/instagram-basic-display-api/getting-started then https://developers.facebook.com/docs/instagram-basic-display-api/guides/long-lived-access-tokens (Don't forget to update your token every 60 days https://developers.facebook.com/docs/instagram-basic-display-api/guides/long-lived-access-tokens#refresh-a-long-lived-token)

Set the variables in config.py:
- Set USERNAME to Discord Bot Username
- Set WEBHOOK to Discord account webhook url. To know how, just Google: "how to create webhook discord".
- Set SLEEPTIME to the time in seconds in between each check for a new post.
- Set IGTOKEN Your Instagram Long-Lived Access Tokens https://developers.facebook.com/docs/instagram-basic-display-api/guides/long-lived-access-tokens?locale=en_US#get-a-long-lived-token
- Set IGUSER_ID Instagram User ID https://developers.facebook.com/docs/instagram-basic-display-api/getting-started#step-5--exchange-the-code-for-a-token

If your config is OK just do it and run your bot.

- py instagram-discord.py or python instagram-discord.py or python3 instagram-discord.py

