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


<!DOCTYPE html>
<!-- saved from url=(0045)https://cues-from-trends.herokuapp.com/?row=4 -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
<title>Trends</title> 
 
<meta name="viewport" content="width=device-width, initial-scale=1"> 
<link rel="stylesheet" href="./Trends_files/bootstrap.min.css"> 
<script src="./Trends_files/jquery.min.js.download"></script> 
<script src="./Trends_files/popper.min.js.download"></script> 
<script src="./Trends_files/bootstrap.min.js.download"></script> 

</head> 
<body style="background-color: black;" class="vsc-initialized"> 


<h2 class="display-1 text-white">Top 5 Trending Topics in India: </h2>
<br><br>
<h4 class="display-1 text-white">Last updated at : 29/12/2020 20:53:51 </h4>

<div class="row"> 
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">#SnowFlowerTaehyung</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=0" class="card-link">View</a>
      </div>
    </div>
  </div>
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">YEONJUN</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=1" class="card-link">View</a>
      </div>
    </div>
  </div>
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">#VarunTej</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=2" class="card-link">View</a>
      </div>
    </div>
  </div>
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">Sony</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=3" class="card-link">View</a>
      </div>
    </div>
  </div>
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">#Rajinikanth</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=4" class="card-link">View</a>
      </div>
    </div>
  </div>
  
  <div class="col-sm-2">
    <div class="card text-center text-white bg-dark mb-3">
      <div class="card-body">
        <h5 class="card-title">#TaehyungOnBurjKhalifa</h5>
        <a href="https://cues-from-trends.herokuapp.com/?row=5" class="card-link">View</a>
      </div>
    </div>
  </div>
  

</div>

<br>


