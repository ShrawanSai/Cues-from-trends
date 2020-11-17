import pandas as pd 
from pytrends.request import TrendReq
import get_trending_topics
import interest_over_time
import trend_details
import reddit_scrapper
import twitter_listener
import get_sentiment
import text_cues
import time
import os

def start_main(path_to_save_to):
    #start_time = time.time()
    try:
        pytrends = TrendReq(hl='en-US', tz=530, timeout=(10,25), retries=2, backoff_factor=0.1)


        hashtags,topics = get_trending_topics.get_trend_names()

        df = interest_over_time.get_iot(hashtags,topics,pytrends)
        print('Step 1 up, entering step 2')

        df = trend_details.get_details_of_topic(df,pytrends)
        print('Step 2 up, entering step 3')

        df = twitter_listener.listener_for_tweets(df)
        print('Step 3 up, entering step 4')

        df = reddit_scrapper.scrape_reddit(df)
        print('Step 4 up, entering step 5')

        df = get_sentiment.get_sentiment(df)
        print('Step 5 up, entering step 6')

        df = text_cues.get_all_text_cues(df)
        print('Step 6 up')


        df.to_pickle(os.path.join(path_to_save_to,'final_ans.pkl'))

        return True
    except:
        return False



