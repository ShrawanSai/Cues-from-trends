from django.shortcuts import render
from django.http import HttpResponse
import dashboard_table.src.retrieve_table



# Create your views here.
def home(request):

    
    context,df = dashboard_table.src.retrieve_table.retrieve()

    row = request.GET.get('row',0) 
    
    context['row'] = row

    
    display_row = df.loc[df['sno'] == int(row)]

    top_5 = list(df['title'])[:6]
    top_5_ids = list(df['sno'])[:6]

    top_5 = dict(zip(top_5, top_5_ids))

    
    
    title = list(display_row['title'])[0]
    type = list(display_row['type'])[0]
    popularity_score = list(display_row['popularity'])[0]
    popularity_score = str(popularity_score)[:5]
    related = list(display_row['related_topics'])[0]

    ########################################################
    tweets_d = list(display_row['tweets'])[0]
    try:
        if len(tweets_d) == 0:
            tweets_d = ['No Tweets Found']
    except:
        tweets_d = ['No Tweets Found']

    ########################################################
    reddits = list(display_row['reddits'])[0]
    try:
        if len(reddits) == 0:
            reddits = ['No Subreddits Found']
        else:
            reddits = reddits[:3]
    except:
        reddits = ['No Subreddits Found']
    ########################################################
    sentiment_score = list(display_row['sentiment'])[0]
    try:
        sentiment_score = str(int(sentiment_score))+'%'
    except:
        sentiment_score = 'Could not compute sentiment score'

    #######################################################
    text_cues = list(display_row['text_cues'])[0]
    try:
        if len(text_cues) == 0:
            text_cues = ['No Text Cues Found']
    except:
        text_cues = ['No Text Cues Found']



    context['title'] = title
    context['type'] = type
    context['popularity_score'] = popularity_score
    context['related'] = related
    context['tweets_d'] = tweets_d
    context['reddits'] = reddits
    context['sentiment_score'] = sentiment_score
    context['text_cues'] = text_cues

    context['top_5'] = top_5


    return render(request,'dashboard_table/home.html',context)
