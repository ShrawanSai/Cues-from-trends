import pandas as pd 
from pytrends.request import TrendReq
from dashboard_table.src.get_trending_topics import get_trend_names
from dashboard_table.src.interest_over_time import get_iot
from dashboard_table.src.trend_details import get_details_of_topic
from dashboard_table.src.reddit_scrapper import scrape_reddit
from dashboard_table.src.twitter_listener import listener_for_tweets
from dashboard_table.src.get_sentiment import get_sentiment
from dashboard_table.src.text_cues import get_all_text_cues
import time
import os



def start_main(path_to_save_to):
    #start_time = time.time()
    print('gg')
    with open(os.path.join(path_to_save_to,'test.txt'),'w') as f:
        f.write('working')

    try:
        pytrends = TrendReq(hl='en-US', tz=530, timeout=(10,25), retries=2, backoff_factor=0.1)


        hashtags,topics = get_trend_names()

        df = get_iot(hashtags,topics,pytrends)
        print('Step 1 up, entering step 2')

        df = get_details_of_topic(df,pytrends)
        print('Step 2 up, entering step 3')

        df = listener_for_tweets(df)
        print('Step 3 up, entering step 4')

        df = scrape_reddit(df)
        print('Step 4 up, entering step 5')

        df = get_sentiment(df)
        print('Step 5 up, entering step 6')

        df = get_all_text_cues(df)
        print('Step 6 up')


        df.to_pickle(os.path.join(path_to_save_to,'final_ans.pkl'))

        return True
    except:
        return False



