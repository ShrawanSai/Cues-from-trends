# Cues-from-trends

https://cues-from-trends.herokuapp.com/

This reposotiry aims to extract and present text cues from trends.
Cues that can be used for creating new memes(meme captions), blogs, posts, tweets and even maybe one liners for tshirts.

The end result is to be a dashboard that displays the top and current trends, hashtags, topics, and how well are they recieved by the 
public.

### For example, 
At the time of editing this Read me file, 
a few current and trending topics are the US elections, Shah Rukh Khan's birthday, the Indian Premiere league (IPL) etc.

The final result would be something like

| Topic id   |      Topic      |  Type | Sentiment Score | Related topics | Text cues | Interest by region |
|----------|:-------------:|------:|------:|------:|------:|------:|
| 1 |  IPL | Cricket league | 89% | ipl live score, mumbai indians, virat kohli | MS Dhoni #DefinitelyNot, Virat❤️ | India, UAE, Australia|
| 2 |Shah Rukh Khan| Indian actor | 91% |  srk news,bollywood,birthday | Baadshah, ❤️SRK❤️, Burj Khalifa | India, UAE, Pakistan |
| 3 | US Elections | General election  | 43% | Trump,biden,congress | free world, God bless President @realDonaldTrump, Predictions | United states of America, Russia, UK |


Trends would be mined from soucres like Twitter, Google Trends, Instagram, Reddit etc after which finding a sentiment score for the same will be done

The step by step process for the entire pipeline is represented as seperate Ipynbs.

These are the steps and the notebooks Inused to solve the issue
1. Find trending topics from twitter for given location -  step-1 trending twitter topics.ipynb
2. Find the interest over time for the topic from trends - step-2 interest_over_time.ipynb
3. Find regions of interest, related topics, type from google trends - step-3 information from google trends.ipynb
4. Find tweets, reddit posts and their comments about each topic - step4a twitter text.ipynb, step4b reddit text.ipynb
5. Run Sentiment Analysis on the extracted text along with post statistics - step5 sentiment analysis.ipynb
6. Find Hashtags, Named Entities, Text with emojis etc from extracted text for text cues - step6.ipynb

The django project was built with the idea of automating the procedure and hosting the live project.
Once the django project has its cronjobs set up it is ready to be deployed on a full scale
For now, a non dynamic version of the app is up at https://cues-from-trends.herokuapp.com/

Here is a sample page:

Top trending:
![image](https://user-images.githubusercontent.com/36449863/142579072-dff8497c-c41f-4d2e-8e7e-e8cfa35d57b8.png)

List of all trending and option to select any card. AlongsideTracking and predicting the interest over time


![image](https://user-images.githubusercontent.com/36449863/142579144-f2c7ecc0-552b-42fb-b375-63363ebece59.png)

Related Topics and Tweets:


![image](https://user-images.githubusercontent.com/36449863/142579222-78d4b46c-de33-448a-aa85-7254ceb175cd.png)


Region wise popularity score and text cues
![image](https://user-images.githubusercontent.com/36449863/142579302-4a3df0c2-1470-4477-9349-ab249cf312bc.png)