<div class="modal-body row">
  <div class="col-md-7">
    <br><br>
  <h2 class="text-center  text-white"><u>All Trending Topics</u></h2><br>			 
  <table class="table table-dark table-striped table-hover table-responsive scrollbar-colored" style="max-height: 1250px; overflow: scroll "> 
    <thead class="thead-dark"> 
    <tr> 
      <th class="text-center">Topic Title</th> 
      <th class="text-center">Popularity Score</th>
      <th class="text-center">Type</th> 
      <th class="text-center">Related Topics</th>
      <th class="text-center">Sentiment Score</th> 
    </tr> 
    </thead> 

    <tbody> 
    <!-- jinja2 Technique -->
     
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=0">#SnowFlowerTaehyung</a></td> 
      <td class="text-center">99.0%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
      </td> 
      <td class="text-center">59.4</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=1">YEONJUN</a></td> 
      <td class="text-center">54.1542582175%</td> 
      <td class="text-center">South Korean singer</td> 
      
      <td class="text-center">
        
          Yeonjun,
        
          TOMORROW X TOGETHER,
        
          Soobin,
        
          BTS,
        
      </td> 
      <td class="text-center">11.0808080808</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=2">#VarunTej</a></td> 
      <td class="text-center">44.3194631119%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Tholi Prema,
        
          Fidaa,
        
          Sai Pallavi,
        
          Gaddalakonda Ganesh,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=3">Sony</a></td> 
      <td class="text-center">38.767161511%</td> 
      <td class="text-center">Multinational conglomerate company</td> 
      
      <td class="text-center">
        
          Sony Xperia XA1 Plus,
        
          Sony Xperia XA,
        
          Job hunting,
        
          Binance,
        
      </td> 
      <td class="text-center">39.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=4">#Rajinikanth</a></td> 
      <td class="text-center">38.6609122979%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Kaala,
        
          Petta,
        
          Darbar,
        
          Bear Grylls,
        
      </td> 
      <td class="text-center">6.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=5">#TaehyungOnBurjKhalifa</a></td> 
      <td class="text-center">37.6500064355%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
      </td> 
      <td class="text-center">22.1590909091</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=6">Musical</a></td> 
      <td class="text-center">36.8840508238%</td> 
      <td class="text-center">Topic</td> 
      
      <td class="text-center">
        
          Musical.ly,
        
          Jal tarang,
        
          Hemantkumar Musical Group,
        
          High School Musical: The Musical: The Series,
        
      </td> 
      <td class="text-center">-2.1166666667</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=7">#NanhaFarishta</a></td> 
      <td class="text-center">36.1004204946%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Casting,
        
      </td> 
      <td class="text-center">5.2833333333</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=8">#Srinagar</a></td> 
      <td class="text-center">35.6583897865%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Cluster University Srinagar,
        
          GD Goenka School,
        
          Fajr prayer,
        
          Salah,
        
      </td> 
      <td class="text-center">22.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=9">Diego Costa</a></td> 
      <td class="text-center">34.3959850422%</td> 
      <td class="text-center">Footballer</td> 
      
      <td class="text-center">
        
          2018 World Cup,
        
          Diego Maradona,
        
          Romelu Lukaku,
        
          Portugal national football team,
        
      </td> 
      <td class="text-center">4.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=10">Captain Marvel</a></td> 
      <td class="text-center">31.900351694%</td> 
      <td class="text-center">Film</td> 
      
      <td class="text-center">
        
          Brie Larson,
        
          Box office,
        
          Blu-ray disc,
        
          Magnet URI scheme,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=11">Patna</a></td> 
      <td class="text-center">31.6757179528%</td> 
      <td class="text-center">City in India</td> 
      
      <td class="text-center">
        
          Patna Pirates,
        
          Patliputra Junction,
        
          VIVO Pro Kabaddi,
        
          Patna Women’s College,
        
      </td> 
      <td class="text-center">2.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=12">Joker</a></td> 
      <td class="text-center">31.342629905%</td> 
      <td class="text-center">Character</td> 
      
      <td class="text-center">
        
          Joaquin Phoenix,
        
          War,
        
          It,
        
          It Chapter Two,
        
      </td> 
      <td class="text-center">3.3333333333</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=13">Kabir Singh</a></td> 
      <td class="text-center">31.2124460433%</td> 
      <td class="text-center">2019 film</td> 
      
      <td class="text-center">
        
          Tujhe Kitna Chahne Lage full video song from Kabir Singh,
        
          Box office,
        
          Arjun Reddy,
        
          Shahid Kapoor,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=14">Avengers: Endgame</a></td> 
      <td class="text-center">31.2124460365%</td> 
      <td class="text-center">2019 film</td> 
      
      <td class="text-center">
        
          Avengers: Endgame,
        
          The Avengers,
        
          The Avengers,
        
          Avengers: Age of Ultron,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=15">Cricket World Cup</a></td> 
      <td class="text-center">31.2124460365%</td> 
      <td class="text-center">Cricket tournament</td> 
      
      <td class="text-center">
        
          2018 Under-19 Cricket World Cup,
        
          Trafford,
        
          Old Trafford,
        
          Rose Bowl Cricket Stadium,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=16">#HospitalOnWheels</a></td> 
      <td class="text-center">31.212446035%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Train,
        
      </td> 
      <td class="text-center">3.125</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=17">Article 370</a></td> 
      <td class="text-center">31.212446035%</td> 
      <td class="text-center">Topic</td> 
      
      <td class="text-center">
        
          Article 35A of the Constitution of India,
        
          Union territory,
        
          Quantum,
        
          Quantum mechanics,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=18">Chandrayaan 2</a></td> 
      <td class="text-center">31.212446035%</td> 
      <td class="text-center">Space mission</td> 
      
      <td class="text-center">
        
          Lander,
        
          Moon landing,
        
          Rover,
        
          Earth,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=19">Thalaiva</a></td> 
      <td class="text-center">30.7605082325%</td> 
      <td class="text-center">Actor</td> 
      
      <td class="text-center">
        
          MassTamilan,
        
          Kabaddi,
        
          Darbar,
        
          Theri,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=20">Power Star</a></td> 
      <td class="text-center">30.5463921005%</td> 
      <td class="text-center">Indian film actor</td> 
      
      <td class="text-center">
        
          Electrical resistance,
        
          Katamarayudu,
        
          Copper,
        
          NSE:STAR,
        
      </td> 
      <td class="text-center">0.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=21">#Croatia</a></td> 
      <td class="text-center">30.5245404265%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          France national football team,
        
          Denmark national football team,
        
          2018 World Cup Final,
        
          VFS Global,
        
      </td> 
      <td class="text-center">-2.9027777778</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=22">NEET results</a></td> 
      <td class="text-center">30.5245404265%</td> 
      <td class="text-center">Entrance exam</td> 
      
      <td class="text-center">
        
          2017,
        
          NEET · 2017,
        
          2019,
        
          2020,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=23">Free WiFi</a></td> 
      <td class="text-center">30.3656807135%</td> 
      <td class="text-center">Topic</td> 
      
      <td class="text-center">
        
          Garena Free Fire,
        
          Railwire Broadband,
        
          DD Free Dish,
        
          wifistudy,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=24">ADMK</a></td> 
      <td class="text-center">30.2641464354%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          2016,
        
          2016 United States presidential election,
        
          E. Madhusudhanan,
        
          Meme,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=25">Lok Sabha Elections</a></td> 
      <td class="text-center">30.186704078%</td> 
      <td class="text-center">General election</td> 
      
      <td class="text-center">
        
          Electoral roll,
        
          Scheduled Castes and Scheduled Tribes,
        
          Parliament of India,
        
          Slogan,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=26">Indian Railways</a></td> 
      <td class="text-center">28.7454796388%</td> 
      <td class="text-center">Railway company</td> 
      
      <td class="text-center">
        
          Super Bowl XXVII,
        
          Privatization,
        
          Zones and divisions of Indian Railways,
        
          Train simulator,
        
      </td> 
      <td class="text-center">33.2386363636</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=27">#VakeelSaab</a></td> 
      <td class="text-center">27.3414683927%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Vakeel Saab,
        
          Telugu language,
        
          Pawan Kalyan,
        
          Ringtone,
        
      </td> 
      <td class="text-center">0.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=28">PM Kisan Yojana</a></td> 
      <td class="text-center">25.8404539209%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Pradhan Mantri Kisan Samman Nidhi,
        
          Yojana,
        
          Farmer,
        
          Plan,
        
      </td> 
      <td class="text-center">None</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=29">#VDAY</a></td> 
      <td class="text-center">21.0009497238%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Gift,
        
          Lindt &amp; Sprüngli,
        
          Wish,
        
          V-Day,
        
      </td> 
      <td class="text-center">64.5333333333</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=30">Microsoft</a></td> 
      <td class="text-center">19.1987239444%</td> 
      <td class="text-center">Technology company</td> 
      
      <td class="text-center">
        
          Microsoft Teams,
        
          Microsoft Forms,
        
          GetintoPC,
        
          Microsoft Office 2019,
        
      </td> 
      <td class="text-center">8.4444444444</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=31">The Power</a></td> 
      <td class="text-center">16.5263805014%</td> 
      <td class="text-center">Australian rules football team</td> 
      
      <td class="text-center">
        
          Akhil,
        
          Physical object,
        
          Molecule,
        
          Refraction,
        
      </td> 
      <td class="text-center">1.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=32">#HappyBirthdayTaehyung</a></td> 
      <td class="text-center">14.1116178648%</td> 
      <td class="text-center">hashtag</td> 
      
      <td class="text-center">
        
          Birthday,
        
          V,
        
          Happiness,
        
          Korean language,
        
      </td> 
      <td class="text-center">26.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=33">taetae</a></td> 
      <td class="text-center">12.6633615215%</td> 
      <td class="text-center">Topic</td> 
      
      <td class="text-center">
        
          V,
        
      </td> 
      <td class="text-center">80.0</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=34">run bts</a></td> 
      <td class="text-center">9.1698819917%</td> 
      <td class="text-center">Web series</td> 
      
      <td class="text-center">
        
          Episode,
        
          V Live,
        
          Jungkook,
        
          Jimin,
        
      </td> 
      <td class="text-center">11.7424242424</td> 
    
    
    </tr> 
     
    <tr> 
    
      <td class="text-center"><a class="btn-link" href="https://cues-from-trends.herokuapp.com/?row=35">minseok</a></td> 
      <td class="text-center">1.0%</td> 
      <td class="text-center">South Korean actor</td> 
      
      <td class="text-center">
        
          Kim Min-seok,
        
      </td> 
      <td class="text-center">8.0</td> 
    
    
    </tr> 
     
     
    </tbody> 
  </table> 

  
    
        <img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAA+gAAAJYCAYAAADxHswlAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Il7ecAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB6l0lEQVR4nOzdd3gU1f/28XsDJEBIo4YQSKihCtJCr6E3AQsCioCUL10sgPSiiCIgCKIoWCmCghSlGJFeRem910CAhB5Icp4/8mR+LAQEDewQ36/r4tKdmZ39zObs7txzZs44jDFGAAAAAADApdxcXQAAAAAAACCgAwAAAABgCwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgAwAAAABgAwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgAwAAAABgAwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgAwAAAABgAwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgAwAAAABgAwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgAwAAAABgAwR0AAAAAABsgIAOAAAAAIANENABAAAAALABAjoAAAAAADZAQAcAAAAAwAYI6AAAAAAA2AABHQAAAAAAGyCgA8ADOHLkiBwOh7788ktr2pAhQ+RwOP7R+r788ks5HA4dOXLEmhYcHKyGDRv+y0qTz++//y6Hw6E5c+a4uhSkMNWqVVPRokUfy2s5HA4NGTLkb5eLiIjQs88+q0yZMsnhcGjcuHG2qOvf4nMMAE8WAjqAJ8bWrVvlcDi0d+9eSdLYsWMVHBx813KJwTnxX5o0aRQcHKwePXooKirq8Rb9BJg+ffojDyN4cKdOndKQIUP0119/ubqU/5TXXntNS5YsUb9+/fTNN9+obt26ri7pofzXPsdr167VkCFD/tV3+qRJk5wOugKAHaR2dQEA8KA2bNigjBkzqkCBApKkdevWqVy5cvdc/pNPPlGGDBl09epVhYeHa8KECdqyZYtWr1790K8dFBSk69evK02aNNa0AQMGqG/fvg+/IZJeeukltWjRQh4eHv/o+clp+vTp2rFjh3r16uXqUqCEgD506FAFBwerRIkSri7nP+O3335TkyZN9MYbbzyW17t+/bpSp06+3bD/2ud47dq1Gjp0qF555RX5+vr+o3VMmjRJmTNn1iuvvJKstQHAv0FAB/DE2Lhxo8qWLWudVr5u3Tr17t37nss/++yzypw5sySpU6dOatGihWbNmmWt52E4HA6lTZvWaVrq1Kn/8Q52qlSplCpVqn/0XMCOrl69Kk9PT1eX8Y+dPXv2Hwe9pNy4cUPu7u5yc0v6ZMU7v08AAJA4xR2AzV28eFGRkZGKjIzUhg0bVLRoUUVGRmrnzp06ceKE8ufPr8jISF25cuVv11W5cmVJ0sGDB61pFy5c0BtvvKFixYopQ4YM8vb2Vr169bR161an5z7oNegOh0PdunXTvHnzVLRoUXl4eKhIkSJavHix03JJXYOelK+++kqpU6fWm2+++VD1Jl53+v333+udd95RYGCg0qZNq5o1a+rAgQPWctWqVdOiRYt09OhR65KAOy8biI+Pv+86HkbJkiXVrFkzp2nFihWTw+HQtm3brGmzZs2Sw+HQ7t27JUlHjx5Vly5dFBISonTp0ilTpkx67rnn7nr/bt26paFDhyp//vxKmzatMmXKpEqVKmnZsmX3rSvx77F69Wr16NFDWbJkka+vrzp16qSbN28qKipKL7/8svz8/OTn56e33npLxhindVy9elWvv/66cubMKQ8PD4WEhGj06NF3Lbds2TJVqlRJvr6+ypAhg0JCQvT2229LSvi7lSlTRpLUtm1b629yv9NwL1++rF69eik4OFgeHh7KmjWratWqpS1btjgtt2HDBtWtW1c+Pj5Knz69qlatqjVr1jgt86Dvc+L7tWLFCnXp0kVZs2ZVYGCgNf+XX35R1apV5eXlJW9vb5UpU0bTp0+/q/Zdu3apevXqSp8+vXLkyKH333//rmViYmI0ePBg5cuXTx4eHsqZM6feeustxcTE3LXca6+9pixZssjLy0uNGzfWiRMn7vm+3bktxhhNnDjRes8THTp0SM8995wyZsyo9OnTq1y5clq0aJHTOhI/bzNnztSAAQOUI0cOpU+fXpcuXbrn6955DXri98mBAwesXmEfHx+1bdtW165du+82JOfn+EHaSXK2uXuZMGGCihQpovTp08vPz0+lS5e22tCQIUOs78TcuXNb25zYTqdNm6YaNWooa9as8vDwUOHChfXJJ584rT84OFg7d+7UihUrrOdXq1bNmh8VFaVevXpZn+d8+fJp1KhRio+Pd1rPzJkzVapUKautFytWTB999NEDbSMAJIUedAC29vTTT+vo0aPW4x07dmj06NHW40aNGkmS2rRp87fXEibuvPn5+VnTDh06pHnz5um5555T7ty5FRERoU8//VRVq1bVrl27FBAQ8NA1r169Wj/++KO6dOkiLy8vjR8/Xs2bN9exY8eUKVOmB17PZ599ps6dO+vtt9/WiBEj/lG97733ntzc3PTGG28oOjpa77//vlq1aqUNGzZIkvr376/o6GidOHFCY8eOlSRlyJDhodbxMCpXrqwZM2ZYjy9cuKCdO3fKzc1Nq1at0lNPPSVJWrVqlbJkyaJChQpJkjZt2qS1a9eqRYsWCgwM1JEjR/TJJ5+oWrVq2rVrl9KnTy8pYcd95MiRevXVV1W2bFldunRJmzdv1pYtW1SrVq2/ra979+7y9/fX0KFDtX79en322Wfy9fXV2rVrlStXLr377rv6+eef9cEHH6ho0aJ6+eWXJUnGGDVu3FjLly9X+/btVaJECS1ZskRvvvmmTp48ab23O3fuVMOGDfXUU09p2LBh8vDw0IEDB6zQUqhQIQ0bNkyDBg1Sx44drYNKFSpUuGfNnTt31pw5c9StWzcVLlxY58+f1+rVq7V7926VLFlSUsLp2/Xq1VOpUqU0ePBgubm5WSFm1apV1hklD/o+J+rSpYuyZMmiQYMG6erVq5ISAm+7du1UpEgR9evXT76+vvrzzz+1ePFitWzZ0nruxYsXVbduXTVr1kzPP/+85syZoz59+qhYsWKqV6+epIRQ2bhxY61evVodO3ZUoUKFtH37do0dO1b79u3TvHnzrPW9+uqr+vbbb9WyZUtVqFBBv/32mxo0aPC3f/MqVarom2++0UsvvaRatWpZf1MpYeC4ChUq6Nq1a+rRo4cyZcqkr776So0bN9acOXPUtGlTp3UNHz5c7u7ueuONNxQTEyN3d/e/ff07Pf/888qdO7dGjhypLVu26PPPP1fWrFk1atSoez4nuT7HD9pOkrPNJWXKlCnq0aOHnn32WfXs2VM3btzQtm3btGHDBrVs2VLNmjXTvn37NGPGDI0dO9Y6UypLliySEi5vKlKkiBo3bqzUqVNrwYIF6tKli+Lj49W1a1dJ0rhx49S9e3dlyJBB/fv3lyRly5ZNknTt2jVVrVpVJ0+eVKdOnZQrVy6tXbtW/fr10+nTp61r/ZctW6YXX3xRNWvWtP4+u3fv1po1a9SzZ88H+GsDQBIMANjY6tWrzbJly8zAgQNN6tSpzS+//GKWLVtm6tWrZ0qXLm2WLVtmli1bZnbu3Gk9Z/DgwUaS2bt3rzl37pw5cuSImTp1qkmXLp3JkiWLuXr1qrXsjRs3TFxcnNNrHj582Hh4eJhhw4Y5TZNkpk2bdtfr3E6ScXd3NwcOHLCmbd261UgyEyZMsKZNmzbNSDKHDx+2pgUFBZkGDRoYY4z56KOPjMPhMMOHD3da/4PWu3z5ciPJFCpUyMTExFjTP/roIyPJbN++3ZrWoEEDExQUZO70MOt4ULNnzzaSzK5du4wxxsyfP994eHiYxo0bmxdeeMFa7qmnnjJNmza1Hl+7du2uda1bt85IMl9//bU1rXjx4tZ7+DAS/x516tQx8fHx1vTy5csbh8NhOnfubE2LjY01gYGBpmrVqta0efPmGUlmxIgRTut99tlnjcPhsNrD2LFjjSRz7ty5e9ayadOmu9ra/fj4+JiuXbvec358fLzJnz//Xdt27do1kzt3blOrVi2naXdK6n1OfL8qVapkYmNjrelRUVHGy8vLhIaGmuvXr99VR6KqVavetc6YmBjj7+9vmjdvbk375ptvjJubm1m1apXTuiZPnmwkmTVr1hhjjPnrr7+MJNOlSxen5Vq2bGkkmcGDB9/z/Ukk6a73sVevXkaS0+tfvnzZ5M6d2wQHB1ufxcTPSp48eZJ8D+/1erfXlfh90q5dO6flmjZtajJlyvS36/u3n+OHaSfJ2eaS0qRJE1OkSJH7LvPBBx/c9R16++vcqU6dOiZPnjxO04oUKeL0OU40fPhw4+npafbt2+c0vW/fviZVqlTm2LFjxhhjevbsaby9vZ0+AwDwb3GKOwBbq1ixosLCwnTlyhWVKVNGdevWVVhYmI4dO6aGDRsqLCxMYWFhKly48F3PDQkJUZYsWRQcHKx27dopX758+uWXX5x6AT08PKxrROPi4nT+/HnrtOM7T9d8UGFhYcqbN6/1+KmnnpK3t7cOHTr0QM9///331bNnT40aNUoDBgxwmvew9bZt29apFy+xR/ZBa0muddz53JUrV0pK6CkvU6aMatWqpVWrVklKOLV0x44d1rKSlC5dOuv/b926pfPnzytfvnzy9fV12m5fX1/t3LlT+/fvf+jaJKl9+/ZOpzeHhobKGKP27dtb01KlSqXSpUs7bf/PP/+sVKlSqUePHk7re/3112WM0S+//GLVJ0k//fTTXafK/lO+vr7asGGDTp06leT8v/76S/v371fLli11/vx565KRq1evqmbNmlq5cqVVy4O+z4k6dOjgNJbCsmXLdPnyZfXt2/eua6zvvBwkQ4YMat26tfXY3d1dZcuWdXpfZ8+erUKFCqlgwYJW3ZGRkapRo4Ykafny5ZIS3n9Jd73//3bAtJ9//llly5ZVpUqVnOru2LGjjhw5ol27djkt36ZNG6f38J/o3Lmz0+PKlSvr/Pnz9z1d/kH83ef4YdpJcra5pPj6+urEiRPatGnTP9rW2/8G0dHRioyMVNWqVXXo0CFFR0f/7fNnz56typUry8/Pz6ndhYWFKS4uzvr+8vX11dWrV//2EhoAeBgEdAC2lbhjFRkZqfDwcIWGhioyMlL79u3Tzp07Vbx4cUVGRt5zh+uHH37QsmXLNH36dJUrV05nz569a+c5Pj5eY8eOVf78+eXh4aHMmTMrS5Ys2rZt2wPtyCUlV65cd03z8/PTxYsX//a5K1asUJ8+fdSnTx/rGst/U++dtSSe3v8gtSTnOhJly5ZN+fPnt8L4qlWrVLlyZVWpUkWnTp3SoUOHtGbNGsXHxzsF9OvXr2vQoEHW9aCJ2x0VFeW03cOGDVNUVJQKFCigYsWK6c0333S6tv1ht9XHx0eSlDNnzrum3779R48eVUBAgLy8vJyWSzxFP/EyjRdeeEEVK1bUq6++qmzZsqlFixb6/vvv/1VYf//997Vjxw7lzJlTZcuW1ZAhQ5xCbuLBijZt2ihLlixO/z7//HPFxMRY7+GDvs+JcufO7fQ4cXyHB7nHeWBg4F2h/c7Pyf79+7Vz58676k68k8PZs2clJby/bm5uTgfGpISDdP/G0aNHk1zHnX/XRHe+H/9Ecn7eHma9D9NOkrPNJaVPnz7KkCGDypYtq/z586tr164PfO26JK1Zs0ZhYWHy9PSUr6+vsmTJYo3z8CDf6/v379fixYvvqj0sLEzS/7W7Ll26qECBAqpXr54CAwPVrl27u8YbAYCHxTXoAGyrSZMmWrFihfV427ZtTvf5Tbz+s2rVqvr999/ven6VKlWsaxMbNWqkYsWKqVWrVvrjjz+sXuh3331XAwcOVLt27TR8+HBlzJhRbm5u6tWr1z8OTfcand3cMVhYUooUKaKoqCh988036tSp0107/A9b77+pJTnXcbtKlSopPDxc169f1x9//KFBgwapaNGi8vX11apVq7R7925lyJBBTz/9tPWc7t27a9q0aerVq5fKly8vHx8fORwOtWjRwmm7q1SpooMHD+qnn37S0qVL9fnnn2vs2LGaPHmyXn311X+8rUlN/yfbny5dOq1cuVLLly/XokWLtHjxYs2aNUs1atTQ0qVL/9HI/s8//7wqV66suXPnaunSpfrggw80atQo/fjjj6pXr571/nzwwQf3vG1b4vXKD/o+3749/9SDtKv4+HgVK1ZMY8aMSXLZOw+cuNq/7T2Xkv/z9qDrfZh2kpxtLimFChXS3r17tXDhQi1evFg//PCDJk2apEGDBmno0KH33c6DBw+qZs2aKliwoMaMGaOcOXPK3d1dP//8s8aOHftA3+vx8fGqVauW3nrrrSTnJx4gypo1q/766y8tWbJEv/zyi3755RdNmzZNL7/8sr766qu/fR0ASAoBHYBtffjhh7p48aLWrVunoUOHauHChUqdOrUmTJigkydP6r333pPkPOjbvWTIkEGDBw9W27Zt9f3336tFixaSpDlz5qh69er64osvnJaPioqywv3jlDlzZs2ZM0eVKlVSzZo1tXr1aqeB3x5FvXf2Yj5qlStX1rRp0zRz5kzFxcWpQoUKcnNzU6VKlayAXqFCBadAMWfOHLVp00YffvihNe3GjRuKioq6a/0ZM2ZU27Zt1bZtW125ckVVqlTRkCFDHiig/1NBQUH69ddfdfnyZade9D179ljzE7m5ualmzZqqWbOmxowZo3fffVf9+/fX8uXLFRYW9o/+HtmzZ1eXLl3UpUsXnT17ViVLltQ777yjevXqWb3K3t7eVg/gvTzM+5yUxNfasWOH8uXL99DbkdT6tm7dqpo1a973fQkKClJ8fLwOHjzo1OO9d+/ef/X6QUFBSa4jqb+rq/3bz/HDtBMp+drc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DoeZMmWKMSbhgFCWLFnM119/bYy5e6diwYIFpnz58tZp78YYs3fvXlOnTh3TvXt3Y4wx27ZtM+XLlzf58uUzLVq0MPnz5zc5cuQwr7322l3Xl9+J0/xSnsQ2NGvWLOPv729OnDhhzTt69KhxOBxmxowZJiYmxqRKlco0btz4rnbw/fffm1KlSpmWLVuaH3/80Xz66acmb9685scffzTGGPP222+bkJAQM2LECHPlyhXz5ZdfWm3w7bffTrIePDr3OuBsjDG7du0yERER5sUXXzQOh8McOHDAFClSxGTIkMH07dvXel7t2rVNo0aNrOATGRlp2rRpY0qVKmX69etn5s6da2rXrm3q169vjEk4Db5du3YmNDTUGJPQC3ru3Dlz6tQp06ZNGxMQEGAKFixoJk6c+NBnFeHRudfZFLfPu31f6sqVK8bHx8d899131rQvv/zSFC5c2JQtW9Z06dLFFCtWzISFhVmnoq9atcqEhISYoUOHWs85fvy4eeaZZ8wrr7xijDHm008/NWnTpnXq6BgxYoRJnTq1GTx4sLXvNH78eFOxYkVTpUoV88033yTZk/8gl20AdsNt1pAiGWMUHx9v3QbI4XA43YIqNjb2nrcIio6O1sKFC1W2bFllz55d/fv310cffaS8efNq3759Gj16tGbOnKmpU6dKkoKDg5U9e3YtWLBAUsLtz7Jly6bly5dbtdypYcOG2rNnj9NtrJo1a6bJkydr8ODBat68ubWsv7+/goOD//2bApdIvA9w8eLFlT59em3fvl0xMTGKi4tT4cKF9eWXX0pKaCdubm4KCwvTihUrJEl//fWXMmfObN1uKHG5xPvDFitWTN7e3tZt9aSE9pgvXz5t3bpVxhgVK1ZM4eHhGj58uHLlyqWhQ4dq9+7dGjNmjDJlymQ9L6n7qCfe/xxPBvM3tz+T/u+WefXq1VNERITWr19vtafE2y7Gx8fL3d1dBQoUkJ+fn2JiYqznR0VFady4cSpYsKC++eYbNW3aVLly5VJERITVDnv27KlXXnlFU6dOlb+/v95991317t1b3377rd54440k68HDu9etPL///nun+8SnSpUqyfd53bp1KlmypFq3bq0CBQpo06ZNyps3r55//nmlSpVKNWrUsJ7XqVMnHTlyxLqt54IFCzR79mx99dVXevfdd/XMM8/Izc3Nmp8tWzY999xz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UydTuXJlp96E119/3QQEBJjY2Fhz8+ZNs2PHDkajTUHOnz9vSpUqZfr06WNN2717t6lUqZJ56qmnzNNPP21ef/11p+e89NJLpmnTpiYqKsocOXLEpE+f3qxYscIY83/3cn3ppZdMaGiodSu1fv36GX9/f/Pll1+a48ePmwEDBpiqVauaNGnSOI2wfT+EpifTV199ZbJmzWr1SH744YemQoUKZuPGjdYye/bscbqd3dSpU43D4TBly5Y1v/zyizU9caf1119/NS+//LLJkSOHSZ8+vfHz87NC1+0SA3hoaKjp2LGjFcATJfakrlmzxuzatSuZthjJrUOHDqZOnTqmSpUqpn///tbfLfE74ciRI6Z+/fqmRo0a5uOPPzbr1683xYsXN926dTPGGHPy5ElTr1498/LLLxtj/i+gr1u3zqRLl87Mnz/fBVsFV/rjjz9MYGCgdcCvffv2xuFwGD8/PxMSEmI6depk5s+fb86cOWM958svvzSZMmUyly9fNleuXDGvvfaayZgxo3n55ZdN6dKlTfv27c1nn31m3nvvPauNPogbN244vQ7wX8E16Eix0qZNq1KlSunixYvav3+/HA6HvLy89N1336l169basWOHOnfurB49emjfvn06ePCgJKlmzZrav3+/03WXDRs21OrVq3Xs2DFrWt++fbVx40alSpVKadKkUZEiRRiNNgXx8/NTSEiIDh48qNjYWN26dUsFCxZUcHCwPD09lTVrVp05c0anT5+2nlOsWDFFRERo3759ypIliwoVKqTvv/9e0v+N5p4pUyadOHFChw8flpRwvXjz5s3Vt29fFShQQMePH9ePP/6ojRs3KkeOHHfVFRsbe9f171xL/mS5deuWpIRB/oKCgqzrMkuUKCE3NzetWLFCX375pTw9PVWzZk29/PLL1hgDDRs2VNasWeXt7a26deta63Rzc9PcuXPVt29fpUqVSp999pl1jehvv/0myXnUb/P/ry2uVq2aZs2apfPnzzvVmDiQZoUKFVSoUKFH8TYgGdSqVUvbt2/XqlWrtGHDBmtw0sTvhC+++ELbtm3Td999p65duyp//vxKnTq1Nm7cKCnhe+7pp5/W7NmzJcm6trdcuXL666+/1KhRIxdsFVwpR44cKlq0qDVQXKVKlZQmTRotWrRIe/bs0eTJk9WoUSNlzZrV2ieqVq2aLly4oI0b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">
    
  
</div> 


<div class="col-md-3">
<br><br><br>

  <div class="card text-center text-white bg-dark mb-3" style="width: 45rem;">
    <div class="card-body">
      <div class="card-header"><h4 class="card-title">Title: #Rajinikanth</h4></div>
      <br>
      <h4 class="card-subtitle mb-2 text-muted">Type: hashtag</h4>
      <h4 class="card-subtitle mb-2 text-muted">Popularity Score: 38.66%</h4>
      <h4 class="card-subtitle mb-2 text-muted">Sentiment Score: 6%</h4>
    </div>
  </div>


  <br>


 <div class="card text-center text-white bg-dark mb-3" style="width: 45rem;">
  <div class="card-body">
    
      <img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAArwAAAH0CAYAAADfWf7fAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Il7ecAAAACXBIWXMAAA9hAAAPYQGoP6dpAACVvElEQVR4nOzdd1hT1xsH8G9A9nQhoIhbVHDhKFpXRcFV96qt29a9d91at6227qporaNqrXsWxb33QAWr4gBxASLKPL8/zo9oBBSUcJPw/TwPDzc3yc2bEODNue95j0oIIUBEREREZKCMlA6AiIiIiEibmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASERERkUFjwktEREREBo0JLxEREREZNCa8RERERGTQmPASEX3E3bt3oVKpsHLlSqVD0TBr1iwUKVIExsbGKF++vNLhKK5QoULo3Lmz+nJAQABUKhUCAgIyfKzUfuadO3eGtbX15weaiVQqFfr27at0GEQ6jwkvUSZauXIlVCoVzp49m+H7xsTEYMKECZ/0zzmrLVy4UOeSv8ywdu1azJ07V+kw0mXfvn0YPnw4qlevDj8/P0ydOlXpkCCEQK5cubBkyRIAwIULF6BSqXD37l2N2yUnoslfxsbGcHBwQKtWrRAYGKhA5Lrt+PHjmDBhAiIiIpQOhUhv5VA6ACKSYmJiMHHiRABA7dq1lQ3mIxYuXIg8efJojKYZgrVr1+Lq1asYOHCgxn5XV1e8fv0aJiYmygSWigMHDsDIyAjLly+Hqamp0uEAAIKCgvDixQt88cUXAIATJ04gX758KFSoUKq379+/PypXroz4+HhcvnwZixcvRkBAAK5evQpHR8cMP/7NmzdhZPR2HKdm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">
    
  </div>
