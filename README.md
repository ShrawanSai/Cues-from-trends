# Cues-from-trends

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
