import matplotlib.pyplot as plt
import base64
import pandas as pd
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(vals,title):

    [x,y] = vals['ct']
    [x,y_p] = vals['ft']
    [xpred,ypred] = vals['pred']

    plt.switch_backend('AGG')
    plt.figure(figsize=(7,5))
    plt.title(f'Interest over time for: {title}')

    plt.plot(x,y,'b',label = 'Current Trend')
    plt.plot(x,y_p,'r', label = 'Fitted Curve')
    plt.plot(xpred,ypred,'r--', label = 'Prediction for next 10 days')

    plt.legend()
    plt.xticks(rotation = 45)
    plt.xlabel('Time in Days')
    plt.ylabel('Popularity Score')
    plt.xlabel('Time in Days')
    plt.ylabel('Popularity Score')

    graph = get_graph()
    return graph

def get_indian_state_graph(rois,title):

    plt.switch_backend('AGG')
    plt.figure(figsize=(10,6))
    plt.title(f'{title}, was most searched for in these states')

    y = [i[0] for i in rois]
    x = [i[1] for i in rois]

    plt.bar(x,y)

    plt.xlabel('State')
    plt.ylabel('Popularity Score')

    plt.xticks(rotation = 15)
    graph = get_graph()
    return graph


    