</div>

 <br>


 <div class="card text-center text-white bg-dark mb-3" style="width: 45rem;">
  <div class="card-body">
    <div class="card-header"><h4 class="card-title">Related Topics</h4></div>
    <ul class="list-group list-group-flush">
      
      <li class="list-group-item text-white bg-dark mb-3">Kaala</li>
      
      <li class="list-group-item text-white bg-dark mb-3">Petta</li>
      
      <li class="list-group-item text-white bg-dark mb-3">Darbar</li>
      
      <li class="list-group-item text-white bg-dark mb-3">Bear Grylls</li>
       
    </ul>
  </div>
</div>

<br>


<div class="card text-center text-white bg-dark mb-3" style="width: 45rem; max-height: 400px; overflow: scroll">
  <div class="card-body">
    <div class="card-header"><h4 class="card-title">Sample Tweets about Topic</h4></div>
    <ul class="list-group list-group-flush">
      
      <li class="list-group-item text-white bg-dark mb-3">RT @TFC_Back: Take Care of Your Health.. Dont Think Anything !! Get Well Soon.. I appreciate your Open Statement !! Respect Sir !! Endrum T…</li>
      
      <li class="list-group-item text-white bg-dark mb-3">RT @IndiaToday: Superstar #Rajinikanth has announced that he will not be starting his political party and that his recent health scare is a…</li>
      
      <li class="list-group-item text-white bg-dark mb-3">How misleading reel life is ???</li>
      
      <li class="list-group-item text-white bg-dark mb-3">RT @GRajinified: People who say - #thalaivar will be now mocked more by others
