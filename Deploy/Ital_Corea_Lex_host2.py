from multiprocessing import Pool

import pandas as pd
import re


data = pd.read_csv('CorEA-message-level_clean2.csv', sep='\t',quotechar="'",
                  engine='python')
data.head(5)


# In[6]:

lex = pd.read_csv('ITALconvertcsv.csv', delimiter=",", quotechar='"', header=0)
lex.head(5)
#print(lex[0:5])
#print(list(lex))


# In[20]:

# In[7]:

new_lex=pd.concat([lex['Lemma/_writtenForm'], lex['Sense/Sentiment/_polarity'], ],axis=1)

halfindex=int((len(new_lex.index))/2)
halfword=(new_lex['Lemma/_writtenForm'][halfindex])
halfplusword=(new_lex['Lemma/_writtenForm'][halfindex+1])
while (halfword[0]==halfplusword[0]):
    halfindex+=1
    halfplusindex=halfindex+1
    halfword=(new_lex['Lemma/_writtenForm'][halfindex])
    halfplusword=(new_lex['Lemma/_writtenForm'][halfplusindex])

#print(halfword)
#print(halfindex)

#print(halfplusword)
#print(halfplusindex)

uphalfLex=new_lex.ix[:halfindex]
lowhalfLex=new_lex.ix[halfplusindex:]
uphalfLex.reset_index(drop=True, inplace=True)
lowhalfLex.reset_index(drop=True, inplace=True)
#print(uphalfLex)
#print(lowhalfLex)


# In[56]:

upquarterindex=int((len(uphalfLex.index))/2)
upquarterword=(uphalfLex['Lemma/_writtenForm'][upquarterindex])
upquarterplusword=(uphalfLex['Lemma/_writtenForm'][upquarterindex+1])
while (upquarterword[0]==upquarterplusword[0]):
    upquarterindex+=1
    upquarterplusindex=upquarterindex+1
    upquarterword=(uphalfLex['Lemma/_writtenForm'][upquarterindex])
    upquarterplusword=(uphalfLex['Lemma/_writtenForm'][upquarterplusindex])

#print(upquarterword)
#print(upquarterplusword)
upupquarterLex=uphalfLex.ix[:upquarterindex]
uplowquarterLex=uphalfLex.ix[upquarterplusindex:]

upupquarterLex.reset_index(drop=True, inplace=True)
uplowquarterLex.reset_index(drop=True, inplace=True)
#print(upupquarterLex)
#print(uplowquarterLex)


# In[59]:

lowquarterindex=int((len(lowhalfLex.index))/2)

lowquarterword=(lowhalfLex['Lemma/_writtenForm'][lowquarterindex])
lowquarterplusword=(lowhalfLex['Lemma/_writtenForm'][lowquarterindex+1])
while (lowquarterword[0]==lowquarterplusword[0]):
    lowquarterindex+=1
    lowquarterplusindex=lowquarterindex+1
    lowquarterword=(lowhalfLex['Lemma/_writtenForm'][lowquarterindex])
    lowquarterplusword=(lowhalfLex['Lemma/_writtenForm'][lowquarterplusindex])

#print(lowquarterword)
#print(lowquarterplusword)
lowupquarterLex=lowhalfLex.ix[:lowquarterindex]
lowlowquarterLex=lowhalfLex.ix[lowquarterplusindex:]

lowupquarterLex.reset_index(drop=True, inplace=True)
lowlowquarterLex.reset_index(drop=True, inplace=True)
#print(lowupquarterLex)
#print(lowlowquarterLex)


# In[ ]:

# In[11]:
cellvavlist=[]
leftrightlist=[]
#for cell in (data['text']):
 #   for word in (cell.split()):


rightlist=[]
leftlist=[]



#for each cell in the text column of data

def lexiconclassifier(cell):

    cellrating=0
    wordcount=0
    lr_classifier=0
    LeftOrRight="None"
    #for reach word in cell
    for word in (cell.split()):
        word=re.sub("[^A-Za-z|-]","", word)
        #print(word)

        ratingfactor=0
        #iterates through the lexicon
        if word in rightlist and lr_classifier==0:
            #print(word)
            lr_classifier="right"
            #print(lr_classifier)
        if word in rightlist and lr_classifier=="right":
            #print(word)
            lr_classifier="right"
            #print(lr_classifier)
        if word in rightlist and lr_classifier=="left":
            #print(word)
            lr_classifier="None"
            #print(lr_classifier)
        if word in rightlist and lr_classifier=="left":
            #print(word)
            lr_classifier="left"
            #print(lr_classifier)
        if word in leftlist and lr_classifier==0:
            #print(word)
            lr_classifier="left"
            #print(lr_classifier)
        if word in leftlist and lr_classifier=="right":
            #print(word)
            lr_classifier="None"
        try:
            if word[0]<=halfplusword[0]:
                if word[0]<=upquarterplusword[0]:
                    new_lex=upupquarterLex
                else:
                    new_lex=uplowquarterLex
            else:
                if word[0]<=lowquarterplusword[0]:
                    new_lex=lowupquarterLex
                else:
                    new_lex=lowlowquarterLex
        except LookupError:
            pass

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

                cellrating=cellrating+(ratingfactor)
    if wordcount==0:
        cellaverage=0
    else:
        cellaverage=(cellrating/wordcount)
    print(cellaverage)
    return(cellaverage)
    #cellvavlist.append(cellaverage)
    #print(lr_classifier)
    #leftrightlist.append(lr_classifier)
    #print(a)

cells=[str(cell) for cell in (data['6text'])]


pool = Pool(processes=3)

result = pool.map(lexiconclassifier, cells)

print(result)

extrarow = pd.DataFrame(cellvavlist)
extrarow2=pd.DataFrame(leftrightlist)

output=pd.concat([data, extrarow, extrarow2],axis=1)
output.to_csv('Corea.csv', encoding='utf-8')


# In[ ]:




# In[ ]:
