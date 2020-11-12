import numpy as np
import tweepy

from datetime import datetime, timedelta
import time

from tweepy import OAuthHandler
from tweepy import API


def listener_for_tweets(df):

    consumer_key="pCx9D6iouX8za05ijzYGTP7aA"
    consumer_secret="usevYFDTLePAwkjRtFdLcIoFbFdtZM4mGygkUpOsC1slvMQVjY"
    access_key="1071084889154310145-PW13NCjmNLWtk5i8YPckRRnhIgcUD0"
    access_secret="UapYLhcTiZ77ztOLqsfe1eCAZMBSpo85NORHq9nNwY2XK"

    class TwitterStreamListener(tweepy.streaming.StreamListener):
    
        count = 0
        tweets = set()

        
        ''' Handles data received from the stream. '''
        

            
        def get_ready(self):
            TwitterStreamListener.count = 0
            TwitterStreamListener.end_time = 0
            TwitterStreamListener.tweets = set()

            
        def on_status(self, status):
            
            #print(f'ID: {status.id}')
            #print(f'Username: {status.user.name}')
            #print(datetime.today())
            

            
            days_old = (datetime.today() - status.created_at).days
            favorites = status.favorite_count
            lang = status.lang
            retweet_count = status.retweet_count
            
            
            if days_old<30 and lang == 'en':
                TwitterStreamListener.tweets.add(status.text)
                TwitterStreamListener.count += 1
            if TwitterStreamListener.count >=5:
                return False
            
            return True

        def on_error(self, status_code):
            print('Got an error with status code: ' + str(status_code))
            if int(status_code) == 420:
                print('sleeping')
                time.sleep(5)
            return True # To continue listening

        def on_timeout(self):
            print('Timeout...')
            return False # To break listening

    listener = TwitterStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    def scrape_tweets(keyword):
        listener.get_ready()
        stream = tweepy.streaming.Stream(auth, listener,timeout=15)
        stream.filter(track=[keyword])
        return list(listener.tweets)
    


    mapping = {}
    c = 1
    for title in df['title']:
        hasht = title
        if c!=1:
            time.sleep(3)
        if c%7 == 0:
            #print('sleeping')
            time.sleep(5)
        #print(title)
        try:
            t = scrape_tweets(title)
        except Exception as e:
            #print(e)
            t = []
        #print( f'Found {len(t)} tweets')
        c += 1
        #print('done searching')
        
        if len(t)<1:
            continue
           
            
        mapping.update({hasht:t})

    df['Tweets'] = df['title'].map(mapping)

    return df





