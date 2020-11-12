import praw
import pandas as pd

def scrape_reddit(df):

    client_id = 'DvckE0IdkAyvcw'
    client_secret = 'DqKfsZFjq2Rnl0aHypyoMIMYN60b3Q'
    user_agent = 'CuesFromTrends'

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    mapping = {}
    for title in df['title']:
        t = title
        if title.startswith('#'):
            title = title[:1]
        else:
            title = title.split()
            title = [i.capitalize() for i in title]
            title = ''.join(title)
        try:
            hot_posts = list(reddit.subreddit(title).hot(limit=10))
        except:
            hot_posts = []
        if len(hot_posts) <= 4:
            try:
                top_posts = list(reddit.subreddit(title).top(limit = 10))
                hot_posts += top_posts
            except:
                hot_posts = []
            if len(hot_posts) <=4:
                try:
                    new_posts = list(reddit.subreddit(title).new(limit = 10))
                    hot_posts += new_posts
                except:
                    hot_posts = []
        subs = []
        if len(hot_posts) == 0:
            continue
        for post in hot_posts:
            if not post.stickied:
                subs.append(post.title + '\n' + post.selftext)
                
        mapping.update({t:subs})
    df['Reddit_Posts'] = df['title'].map(mapping)
    return df
