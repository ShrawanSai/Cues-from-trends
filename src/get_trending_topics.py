from tweepy import OAuthHandler
from tweepy import API

def get_trend_names():
    consumer_key="WNxuoNZkT2YfX65mio3eAvf8f"
    consumer_secret="QxhuS1xu6NxyfhiSErxTmhYgRgK8HupSPJzVhBWkSXIJEZ4hme"
    access_token="1071084889154310145-qYXNlTJtyne6iqaaaRDipyYWMR7wyh"
    access_token_secret="zjrmqthh0W7cYuVGjt7Uztgn6tgkzWZCUEhUob8m6CxKd"

    # Consumer key authentication(consumer_key,consumer_secret can be collected from our twitter developer profile)
    auth = OAuthHandler(consumer_key, consumer_secret)

    # Access key authentication(access_token,access_token_secret can be collected from our twitter developer profile)
    auth.set_access_token(access_token, access_token_secret)

    # Set up the API with the authentication handler
    api = API(auth)


    trends = api.trends_place(id=23424848) #india

    trends = trends[0]['trends']


    topics =set()
    hashtags = set()
    for topic in trends:
        #print(topic['name'])
        #len(s) == len(s.encode())
        if not len(topic['name']) == len(topic['name'].encode()):
            continue
        if topic['name'].startswith('#'):
            hashtags.add(topic['name'])
        else:
            topics.add(topic['name'])

    return hashtags,topics



