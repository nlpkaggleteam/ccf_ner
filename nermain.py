'''
数据的基本处理
'''
import numpy as np
import pandas as pd
import re
def read_data(filename='ccf_ner/test.csv'):
    df=pd.read_csv(filename,delimiter='\t',header=None)

    datalist=df[0].tolist()

    idlist=[]
    contentlist=[]
    relationlist=[]
    name1list=[]
    name2list=[]

    ids=-1
    content=''
    relation=''
    name1=''
    name2=''
    for i in range(len(datalist)):
        if i%2==1:
            relation,name1,name2=parser_relation_name1_name2(datalist[i])
            idlist.append(ids)
            contentlist.append(content)
            relationlist.append(relation)
            name1list.append(name1)
            name2list.append(name2)

        else:
            ids,content=parseid_content(datalist[i])

    idf=pd.DataFrame(idlist,columns=['id'])
    contentdf=pd.DataFrame(contentlist,columns=['content'])
    relationdf=pd.DataFrame(relationlist,columns=['relation'])
    name1df=pd.DataFrame(name1list,columns=['name1'])
    name2df=pd.DataFrame(name2list,columns=['name2'])
    df=pd.concat([idf,contentdf,relationdf,name1df,name2df],axis=1)
    df.to_csv("train_aug.csv",index=False)
def parseid_content(content='8000 "The surgeon cuts a small hole in the skull and lifts the edge of the brain to expose the nerve."'):
    rex=re.compile('\d+ ')
    result=rex.findall(content)

    ids=int(result[0])
    content=rex.sub('',content)

    return ids,content.replace("\"","")
def parser_relation_name1_name2(content='Product-Producer(hole,surgeon)'):
    contentlist=content.split("(")
    namelist=contentlist[1].split(",")
    return contentlist[0],namelist[0],namelist[1][:-1]
def read_testdata(file='ccf_ner/test.csv'):
    df=pd.read_csv(file,delimiter='\t',header=None)
    print(df)
    datalist=df[0].tolist()
    idslist=[]
    contentlist=[]
    for x in datalist:
        ids,content=parseid_content(x)
        idslist.append(ids)
        contentlist.append(content)
    idf=pd.DataFrame(idslist,columns=['id'])
    contentdf=pd.DataFrame(contentlist,columns=['content'])
    df=pd.concat([idf,contentdf],axis=1)
    df.to_csv('test_aug.csv',index=False)



if __name__ == '__main__':
    # read_data()
    parseid_content()
    parser_relation_name1_name2()
    read_testdata()

