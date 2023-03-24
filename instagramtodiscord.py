import requests as rq
import json
import logging
from datetime import datetime
import time
import config


token = config.IGTOKEN
user_id = config.IGUSER_ID


def discord_webhook(url,full_name,mediaimage,text):
    '''
    Sends a test Discord webhook notification
    '''
       
    data = {
        "username": config.USERNAME,
        "embeds": [{
            "title": full_name +' | Shared New Post!',
            "url": url,
            "image": {"url": mediaimage},
            "description": '***'+text+'***',
            "color": config.COLOUR,
            "footer": {'text': 'made by KhalidM'},
            "timestamp": str(datetime.utcnow()),          
    }]
    }
    result = rq.post(config.WEBHOOK, data=json.dumps(data), headers={"Content-Type": "application/json"})
    
    try:
        result.raise_for_status()
    except rq.exceptions.HTTPError as err:
        logging.error(msg=err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        logging.info(msg="Payload delivered successfully, code {}.".format(result.status_code))


def First_check():
    posts = []
    try:
        time.sleep(5)
        url = f"https://graph.instagram.com/me/media?fields={user_id},caption&access_token={token}"
        html = rq.get(url=url)
        output = html.json()       
        full_name = "" #### Set The Full Name of The IG Account
        mediaid = output['data'][0]['id']
        text = output['data'][0]['caption']
        url = f"https://graph.instagram.com/{mediaid}?fields=id,media_type,media_url,username,timestamp,permalink&access_token={token}"
        html = rq.get(url=url)
        output = html.json()   
        mediaimage = output["media_url"]
        shortcode = output['permalink']
        posts.append(shortcode+' :'+full_name+' :'+mediaimage+' :'+text)
    except Exception as e:
        print('Missing username or something.')
    print('First Check Success!')
    return posts


def Second_check(firstpost):
    second_posts = []
    try:
        time.sleep(5)
        url = f"https://graph.instagram.com/me/media?fields={user_id},caption&access_token={token}"
        html = rq.get(url=url)
        output = html.json()       
        full_name = "" #### Set The Full Name of The IG Account
        mediaid = output['data'][0]['id']
        text = output['data'][0]['caption']
        url = f"https://graph.instagram.com/{mediaid}?fields=id,media_type,media_url,username,timestamp,permalink&access_token={token}"
        html = rq.get(url=url)
        output = html.json()   
        mediaimage = output["media_url"]
        shortcode = output['permalink']
        second_posts.append(shortcode+' :'+full_name+' :'+mediaimage+' :'+text)
    except Exception as e:
        print('Missing username or something.')
        return firstpost
    if firstpost[0].split()[0] != second_posts[0].split()[0]:
        filteredList = [second_posts for second_posts in second_posts if second_posts not in firstpost]
        i = 0
        for item in filteredList:
            discord_webhook(str(filteredList[i].split(' :')[0]),str(filteredList[i].split(' :')[1]),str(filteredList[i].split(' :')[2]),str(filteredList[i].split(' :')[3]))
            i += 1
        i = 0   
        firstpost = First_check()
        return firstpost
    print(datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')+'  |  No Changes in pages!')
    return firstpost


firstpost = First_check()


while True:
    time.sleep(config.SLEEPTIME)
    firstpost = Second_check(firstpost)
