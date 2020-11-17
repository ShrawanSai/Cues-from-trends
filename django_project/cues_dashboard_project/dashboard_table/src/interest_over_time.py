import re
import numpy as np
import time
import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
# curve-fit() function imported from scipy 
from scipy.optimize import curve_fit 

def func(t, c0,c1,c2,c3): 
    return c0+c1*t-c2*np.sin(-c3*t)

def no_of_days(x):
    temp = [(x[i]-x[0]).days for i in range(len(x))]
    return temp

def get_slope(x,param):
    slope = func(x[-1]+10,param[0],param[1],param[2],param[3]) - func(x[-1]+1,param[0],param[1],param[2],param[3])
    return slope

def pedict_next(x,param,y,n):
    
    y_n = np.empty(n)
    y_p = [func(i,param[0],param[1],param[2],param[3]) for i in x]
    
    xpred = [x[-1]+i for i in range(1,11)]
    ypred = [func(i,param[0],param[1],param[2],param[3]) for i in xpred]

    
    plt.plot(x,y,'b',label = 'Current Trend')
    plt.plot(x,y_p,'r', label = 'Fitted Curve')
    plt.plot(xpred,ypred,'r--', label = 'Prediction for next 10 days')
    plt.legend()


def trend_status(topic,pytrends, plot = False):
    kw_list = [topic]
    #print('passed 1' )
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='IN', gprop='')
    #print('passed 2')
    interest = pytrends.interest_over_time().tail(5)
    
    interest = interest[interest.columns[0]]
    
    x = no_of_days(list(interest.index))
    y = list(interest)
    n = len(x)

    guess = [100,0.01,100,0.01]
    
    param, param_cov = curve_fit(func, x, y,guess,maxfev = 100000) 
    
    slope = get_slope(x,param)
    
    if plot:
        pedict_next(x,param,y,n)
    
    return slope


def get_iot(hashtags,topics,pytrends):

    
    twitter_stuff = hashtags.union(topics)
    #print(twitter_stuff)

    df = pytrends.top_charts(2019, hl='en-US', tz=300, geo='IN')

    all_topics = twitter_stuff.union(set(list(df['title'])))
    all_topics = list(all_topics)
    #print(all_topics)

    popularity = {}

    for title in all_topics:
        
        temp = title
        if title.startswith('#'):
            title = title[1:]
            title = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', title)
            if len(title)<1: 
                continue
            title = ' '.join(title)
        try:
            slope = trend_status(title,pytrends)
            popularity[temp] = slope
        except Exception as e:
            #print(e)
            pass
        #time.sleep(2)


    popularity_db = pd.DataFrame(popularity.items())
    #print(popularity_db)
    popularity_db.columns = ['title','popularity']


    scaler = MinMaxScaler()
    popularity_db['popularity'] = scaler.fit_transform(popularity_db['popularity'].values.reshape(-1,1))

    popularity_db.sort_values(by = 'popularity', ascending=False, inplace=True)

    popularity_db.reset_index(inplace=True)
    popularity_db['popularity'] = popularity_db['popularity']*100

    db_len = len(popularity_db)

    popularity_db = popularity_db[['title','popularity']]

    popularity_db.at[0, 'popularity'] = popularity_db.at[0, 'popularity'] - 1
    popularity_db.at[db_len-1, 'popularity'] = popularity_db.at[db_len-1, 'popularity'] + 1

    return popularity_db


