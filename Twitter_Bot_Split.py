
# coding: utf-8

# In[17]:

import pandas as pd
import re
import io

def botsplit(day):
    # In[69]:

    data = pd.read_csv('/Users/halukamaier-borst/Documents/CardiffUniversity/Master Thesis/'+day+'.csv', skipinitialspace = True, quotechar = "'")


    # In[70]:

    data=data.sort_values(by='id')


    # In[71]:

    id=0
    counter=0
    botlist=[]
    for cell in data["id"]:
        if counter>49:
            if id not in botlist:
                botlist.append(id)
            else:
                pass
        if cell != id:
            id=cell
            counter=1
        else:
            counter+=1




    # In[72]:

    ID=0
    counter=0
    normallist=[]
    for cell in data["id"]:


        if cell!=ID:
            if counter==1:
                normallist.append(ID)
                counter=0
            else:
                counter=0
        else:
            pass
        counter+=1
        ID=cell
    if (counter==1):
        normallist.append(ID)



    # In[73]:



    # In[74]:

    frames=[data["text"], data["id"],]
    reduced_data=pd.concat([data["text"], data["id"],], axis=1)


    # In[75]:

    botsampleid = []
    normalsampleid = []
    botsampletext=[]
    normalsampletext=[]

    progcounter=0
    for index, row in reduced_data.iterrows():
        progcounter+=1
        if(row['id'])in botlist:
            botsampleid.append(row['id'])
            botsampletext.append(row['text'])

        if(row['id'])in normallist:
            normalsampleid.append(row['id'])
            normalsampletext.append(row['text'])



        if (progcounter%1000==0):
            print(progcounter)




    # In[77]:

    botdf=pd.DataFrame()
    botdf["id"]=botsampleid
    botdf["text"]=botsampletext
    botdf["botornot"]=1
    normaldf=pd.DataFrame()
    normaldf["id"]=normalsampleid
    normaldf["text"]=normalsampletext
    normaldf["botornot"]=0
    normaldf.reset_index(drop=True, inplace=True)
    botdf.reset_index(drop=True, inplace=True)
    normaldf = normaldf[normaldf.text != 'text']
    botdf = botdf[botdf.text != 'text']

    normaldf=(normaldf.sample(5000))
    botdf=(botdf.sample(5000))


    # In[78]:

    normaldf.to_csv("normaltweets"+day+".csv", quotechar='"')
    botdf.to_csv("bottweets"+day+".csv", quotechar='"')
    test=pd.concat([normaldf,botdf], ignore_index=True)
    test.to_csv("/Users/halukamaier-borst/Documents/CardiffUniversity/Master Thesis/BotorNot"+day+".csv", quotechar='"', index=False)
    test.head(5)


    # In[79]:

    test.tail(5)


    # In[80]:

    data = test
    dotcountlist=[]
    commacountlist=[]
    exclamationcountlist=[]
    wordcountlist=[]
    uppercasecountlist=[]
    lowercasecountlist=[]
    charcountlist=[]
    specialcharlist=[]
    numbercountlist=[]
    uniquewordlist=[]
    qmarkcountlist=[]
    apicescountlist=[]
    quotescountlist=[]
    openparlist=[]
    closeparlist=[]
    operatorlist=[]
    hashtagcountlist=[]
    dottycountlist=[]
    linkcountlist=[]

    a=0
    #for each cell in the text column of data

    for cell in (data['text']):

        a+=1
        dotcount=0
        commacount=0
        qmarkcount=0
        exclamationcount=0
        wordcount=0
        uppercasecount=0
        lowercasecount=0
        charcount=0
        lr_classifier=0
        specialchar=0
        numbercount=0
        cellwordlist=[]
        uniqueword=0
        qmarkcount=0
        apicescount=0
        quotescount=0
        openparcount=0
        closeparcount=0
        operatorcount=0
        hashtagcount=0
        dottycount=0
        linkcount=0


        dotcount=cell.count(".")
        commacount=cell.count(",")
        exclamationcount=cell.count("!")
        qmarkcount=cell.count("?")
        apicescount=cell.count("'")
        quotescount=cell.count('"')
        openparcount=cell.count('(')
        closeparcount=cell.count(')')
        hashtagcount=cell.count('#')


        if a>10000:
            break
        else:

            #for reach word in cell
            for word in (cell.split()):
                if word in cellwordlist:
                    continue
                else:
                    cellwordlist.append(word)
                    uniqueword+=1
                if re.search('\.\.\.',word):
                    dottycount+=1
                if re.search('http',word):
                    linkcount+=1


                wordcount+=1
                uppercaseword=word[1:]
                for c in uppercaseword:
                    if c.istitle():
                        uppercasecount+=1
                        #print(word)

                for char in word:
                    charcount+=1
                    if re.match("[^a-zA-Z0-9]", char):
                        specialchar+=1
                    if re.match("[0-9]", char):
                        numbercount+=1
                    if char.islower():
                        lowercasecount+=1
                    if re.match("[\+\/\-\*\%\=<>&]", char):
                        operatorcount+=1

            #print(cell)
            #print("Dotcount: " + str((dotcount)))
            #print("Commacount: "+ str(commacount))
            #print("Exclamationcount: "+ str(exclamationcount))
            #print("Wordcount: "+ str(wordcount))
            #print("Uppercasecount "+ str(uppercasecount))
            #print("Charcount "+ str(charcount))
            dotcountlist.append(dotcount)
            commacountlist.append(commacount)
            exclamationcountlist.append(exclamationcount)
            wordcountlist.append(wordcount)
            uppercasecountlist.append(uppercasecount)
            lowercasecountlist.append(lowercasecount)
            charcountlist.append(charcount)
            specialcharlist.append(specialchar)
            numbercountlist.append(numbercount)
            uniquewordlist.append(uniqueword)
            qmarkcountlist.append(qmarkcount)
            apicescountlist.append(apicescount)
            quotescountlist.append(quotescount)
            openparlist.append(openparcount)
            closeparlist.append(closeparcount)
            operatorlist.append(operatorcount)
            hashtagcountlist.append(hashtagcount)
            dottycountlist.append(dottycount)
            linkcountlist.append(linkcount)


    row1=pd.DataFrame()
    row1["Dotcount"]=dotcountlist
    row2=pd.DataFrame()
    row2["Commacount"]=commacountlist
    row3=pd.DataFrame()
    row3["Exclcount"]=exclamationcountlist
    row4=pd.DataFrame()
    row4["Wordcount"]=wordcountlist
    row5=pd.DataFrame()
    row5["Uppercasecount"]=uppercasecountlist
    row6=pd.DataFrame()
    row6["Lowercasecount"]=lowercasecountlist
    row7=pd.DataFrame()
    row7["Specialchar"]=specialcharlist
    row8=pd.DataFrame()
    row8["Numbercount"]=numbercountlist
    row9=pd.DataFrame()
    row9["Charcount"]=charcountlist
    row10=pd.DataFrame()
    row10["Uniquewords"]=uniquewordlist
    row11=pd.DataFrame()
    row11["Qmarkcount"]=qmarkcountlist
    row11=pd.DataFrame()
    row11["Apicescount"]=apicescountlist
    row12=pd.DataFrame()
    row12["Quotescount"]=quotescountlist
    row13=pd.DataFrame()
    row13["Openpar"]=openparlist
    row14=pd.DataFrame()
    row14["Closepar"]=closeparlist
    row15=pd.DataFrame()
    row15["Operatorcount"]=operatorlist
    row16=pd.DataFrame()
    row16["Hashtagcount"]=hashtagcountlist
    row17=pd.DataFrame()
    row17["Dottycount"]=dottycountlist
    row18=pd.DataFrame()
    row18["Linkcount"]=linkcountlist

    output=pd.concat([data, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18],axis=1)



    # In[83]:

    new_datareduced=output.ix[:,[0,2]]
    datareduced=output.ix[:,2:]
    print(datareduced.head(10))
    datareduced.describe()
    c=0
    limit=0
    for column in datareduced:
        limit+=1
    print(limit)
    a=-1
    for column in datareduced:
        lista=[]
        a+=1
        columnmean=((datareduced.ix[:, a]).mean())/datareduced['Charcount'].mean()
        print(column,":" ,columnmean)
        b=-1
        for index, row in (datareduced).iterrows():
            b+=1
            columnval=(datareduced.ix[b, a])
            columnratio=columnval/datareduced.ix[b,'Charcount']
            columnREL=(columnratio/columnmean)
            lista.append(columnREL)
        c+=1
        print(c)
        if c>limit:
            print("Limit!")
            break
        else:
            column = pd.DataFrame({(column+"REL") : lista})
            #print(column)
            new_datareduced=pd.concat([new_datareduced, column], axis=1)
            #print(datareduced)
    print("STOP!")


    # In[84]:

    new_datareduced=new_datareduced.drop("ApicescountREL", axis=1)
    new_datareduced=new_datareduced.drop("botornotREL", axis=1)
    new_datareduced.to_csv('/Users/halukamaier-borst/Documents/CardiffUniversity/Master Thesis/botornot'+day+'REL.csv', encoding='utf-8', index=False)

    # In[ ]:
