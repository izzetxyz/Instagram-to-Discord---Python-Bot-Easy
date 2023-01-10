import requests as rq
import json
import numpy as np
import logging
from datetime import datetime
import time
import config
headers = {
    "user-agent": "Instagram 219.0.0.12.117 Android",
    "content-type": "application/json",
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "access-control-allow-origin": "https://www.instagram.com",
    "access-control-expose-headers": "X-IG-Set-WWW-Claim",
    "alt-svc": '''h3=":443"; ma=86400'''
}

usernames = config.USERNAMES

def discord_webhook(url,full_name,mediaimage,text):
    '''
    Sends a test Discord webhook notification
    '''
       
    data = {
        "username": config.USERNAME,
        "avatar_url": config.AVATAR_URL,
        "embeds": [{
            "title": full_name +' | Shared New Post!',
            "url": url,
            "thumbnail": {"url": mediaimage},
            "description": '***'+text+'***',
            "color": int(config.COLOUR),
            "footer": {'text': 'made by izzy'},
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

def First_check(usernames):
    posts = []
    for profile in usernames:
        try:
            url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={profile}"
            print(url)
            html = rq.get(url=url,headers=headers)
            print(html.text)
            output = html.json()
            
            full_name = output['data']['user']['full_name']
            mediaimage = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['display_url']
            text = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            shortcode = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']
            posts.append('https://www.instagram.com/p/'+shortcode+' :'+full_name+' :'+mediaimage+' :'+text)
        except Exception as e:
            print('Missing username or something.')
    print('First Check Success!')
    return posts
def Second_check(usernames,firstpost):
    second_posts = []
    for profile in usernames:
        try:
            url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={profile}"
            html = rq.get(url=url,headers=headers)
            output = html.json()
            full_name = output['data']['user']['full_name']
            mediaimage = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['display_url']
            text = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            shortcode = output['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']
            second_posts.append('https://www.instagram.com/p/'+shortcode+' :'+full_name+' :'+mediaimage+' :'+text)
        except Exception as e:
            print('Missing username or something.')
            return firstpost
    if(np.array_equal(firstpost,second_posts)==False):
        filteredList = [second_posts for second_posts in second_posts if second_posts not in firstpost]
        i = 0
        for item in filteredList:
            discord_webhook(str(filteredList[i].split(' :')[0]),str(filteredList[i].split(' :')[1]),str(filteredList[i].split(' :')[2]),str(filteredList[i].split(' :')[3]))
            i += 1
        i = 0   
        firstpost = First_check(usernames)
        return firstpost
    print(datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')+'  |  No Changes in pages!')
    return firstpost


firstpost = First_check(usernames)


while True:
    time.sleep(config.SLEEPTIME)
    firstpost = Second_check(usernames,firstpost)

