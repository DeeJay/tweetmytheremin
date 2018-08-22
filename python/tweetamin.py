from twython import TwythonStreamer
from time import sleep
#import pandas as pd
import re
import time
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            notelist = get_number(data['text'])
            print(notelist)
            sender.send_message('/play_this', notelist)
            print("done")

#Insert your auth keys
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

def get_number(mostrecent):
    result = re.findall(r'\d+',mostrecent)
    return [int(x) for x in result]

#getTweets()

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_key,
    access_secret
)
print("Ready...")
stream.statuses.filter(track='#tweetmytheremin')
