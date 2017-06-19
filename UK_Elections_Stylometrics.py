import pandas as pd
import re


data = pd.read_csv('bigtweets_2_out_utf8.csv', delimiter=",", quotechar="'", error_bad_lines=False)
data.head(5)


rightlist=["Theresa","May","Conservatives","Tory","Conservative","Tories"]
leftlist=["Jeremy", "Corbyn", "Labour"]

dotcountlist=[]
commacountlist=[]
exclamationcountlist=[]
wordcountlist=[]
uppercasecountlist=[]
lr_classifierlist=[]
a=0
#for each cell in the text column of data

for cell in (data['text']):
    print(a)
    a+=1
    dotcount=0
    commacount=0
    exclamationcount=0
    wordcount=0
    uppercasecount=0
    lr_classifier=0


    dotcount=cell.count(".")
    commacount=cell.count(",")
    exclamationcount=cell.count("!")
    if a>10000:
        break
    else:

        #for reach word in cell
        for word in (cell.split()):
            wordcount+=1
            uppercaseword=word[1:]
            uppercasecount+=sum(1 for c in uppercaseword if c.isupper)

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


        print("Dotcount: " + str((dotcount)))
        print("Commacount: "+ str(commacount))
        print("Exclamationcount: "+ str(exclamationcount))
        print("Wordcount: "+ str(wordcount))
        print("Uppercasecount "+ str(uppercasecount))
        print(lr_classifier)
        dotcountlist.append(dotcount)
        commacountlist.append(commacount)
        exclamationcountlist.append(exclamationcount)
        wordcountlist.append(wordcount)
        lr_classifierlist.append(lr_classifier)

row1 = pd.DataFrame(dotcountlist)
row2=pd.DataFrame(commacountlist)
row3=pd.DataFrame(exclamationcountlist)
row4=pd.DataFrame(wordcountlist)
row5=pd.DataFrame(lr_classifierlist)
output=pd.concat([data, row1, row2, row3, row4, row5],axis=1)
output.to_csv('outputStylo.csv', encoding='utf-8')


    # In[ ]:
