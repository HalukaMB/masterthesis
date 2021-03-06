
# coding: utf-8

# In[4]:

import pandas as pd
import re

# In[5]:

data = pd.read_csv('bigtweets_2_out_utf8.csv', delimiter=",", quotechar="'", error_bad_lines=False)
data.head(5)


# In[6]:

lex = pd.read_csv('englishconvert.csv', delimiter=",", quotechar="'")
lex.head(5)
print(lex[1:5])


# In[7]:

new_lex=pd.concat([lex['Lemma/_writtenForm'], lex['Sense/Sentiment/_polarity'], lex['Sense/Sentiment/_strength']],axis=1)
print(new_lex)


# In[8]:

print(lex['Lemma/_writtenForm'][0:5])


# In[11]:
cellvavlist=[]
leftrightlist=[]
#for cell in (data['text']):
 #   for word in (cell.split()):
for row in new_lex:
    print(row)

rightlist=["Theresa","May","Conservatives","Tory","Conservative","Tories"]
leftlist=["Jeremy", "Corbyn", "Labour"]


a=0
#for each cell in the text column of data
for cell in (data['text']):
    a+=1
    cellrating=0
    wordcount=0
    lr_classifier=0
    LeftOrRight="None"
    #for reach word in cell
    for word in (cell.split()):
        word=re.sub("[^A-Za-z|-]","", word)
        print(word)
        if a>10:
            break
        ratingfactor=0
        #iterates through the lexicon
        if word in rightlist and lr_classifier==0:
            print(word)
            lr_classifier="right"
            print(lr_classifier)
        if word in rightlist and lr_classifier=="right":
            print(word)
            lr_classifier="right"
            print(lr_classifier)
        if word in rightlist and lr_classifier=="left":
            print(word)
            lr_classifier="None"
            print(lr_classifier)
        if word in rightlist and lr_classifier=="left":
            print(word)
            lr_classifier="left"
            print(lr_classifier)
        if word in leftlist and lr_classifier==0:
            print(word)
            lr_classifier="left"
            print(lr_classifier)
        if word in leftlist and lr_classifier=="right":
            print(word)
            lr_classifier="None"

        for index, row in (new_lex).iterrows():
            #if word is found in the lexicon
            #print str.startswith( 'this' )
            if word.startswith(row["Lemma/_writtenForm"]):
                wordcount+=1
                #classifier
                if row["Sense/Sentiment/_polarity"]=="neutral":
                    ratingfactor=0
                if row["Sense/Sentiment/_polarity"]=="positive":
                    ratingfactor=1
                if row["Sense/Sentiment/_polarity"]=="negative":
                    ratingfactor=-1
                if row["Sense/Sentiment/_strength"]=="average":
                    rating=0.5
                if row["Sense/Sentiment/_strength"]=="strong":
                    rating=1
                cellrating=cellrating+(ratingfactor*rating)
    if wordcount==0:
        cellaverage==0
    else:
        cellaverage=(cellrating/wordcount)
    print(cellaverage)
    cellvavlist.append(cellaverage)
    print(lr_classifier)
    leftrightlist.append(lr_classifier)
    print(a)


extrarow = pd.DataFrame(cellvavlist)
extrarow2=pd.DataFrame(leftrightlist)

output=pd.concat([data, extrarow, extrarow2],axis=1)
output.to_csv('outputLex.csv', encoding='utf-8')


# In[ ]:
