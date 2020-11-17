import preprocessor as tweet_p
import re
from emoji import UNICODE_EMOJI
from nltk.tokenize import word_tokenize
import spacy    
tweet_p.set_options(tweet_p.OPT.URL,tweet_p.OPT.MENTION)
nlp = spacy.load("en_core_web_sm")
all_stopwords = set(nlp.Defaults.stop_words)



def is_emoji(s):
    return s in UNICODE_EMOJI



def gather_details(orig_line_str):
    
    orig_line_str = re.sub(r'^RT', '', orig_line_str)

    doc = nlp(orig_line_str) 

    named_entities = set()

    for nc in doc.noun_chunks:
        flag = False
        for w in nlp(str(nc)):
            if w.tag_ == 'NNP':
                named_entities.add(nc.text) 

    orig_line = word_tokenize(orig_line_str)
    exclamation_indices = []
    emoji_indices = []
    emojis = []
    hashtags = []

    temp = []

    #  Coach #Bigil 🔥🔥 Another fav scene
    for w in orig_line:
        #print(w)
        word = w[0]

        for character in range(1,len(w)):
            #print(w[character])
            if w[character] in UNICODE_EMOJI:
                #print(w[character])

                if word[-1] not in UNICODE_EMOJI:
                    word += ' '+w[character].strip()
                else:
                    #print(w[character])
                    if word[-1] == w[character]:
                        pass
                    word = word.strip()+w[character]
            else:
                #print(w[character])
                word = word.strip() + w[character]
            #print(word)

        temp.append(word.strip())


    line_str = ' '.join(temp)
    line_str = re.sub('# ','#',line_str)
    line = word_tokenize(line_str)

    c = 0
    for word_index in range(len(orig_line)):
        if orig_line[word_index] in all_stopwords:
            continue
        elif orig_line[word_index].startswith('#'):
            hashtags.append('#'+orig_line[word_index+1])

        elif orig_line[word_index] == '!':
            exclamation_indices.append(word_index)

        elif is_emoji(orig_line[word_index][0]) :
            emoji_indices.append(word_index)
            if len(orig_line[word_index]) > 1 and len(list(set(orig_line[word_index]))) == 1:
                emojis.append(orig_line[word_index][0])
            else:
                emojis.append(orig_line[word_index])




    return exclamation_indices,emoji_indices, hashtags,named_entities, emojis,orig_line,line,line_str


def hashtag_cues(orig_line_str,hashtags):
    chunks = re.split(',|\.|:|&|\!|\?', orig_line_str)

    cues_1 = set()
    #chunks_set = set(chunks)
    if len(hashtags)>0:

        if len (orig_line_str)>=6:

            for ht in hashtags:
                #print(ht)
                for chunk in chunks:
                    #print(chunk)
                    if ht in chunk:
                        no_stops = ' '.join(w for w in chunk.split() if w not in all_stopwords)
                        if len(no_stops)>5:
                            twos = chunk.split(ht)
                            #print(twos)
                            left = twos[0] + ' ' + ht
                            right = ht + ' ' + twos[1]
                            left_no_stops = [w for w in left.split() if w not in all_stopwords]
                            #print(left_no_stops)
                            try:
                                right_no_stops = [w for w in right.split() if w not in all_stopwords]
                                if len(right_no_stops)>=3:
                                    if len(right_no_stops)>=5:
                                        cues_1.add(' '.join(right.split()[:5]))
                                    else:
                                        cues_1.add(right)
                            except:
                                pass

                            if len(left_no_stops)>=3:
                                if len(left_no_stops)>=5:
                                    cues_1.add(' '.join(left.split()[-5:]))
                                else:
                                    cues_1.add(left)
    return cues_1



def exclamation_cues(exclamation_indices,orig_line):
    
    cues_1 = set()
    if len(exclamation_indices) != 0:
        actual_indices = [exclamation_indices[0]]
        for i in range(1, len(exclamation_indices)):
            if exclamation_indices[i] == exclamation_indices[i-1]+1:
                continue
            else:
                actual_indices.append(exclamation_indices[i])


        exclamation_cues = []
        for i in actual_indices:
            try:
                exclamation_cues.append(' '.join(orig_line[i-5:i+1]))
            except:
                exclamation_cues.append(' '.join(orig_line[0:i+1]))
        #print(exclamation_cues)
        for j in exclamation_cues:

            chunks_ex = re.split(',|\.|:|&|\!|\?', j)
            #print(chunks_ex)
            if len(chunks_ex)>1:
                cues_1.add(chunks_ex[-2])
    return cues_1



def emoji_1(emoji_indices,orig_line,named_entities,orig_line_str):

    cues_1 = set()
    if len(emoji_indices)!= 0:
        for e in emoji_indices:
            try:
                if orig_line[e-1] in {'.','?',',',':','!'}:
                    if len(named_entities) != 0:
                        for ne in named_entities:
                            #print(ne)
                            ne_left = ne.split()[0]
                            ne_right = ne.split()[-1]
                            try:
                                left_cue = orig_line[orig_line.index(ne_left)-4:orig_line.index(ne_left)+1]
                            except:
                                left_cue = orig_line[:orig_line.index(ne_left)+1]
                            try:
                                right_cue = orig_line[orig_line.index(ne_right)+1:orig_line.index(ne_left)+5]
                            except:
                                right_cue = orig_line[orig_line.index(ne_right):]
                            cues_1.add((' '.join(left_cue) + ' ' + ne).strip())
                            cues_1.add((ne + ' ' + ' '.join(right_cue)).strip())
                else:

                    no_stops = [w for w in orig_line_str.split() if w not in all_stopwords]
                    if len(no_stops) <=5:
                        cues_1.add(orig_line_str)
                    else:
                        if len(named_entities) != 0:
                            for ne in named_entities:
                                #print(ne)
                                ne_left = ne.split()[0]
                                ne_right = ne.split()[-1]
                                try:
                                    left_cue = orig_line[orig_line.index(ne_left)-4:orig_line.index(ne_left)]
                                except:
                                    left_cue = orig_line[:orig_line.index(ne_left)+1]
                                try:
                                    right_cue = orig_line[orig_line.index(ne_right)+1:orig_line.index(ne_left)+5]
                                except:
                                    #print(ne_right,orig_line)
                                    right_cue = orig_line[orig_line.index(ne_right):]
                                cues_1.add((' '.join(left_cue) + ' ' + ne).strip())
                                cues_1.add((ne + ' ' + ' '.join(right_cue)).strip())

            except Exception as e:
                #print(e)
                continue        
    return cues_1


def emoji_2(line_str, emojis):

    chunks = re.split(',|\.|:|&|\!|\?', line_str)

    cues_1 = set()
    #chunks_set = set(chunks)
    if len(emojis)>0:

        if len (line_str)>=6:

            for ej in emojis:
                #print(ej)
                for chunk in chunks:
                    #print(chunk)
                    if ej in chunk:
                        no_stops = ' '.join(w for w in chunk.split() if w not in all_stopwords)
                        if len(no_stops)>5:
                            twos = chunk.split(ej)
                            #print(twos)
                            left = twos[0] + ' ' + ej
                            right = ej + ' ' + twos[1]
                            left_no_stops = [w for w in left.split() if w not in all_stopwords]
                            #print(left_no_stops)
                            try:
                                right_no_stops = [w for w in right.split() if w not in all_stopwords]
                                if len(right_no_stops)>=3:
                                    if len(right_no_stops)>=5:
                                        cues_1.add(' '.join(right.split()[:5]))
                                    else:
                                        cues_1.add(right)
                            except:
                                pass

                            if len(left_no_stops)>=3:
                                if len(left_no_stops)>=5:
                                    cues_1.add(' '.join(left.split()[-5:]))
                                else:
                                    cues_1.add(left)
    return cues_1


def get_text_cues(orig_line_str):
    
    cues_1 = set()
    exclamation_indices,emoji_indices, hashtags,named_entities, emojis,orig_line,line,line_str = gather_details(orig_line_str)
    cues_1 = cues_1.union(hashtag_cues(orig_line_str,hashtags))
    cues_1 = cues_1.union(exclamation_cues(exclamation_indices,orig_line))
    cues_1 = cues_1.union(emoji_1(emoji_indices,orig_line,named_entities,orig_line_str))
    cues_1 = cues_1.union(emoji_2(line_str, emojis))
    cues_1.discard('RT')
    cues_1.discard('RT :')
    return list(cues_1)



def get_all_text_cues(df):

    

    mapping = {}
    for title,tweets,reddits in zip(df['title'],df['Tweets'],df['Reddit_Posts']):
        
        
        try:
            cues = []
            for j in tweets:

                j = j.splitlines()
                for tweet in j:
                    tweet = tweet_p.clean(re.sub(r'^RT : ', '', tweet))
                    cues += get_text_cues(tweet)
                    
            try:
                
                for j in reddits:

                    j = j.splitlines()
                    for post in j:
                        cues += get_text_cues(post)
            except Exception as e:
                pass
                #print(e)
            
            mapping.update({title:cues})
            #print(title)
        except Exception as e:
            pass

    df['Text_Cues'] = df['title'].map(mapping)

    return df
    


