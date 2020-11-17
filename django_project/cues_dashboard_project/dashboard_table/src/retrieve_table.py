import pandas as pd
import numpy as np
import json 
import os
def retrieve():
    #df = pd.read_csv('C:/Users/msais/Desktop/Cues/django_project/cues_dashboard_project/dashboard_table/src/final_sumission.csv')
    #df = pd.DataFrame({'a': [12, 3, 4], 'b': [5, 6, 7]})
    
    file_name = os.path.join(os.getcwd(),'dashboard_table','src','final_ans.pkl')
    df = pd.read_pickle(file_name)
    df.insert(0, 'sno', df.index)
    df.columns = ['sno','title','popularity','type','related_topics','roi','tweets','reddits','sentiment','text_cues']

    #df['related_topics'] = df['related_topics'].apply(lambda x: list(x))

    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}


    return context,df