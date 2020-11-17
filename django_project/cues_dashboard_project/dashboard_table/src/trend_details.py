import re
import numpy as np
import time
import pandas as pd                        
from pytrends.request import TrendReq


def get_details_of_topic(df,pytrends):

    #pytrends = TrendReq(hl='en-US', tz=530, timeout=(10,25), retries=2, backoff_factor=0.1)

    titletype = {}
    for topic in df['title']:
        keywords = pytrends.suggestions(keyword=topic)
        #print(keywords)
        try:
            
            if not topic.startswith('hashtag'):
                title = keywords[0]['title']
            else:
                title = topic
            type_of = keywords[0]['type']
        except IndexError:
            title = topic
            type_of = 'hashtag'
        titletype[topic] = type_of

    df['Type'] = df['title'].map(titletype)

    titles = df['title']

    related_titles = {}
    hashtags = []

    for title in titles:
        if title.startswith('#'):
            hasht = title
            hashtags.append(title)
            title = title[1:]
            title = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', title)
            if len(title)<1: 
                continue
            title = ' '.join(title)
            try:
                pytrends.build_payload(kw_list=[title])
                #print(title)
                related_topic = pytrends.related_topics()
                related = list(related_topic[list(related_topic.keys())[0]]['rising']['topic_title'])
                related_titles.update({hasht: related[:4]})
            except Exception as e:
                print(title)
        else:
            try:
                pytrends.build_payload(kw_list=[title])
                #print(title)
                related_topic = pytrends.related_topics()
                related = list(related_topic[list(related_topic.keys())[0]]['rising']['topic_title'])
                related_titles.update({title: related[:4]})
            except Exception as e:
                #print(e)
                pass
                #print(title,related_topic)
    
    df['Related Topics'] = df['title'].map(related_titles)


    regions_of_interest = {}

    for title in titles:
        hasht = title
        if title.startswith('#'):
            hasht = title
            title = title[1:]
            title = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', title)
            if len(title)<1: 
                continue
            title = ' '.join(title)
            
        
        kw_list = [title]
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='IN', gprop='')
        regions = pytrends.interest_by_region(resolution='DMA', inc_low_vol=True, inc_geo_code=False)
        regions['region'] = regions.index
        regions = regions.to_numpy()
        regions = sorted(regions, key=lambda regions: regions[0]) [::-1]
        
        regions_of_interest.update({hasht:regions})

            
        print(title)
        time.sleep(5)


    df['regions_of_interest'] = df['title'].map(regions_of_interest)

    
    return df