SEE THIS GUYS!!! 

🤘He was never mocked by others
🤘He was ne…</li>
      
      <li class="list-group-item text-white bg-dark mb-3">RT @contking: BJP ko thoda round ghumake
MGR ke jaise battein karake
Politics me Kollywood milake
Chale gaye sabke mood banake

All the Raj…</li>
       
    </ul>
  </div>
</div>

<br>

<div class="card text-center text-white bg-dark mb-3" style="width: 45rem; max-height: 400px; overflow: scroll ">
  <div class="card-body">
    <div class="card-header"><h4 class="card-title">Sample Posts from Subreddits about Topic</h4></div>
    <ul class="list-group list-group-flush">
      
      <li class="list-group-item text-white bg-dark mb-3">No Subreddits Found</li>
       
    </ul>
  </div>
</div>



</div>
</div>
<br>
<div class="card text-center text-white bg-dark mb-3" style="max-height: 400px; overflow: scroll">
  <div class="card-body">
    <div class="card-header"><h4 class="card-title">Extracted Text Cues </h4></div>
    <ul class="list-group list-group-flush">
      
      <li class="list-group-item text-white bg-dark mb-3"> Dont Think Anything </li>
      
      <li class="list-group-item text-white bg-dark mb-3">I appreciate your Open Statement </li>
      
      <li class="list-group-item text-white bg-dark mb-3"> Respect Sir </li>
      
      <li class="list-group-item text-white bg-dark mb-3">#Rajinikanth has announced that he</li>
      
      <li class="list-group-item text-white bg-dark mb-3"> People who say -  #thalaivar</li>
      
      <li class="list-group-item text-white bg-dark mb-3">🤘He was never mocked by others</li>
      
      <li class="list-group-item text-white bg-dark mb-3">🤘He was ne…</li>
       
    </ul>
  </div>
</div>


 
 

    

</body></html>

