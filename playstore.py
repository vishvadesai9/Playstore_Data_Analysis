import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox
import re,pymysql
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import PIL
from PIL import ImageTk, Image
import path
import os
import seaborn as sns
import io 
import math 
from collections import OrderedDict
from datetime import datetime
from datetime import time
from datetime import date
import time
from tkinter.ttk import *   
from tkcalendar import Calendar,DateEntry
import tkinter as tk                 
from tkinter import font  as tkfont 
import matplotlib.style as style  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from string import ascii_letters 
from tkinter.filedialog import asksaveasfile  
from matplotlib.backends.backend_pdf import PdfPages 
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score 
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
from textblob import TextBlob as tb
import openpyxl
from openpyxl import *
import xlrd
import xlsxwriter
from xlutils.copy import copy
pd.options.mode.chained_assignment=None

def adjustWindow(window,screen):
 w = screen.winfo_screenwidth() # width of the screen
 h = screen.winfo_screenheight() # height of the screen
 window.geometry('%dx%d' % (w, h)) # set the dimensions of the screen and where it is placed
 window.resizable(True, True) # disabling the resize option for the window
 window.configure(background='white') # making the background white of the window


 
##=============15================================
def q15():
    global positive,negative,neutral,total_sentiment,positive_percent,neutral_percent,negative_percent
    df = pd.read_excel('googleplaystore_user_reviews.xlsx')
    df=df.dropna()
    df=df[df['App']=='10 Best Foods for You']
    df1=dict(tuple(df.groupby(['Sentiment'])))
    negative=len(df1['Negative'])
    neutral=len(df1['Neutral'])             
    positive=len(df1['Positive'])
    total_sentiment=positive+negative+neutral
    positive_percent=(positive/total_sentiment)*100
    positive_percent=round(positive_percent,2)
    
    neutral_percent=(neutral/total_sentiment)*100
    neutral_percent=round(neutral_percent,2)
    
    negative_percent=(negative/total_sentiment)*100
    negative_percent=round(negative_percent,2)
    

def pie():
    plt.figure(figsize=(8,4))
    figureObject,axesObject=plt.subplots()
    plt.pie(
            [positive,neutral,negative],
            labels=['Positive','Neutral','Negative'],
            colors=['#33cc33','#99ff66','#ccff99'],
            startangle=90,
            autopct='%1.2f'
            )
    axesObject.axis('equal')
    plt.savefig('testplot.png')
    img=Image.open('testplot.png').save('testplot.png','PNG')
    plt.close()


def main15():
    global screen15,p
    screen15=tk.Toplevel(screenr2)
    p=tk.StringVar(master=screen15)
    
    q15()
    pie()
    screen15.title("10 Best foods for you")
    adjustWindow(screen15,screen15) 
    screen15.configure(background='#ffff99')
    
    path = "testplot.png"
    img=Image.open(path)
    img=img.resize((500,400),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen15)
    
    panel = tk.Label(screen15, image = img)

    panel.pack(side = "bottom", fill = "both", expand = "yes")

   
    if (positive_percent>negative_percent) and (positive_percent>neutral_percent):
        p.set(value=positive_percent)
        a1=tk.Label(screen15,text='The App "10 Best Foods for You" has %s positive response.\nLaunching a similar App is advisable since users like such apps.'%(p.get()), width='10', height="8", font=("Calibri", 20,'bold'), fg='black', bg='#ccff66')
        a1.pack(fill=X)

    else:
        a2=tk.Label(screen15,text='The App "10 Best Foods for You" has %s positive response.\nLaunching a similar App is inadvisable since users do not like such apps.'%(p.get()), width='10', height="8", font=("Calibri", 20,'bold'), fg='black', bg='#ccff66')
        a2.pack(fill=X)
        p.set(value=positive_percent)
        a3=tk.Label(screen15,text='%s'%(p.get()))
    b1=tk.Button(screen15, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr2.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen15,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen15.destroy)
    b2.place(x=110,y=0)

 
 
    screen15.mainloop()

##===========================17===============================
def bar():
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()
    df['Size']=df['Size'].str.rstrip('M')

    df['Size']=pd.to_numeric(df['Size'],errors='coerce')

    df.groupby('Installs')["Size"].mean().sort_values(ascending=True).plot(kind='bar',figsize=(10,10),color='#ccccff')
    
    plt.ylabel('Avg.Size(in MB)')
    plt.xlabel('Downloads')
    
    if os.path.isfile('abc.png'):
        os.remove('abc.png')
    plt.savefig('abc.png')
    Image.open('abc.png').save('abc.png','PNG')
    plt.close()



    
    
def main17(): 
    global screen17
    
    screen17=tk.Toplevel(screend1)
    screen17.title("Installs vs App Size")
    adjustWindow(screen17,screen17)

    bar()
    a1=tk.Label(screen17,text='App Downloads and App Size', width='10', height="2", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a1.pack(fill=X)
    path = "abc.png"
    img=Image.open(path)
    img=img.resize((700,700),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen17)
    panel = tk.Label(screen17, image = img)
    panel.place(x=750,y=55)
    b1=tk.Button(screen17, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen17,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen17.destroy)
    b2.place(x=110,y=0)
    a2=tk.Label(screen17, text="Apps which have big size,have more number of installs\n as App having more size are  much better and dynamic.  ", bg='#ccff66', height='2',font=("Calibri", 12, 'bold'))
    a2.place(x=100, y=200)

    
    screen17.mainloop() 

#####============================14=================================
def q14():
    global screen14_1
    if (app.get()=='----Select app----' or app.get()==''or review.get()=='--Select Type--'):
        messagebox.showerror('Select Proper Fields')
    else:
        screen14_1=tk.Toplevel(screen14)
        screen14_1.title('Reviews')
        adjustWindow(screen14_1,screen14_1)
        a1=tk.Label(screen14_1, text="%s\n%s Reviews"%(app.get(),review.get()), width='32', height="2",font=("Calibri", 22, 'bold'), fg='white', bg='#66ff33')
        a1.pack(side='top',anchor='n',fill = X, expand = "yes")
        t=tk.Text(screen14_1)
        reviewlist=[]
        r=tk.StringVar(master=screen14)
        df = pd.read_excel('googleplaystore_user_reviews.xlsx')
        df=df.dropna()
        for i in range(len(df.index)):
            if df.iloc[i].App == app.get():
                if df.iloc[i].Sentiment == review.get():
                    reviewlist.append(df.iloc[i].Translated_Review)
        t=tk.Text(screen14_1,bg='yellow',bd='4',pady='10',height=screen14_1.winfo_screenheight(),relief='groove',wrap='word',font=("Open Sans",10, 'bold'))

        for i in range(len(reviewlist)):
            t.insert(END, str(i+1)+"."+reviewlist[i]+'\n\n')
        t.config(state='disabled')
        t.pack(pady='10')
        b1=tk.Button(screen14_1, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr2.destroy)
        b1.place(x=0,y=0)
        b2=tk.Button(screen14_1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen14_1.destroy)
        b2.place(x=110,y=0)
        screen14_1.mainloop()
    
def main14():
    global app,screen14,review
    screen14=tk.Toplevel(screenr2)
    app =tk.StringVar(master=screen14)
    review=tk.StringVar(master=screen14)

    screen14.title("REVIEWS")
    df = pd.read_excel('googleplaystore_user_reviews.xlsx')
    df=df.dropna()
    
    adjustWindow(screen14,screen14)
    a1=tk.Label(screen14, text="User Reviews ", width='32', height="2",font=("Calibri", 22, 'bold'), fg='white', bg='#66ff33')
    a1.pack(side='top',anchor='n',fill = X, expand = "yes")                         #place(x=(screen14.winfo_screenwidth())/2, y=0)
    a2=tk.Label(screen14, text="App", bg='#ffff00', width='20', height='2',font=("Calibri", 15, 'bold'))
    a2.place(x=400, y=120)

    list1=df['App'].unique().tolist()
    c1=ttk.Combobox(screen14 , width=55, values = list1 ,textvariable = app,)
    c1.place(x=650,y=130)

    app.set('----Select app----')

    a3 = tk.Label(screen14, text="Review", bg='#ffff00', width='20', height='2',font=("Calibri", 15, 'bold'))
    a3.place(x=400, y=200)
    list2=['Positive','Negative','Neutral']
    droplist2=tk.OptionMenu(screen14,review, *list2)
    droplist2.config(width=50)
    review.set('--Select Type--')
    droplist2.place(x=650,y=215)
    
    b1=tk.Button(screen14, text='Submit', width=15 ,height=2,font=("Open Sans", 13, 'bold'), bg='#ff0000',fg='white',command=q14)
    b1.place(x=650, y=490)
    b2=tk.Button(screen14, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr2.destroy)
    b2.place(x=0,y=0)
    b3=tk.Button(screen14,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen14.destroy)
    b3.place(x=110,y=0)
    screen14.mainloop()

#####====================9=======================
def q9():
    global t1
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()

    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    t1=[]
    
    for i in range(len(df.index)):
        if (df.iloc[i].Installs >= 100000) and (df.iloc[i].Rating >=4.1):
            t1.append(df.iloc[i].App)
            

def plot9():
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df.dropna()
    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    data={'Installs':df['Installs'],'Rating':df['Rating']}
    df1=pd.DataFrame(data)
    df1['Installs']=df1['Installs'].str.rstrip('+')

    df1['Installs']=df1['Installs'].str.replace(',','').astype(float)
    df1=df1.sort_values(by='Installs')

    ax=sns.barplot(x=df1['Installs'], y=df1['Rating'],palette='husl')

    plt.xticks(rotation=90)
    ax.set(xlabel='Installs',ylabel='Rating')
    plt.tight_layout()
    plt.savefig('dwnldVsrating.png')
    img=Image.open('dwnldVsrating.png').save('dwnldVsrating.png','PNG')
    plt.close()

    
    
def main9():
    global screen9
    screen9=tk.Toplevel(screenr1)
    adjustWindow(screen9,screen9)
    screen9.title('Downloads and Rating')
    q9()
    plot9()
    path = "dwnldVsrating.png"
    img=Image.open(path)
    img=img.resize((500,350),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen9)
    
    panel = tk.Label(screen9, image = img)
    panel.place(x=50,y=200)
    a1=tk.Label(screen9, text="Apps Having downloads over 1,00,000 and Rating 4.1 and above\n", font=("Open Sans", 12, 'bold'), fg='black',bg='#66ff33')
    a1.place(x=800,y=0)
    a2=tk.Label(screen9,text='Apps having more installs,have comapritively less overall rating\nAs they are diluted by low ratings ',font=("Open Sans", 12, 'bold'), fg='black',bg='#66ff33')
    a2.place(x=60,y=50)
    t=tk.Text(screen9,bg='yellow',bd='4',pady='10',height=screen9.winfo_screenheight(),font=("Open Sans",10, 'bold'))
    for i in range(len(t1)):
        t.insert(END, str(i+1)+"."+t1[i]+'\n\n')
    t.config(state='disabled')
    t.place(x=750,y=50)
    b1=tk.Button(screen9, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen9,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen9.destroy)
    b2.place(x=110,y=0)
    screen9.mainloop()

###======================10==================================
def month(x):
    if x[0:3]=='Jan':
        return 1
    elif x[0:3]=='Feb':
        return 2
    elif x[0:3]=='Mar':
        return 3
    elif x[0:3]=='Apr':
        return 4
    elif x[0:3]=='May':
        return 5
    elif x[0:3]=='Jun':
        return 6
    elif x[0:3]=='Jul':
        return 7
    elif x[0:3]=='Aug':
        return 8
    elif x[0:3]=='Sep':
        return 9
    elif x[0:3]=='Oct':
        return 10
    elif x[0:3]=='Nov':
        return 11
    elif x[0:3]=='Dec':
        return 12



def dates_str_to_int():
    global sample
    sample=sample.set_index("App")
    sample=sample.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    sample=sample.dropna()
    sample['Last Updated'] = sample['Last Updated'].dt.strftime('%d-%b-%y')
    dates=sample['Last Updated']
    

    
    year=[]
    counter=0
    for i in dates:
        year.append([int(i[:-7]),month(i[-6:-3]),int(i[-2:])])
        counter=counter+1
    return year
def install():
    Installs=[]
    global sample
    sample['Installs']=sample['Installs'].str.rstrip('+')
    sample['Installs']=sample['Installs'].str.replace(',','').astype(float)
    sample=sample.dropna()
    for i in sample['Installs']: 
        Installs.append(int(i))
    
        
    return Installs 
def qn10():
    year=dates_str_to_int()
    
    installs=install()
    category=list(OrderedDict.fromkeys(sample['Category']))
    temp=[]
    counter=0
    for i in category:
        temp.append([0,0,0,0,0,0,0,0,0,0,0,0])
    for i in sample['Category']:
        jcounter=0
        for j in category:
            if i==j:
                if year[counter][1]==1:
                    temp[jcounter][0]=temp[jcounter][0]+installs[counter]
                elif year[counter][1]==2:
                    temp[jcounter][1]=temp[jcounter][1]+installs[counter]
                elif year[counter][1]==3:
                    temp[jcounter][2]=temp[jcounter][2]+installs[counter]
                elif year[counter][1]==4:
                    temp[jcounter][3]=temp[jcounter][3]+installs[counter]
                elif year[counter][1]==5:
                    temp[jcounter][4]=temp[jcounter][4]+installs[counter]
                elif year[counter][1]==6:
                    temp[jcounter][5]=temp[jcounter][5]+installs[counter]
                elif year[counter][1]==7:
                    temp[jcounter][6]=temp[jcounter][6]+installs[counter]
                elif year[counter][1]==8:
                    temp[jcounter][7]=temp[jcounter][7]+installs[counter]
                elif year[counter][1]==9:
                    temp[jcounter][8]=temp[jcounter][8]+installs[counter]
                elif year[counter][1]==10:
                    temp[jcounter][9]=temp[jcounter][9]+installs[counter]
                elif year[counter][1]==11:
                    temp[jcounter][10]=temp[jcounter][10]+installs[counter]
                elif year[counter][1]==12:
                    temp[jcounter][11]=temp[jcounter][11]+installs[counter]
            jcounter=jcounter+1
        counter=counter+1
    return temp
def q10_2():
    global sum2,sum1,f1
    df=pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    df=df.dropna()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    d1= (df[(df['Content Rating'] == 'Teen')].Installs).to_list()
    e1= (df[(df['Content Rating'] == 'Mature 17+')].Installs).to_list()
    sum1=sum(d1)
    sum2=sum(e1)
    f1=sum1/sum2
    f1=str(round(f1,2))
    sum1=str(sum1)
    sum2=str(sum2)


def plot10()  :          
    global sample,cat,mon
    sample=pd.read_excel('googleplaystore_App_data.xlsx')#reading data for the data set
    sample=sample.replace(np.NaN,0)
    sample.drop(index=[10474],inplace=True)

    cate_month = qn10()
    dict_month = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June',7:'July',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
    
    categories = []
    months = [] 
    maxinstalls = [] 
    
    cat = sample['Category'].unique()

    for index in range(len(cat)):
        categories.append(cat[index])
        maxinstalls.append(max(cate_month[index]))
        m = (cate_month[index].index(max(cate_month[index]))+1)    
        months.append(dict_month[m])
    
    category_dict=dict(zip(categories,months))

    for key,value in category_dict.items():
        if key=='GAME':
            cat=key
            mon=value
    
    plt.figure(figsize=(15,15))
    plt.plot(categories,maxinstalls)            
    plt.title('CATEGORY vs INSTALLS',fontsize=15)
    plt.xticks(rotation=90)
    plt.xlabel('CATEGORY', fontsize = 15)
    plt.ylabel('INSTALLS', fontsize = 15)
    plt.savefig('q10.png')
    Image.open('q10.png').save('q10.png','PNG')
    plt.close()
#    plt.show()

def main10():
     global screen10
     screen10=tk.Toplevel(screenc1)
     adjustWindow(screen10,screen10)
     screen10.title('Category Installs')
     l1=tk.Label(screen10,text='Category Month', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     l1.pack(fill=X)
     
     plot10()
     q10_2()
     path='q10.png'
     img=Image.open(path)
     img=img.resize((732,588),Image.ANTIALIAS)
     img = ImageTk.PhotoImage(img, master=screen10)
     panel = tk.Label(screen10, image = img)
     panel.place(x=800,y=100)
     txt2='The month of '+mon+' has seen the maximum downloads for '+cat+' category.'
     a1=tk.Label(screen10, text=txt2 , font=('calibri',15,'bold'),fg='black',bg='#ffff00')
     a1.place(x=20,y=120)
     txt4='Number of Teen downloads:  '+sum1+'\n\nNumber of Mature 17+ downloads:  '+sum2+'\n\nRatio of downloads for the app that qualifies as teen versus mature17+ :  '+f1
     a2=tk.Label(screen10, text=txt4 , font=('calibri',15,'bold'),fg='black',bg='#ffff00')
     a2.place(x=20,y=120)
     b1=tk.Button(screen10, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
     b1.place(x=0,y=0)
     b2=tk.Button(screen10,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen10.destroy)
     b2.place(x=110,y=0)
     screen10.mainloop()

###==============================11==========================
def q11():
    global quarter_ans,yr,qr
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    df=df.dropna()
    df=df.reset_index()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(int)
    data={'App':df['App'],'Installs':df['Installs'],'Last':df['Last Updated']}
    df1=pd.DataFrame(data)

    df1['Last']=df['Last Updated'].dt.date
    df1=df1.sort_values(by='Last')

    df1['Last']=df['Last Updated'].dt.to_period('Q')

    c=df1['Last'].to_list()
    uniqueQ=[]
    q={}
    for i in c:
        if i not in uniqueQ:
            uniqueQ.append(i)

    for i in uniqueQ:
    
        df_a=(df1[(df1.Last==i)].Installs).to_list()

        q.update({i:sum(df_a)})
    v=list(q.values())
    k=list(q.keys())
    quarter_ans= k[v.index(max(v))]
    c=str(quarter_ans)
    qr=c[4:]
    yr=c[:4]

    

def main11():
    global screen11
    
    screen11=tk.Toplevel(screend1)
    screen11.title("Quarter")
    adjustWindow(screen11,screen11)
    q11()
    a1=tk.Label(screen11,text='Quarter and Installs', width='10', height="2", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a1.pack(fill=X)
    txt3=qr+' of year '+yr+' has generated the highest number of install for each app used in the study. '
    a2=tk.Label(screen11,text=txt3, width='50', height="50", font=("Calibri", 20,'bold'), fg='black', bg='#174873')
    a2.pack(pady=100,fill=X)
    b1=tk.Button(screen11, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen11,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen11.destroy)
    b2.place(x=110,y=0)
    screen11.mainloop()

###============================12=========================
def q12():
    global p_ans,n_ans,same_ratio
    df=pd.read_excel('googleplaystore_user_reviews.xlsx')    
    df=df.dropna()
    l1=df['App'].unique().tolist()
    positive_dict={}
    negative_dict={}
    same_ratio=[]
    for i in l1:
        x=i
        df1 = df[(df.App ==x) ]
        df1 =df1[(df1.Sentiment=='Positive')]
        df2 = df[(df.App ==x) ]
        df2 =df2[(df2.Sentiment=='Negative')]

        a=len(df1.index)
        b=len(df2.index)
        try:
            c=a/b
        except ZeroDivisionError:
            c=0
        
        positive_dict.update({i:len(df1.index)})
        negative_dict.update({i:len(df2.index)})
        if c==1:
            same_ratio.append(i)
    v=list(positive_dict.values())
    k=list(positive_dict.keys())
    p_ans= k[v.index(max(v))]
    x=list(negative_dict.values())
    y=list(negative_dict.keys())
    n_ans= y[x.index(max(x))]
 
def main12():    
    global screen12
    
    screen12=tk.Toplevel(screens1)
    screen12.title("Category Downloads")
    adjustWindow(screen12,screen12)
    q12()
    a1=tk.Label(screen12,text='Positive and Negative Sentiments', width='10', height="2", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a1.pack(fill=X)
    s1='  App which has generated the most Positive Sentiments :   '+p_ans+'\n\n\nApp which has generated the most Negative Sentiments :   '+n_ans+'\n\n\n'
    l2=tk.Label(screen12,text=s1,width='63',height='20' ,font=("Helvetica",13, 'bold', 'italic'), fg='black', bg='#fa3e3e')
    l2.place(x=80,y=150)
    a2=tk.Label(screen12,text='Apps having same ratio for Positive and Negative Sentiments ', height="2",font=("Calibri", 15,'bold'), fg='black', bg='#5225d9')
    a2.place(x=800,y=80)
    t=tk.Text(screen12,bg='yellow',bd='4',pady='10',padx='20',height=screen12.winfo_screenheight(),font=("Open Sans",10, 'bold'))
    for i in range(len(same_ratio)):
        t.insert(END, str(i+1)+"."+same_ratio[i]+'\n\n')
    t.config(state='normal')
    t.place(x=750,y=150)
    b1=tk.Button(screen12, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screens1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen12,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen12.destroy)
    b2.place(x=110,y=0)
    screen12.mainloop()
#####=============================13============================
def plot13():
    
    df = pd.read_excel('D:\PyInt\googleplaystore_user_reviews.xlsx')

    sns.scatterplot(df['Sentiment_Polarity'],df['Sentiment_Subjectivity'] ,hue=df['Sentiment'], edgecolor='white',palette="husl") 
    plt.xlabel('Sentiment Polarity', fontsize=10) 
    plt.ylabel('Sentiment Subjectivity', fontsize=10) 
    plt.title("Sentiment Analysis", fontsize=10) 
    plt.savefig('q13.png')
    Image.open('q13.png').save('q13.png','PNG')
    plt.close()
def main13():
     global screen13
     screen13=tk.Toplevel(screens1)
     adjustWindow(screen13,screen13)
     screen13.title('Sentiment Analysis')
     l1=tk.Label(screen13,text='Sentiment Polarity and Sentiment Subjectivity', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     l1.pack(fill=X)
     
     plot13()
     
     path='q13.png'
     img=Image.open(path)

     img = ImageTk.PhotoImage(img, master=screen13)
     panel = tk.Label(screen13, image = img)

     panel.pack()

     
     b1=tk.Button(screen13, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screens1.destroy)
     b1.place(x=0,y=0)
     b2=tk.Button(screen13,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen13.destroy)
     b2.place(x=110,y=0)
     screen13.mainloop()
  
#####==========================16============================ 
def plot16():
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()
    data={'Installs':df['Installs'],'Last Updated':df['Last Updated']}
    df1=pd.DataFrame(data)
    df1['Last Updated']=df['Last Updated'].dt.month    

    df1['Installs']=df1['Installs'].str.rstrip('+')
    
    df1['Installs']=df1['Installs'].str.replace(',','').astype(float)
    df1=df1.sort_values(by='Last Updated')

    dict_months={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
 
    sns.set_style("whitegrid") 
    sns.set_context("paper") 
    g=sns.barplot(df1['Last Updated'],df1['Installs'],palette='husl',edgecolor='white')
    g.set(xticklabels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    g.set(xlabel='Months',ylabel='Downloads')
    plt.savefig('dwnldVsmonth.png')
    img=Image.open('dwnldVsmonth.png').save('dwnldVsmonth.png','PNG')
    plt.close()

    
    
def main16():
    global screen16
    screen16=tk.Toplevel(screend1)
    adjustWindow(screen16,screen16) 
    screen16.title('Downloads Vs Months')
    plot16()
    screen16.config(background='#ffff99')
    
    path = "dwnldVsmonth.png"
    img=Image.open(path)
    img=img.resize((500,350),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen16)
    
    panel = tk.Label(screen16, image = img)
       
    a1=tk.Label(screen16,text='July and August is the best indicator to the average downloads \nthat an App will generate over the entire year.', width='50', height="2", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a1.pack(fill=X)
    panel.pack(padx=20,pady=50)
    b1=tk.Button(screen16, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen16,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen16.destroy)
    b2.place(x=110,y=0)
    screen16.mainloop()
  
#####==========================8==========================
def plot1():
    global df_apps
    df_apps=pd.DataFrame()
    df_apps = pd.read_excel('googleplaystore_App_data.xlsx')
    df_apps=df_apps.dropna()
    df_apps = df_apps[(df_apps['Category'] == "SPORTS") |
    (df_apps['Category'] == "ENTERTAINMENT") | (df_apps['Category'] == "SOCIAL")
    | (df_apps['Category'] == "NEWS_AND_MAGAZINES") | (df_apps['Category'] ==
      "EVENTS") | (df_apps['Category'] == "TRAVEL_AND_LOCAL")|
      (df_apps['Category'] == "GAME")]
    df1=df_apps[(df_apps['Category'] == "GAME")]
    df1['Installs']=df1['Installs'].str.rstrip('+')
    df1['Installs']=df1['Installs'].str.replace(',','').astype(float)
    df1['Last Updated']=df_apps['Last Updated'].dt.date
    df1['Last Updated']=df_apps['Last Updated'].dt.year
    a=df1.groupby('Last Updated')["Installs"].mean()
    a.plot(kind='line',figsize=(5,5),color='blue')
    plt.xlabel('Year')
    plt.ylabel('Installs(in 10millions)')
    plt.title('GAME')
    plt.savefig('game.png')
    img=Image.open('game.png').save('game.png')
    plt.close()


    
def plot2():
    df2=df_apps[(df_apps['Category'] == "ENTERTAINMENT")]
    df2['Installs']=df2['Installs'].str.rstrip('+')
    df2['Installs']=df2['Installs'].str.replace(',','').astype(float)
    df2['Last Updated']=df_apps['Last Updated'].dt.date
    df2['Last Updated']=df_apps['Last Updated'].dt.year
    b=df2.groupby('Last Updated')["Installs"].mean()
    b.plot(kind='bar',figsize=(5,5),color='red')   
    plt.xlabel('Year')
    plt.ylabel('Installs(in 10millions)') 
    plt.title('ENTERTAINMENT')
    plt.savefig('entertainment.png')
    img=Image.open('entertainment.png').save('entertainment.png') 
    plt.close()

    
def plot3():
    df2=df_apps[(df_apps['Category'] == "EVENTS")]

    df2['Installs']=df2['Installs'].str.rstrip('+')
    df2['Installs']=df2['Installs'].str.replace(',','').astype(float)
    df2['Last Updated']=df_apps['Last Updated'].dt.date
    df2['Last Updated']=df_apps['Last Updated'].dt.year
    c=df2.groupby('Last Updated')["Installs"].mean()
    c.plot(kind='bar',figsize=(5,5),color='red')   
    plt.xlabel('Year')
    plt.ylabel('Install')
    plt.title('EVENTS')
    plt.savefig('events.png')
    img=Image.open('events.png').save('events.png')
    plt.close()

def text_parameters(i):
 df_apps = pd.read_excel('googleplaystore_App_data.xlsx')

 df_apps=df_apps.dropna()
 df_apps['Installs']=df_apps['Installs'].str.rstrip('+')
 df_apps['Installs']=df_apps['Installs'].str.replace(',','').astype(float)
 


 text=[]
 cor1=[]
 cor2=[]

 if i==1:

     df_apps = df_apps[(df_apps['Category'] == "SPORTS") |
    (df_apps['Category'] == "ENTERTAINMENT") | (df_apps['Category'] == "SOCIAL")
    | (df_apps['Category'] == "NEWS_AND_MAGAZINES") | (df_apps['Category'] ==
      "EVENTS") | (df_apps['Category'] == "TRAVEL_AND_LOCAL")|
      (df_apps['Category'] == "GAME")]
 else:
     pass


 df_apps.dtypes
 df_apps["Type"] = (df_apps["Type"] == "Paid").astype(int)
 corr = df_apps.apply(lambda x: x.factorize()[0]).corr()

 for i in df_apps.columns:
     for j in df_apps.columns:
         if corr[i][j]<(-0.25):
             cor1.append(i)
             cor2.append(j)
 cor1=np.array(cor1)
 strong_cor=list(np.unique(cor1))

 df_apps['Size'].replace('Varies with device', np.nan, inplace=True)

 df_apps=df_apps.dropna(how='any',axis=0)
 df_apps['Size']=df_apps['Size'].str.rstrip('M,k')
 df_apps['Size']=df_apps['Size'].astype(float)

 popAppsCopy = df_apps.copy() 
 label_encoder = preprocessing.LabelEncoder()

 df_app=[]
 popAppsCopy['Category']=label_encoder.fit_transform(popAppsCopy['Category'])

 popAppsCopy['Category']=label_encoder.inverse_transform(popAppsCopy['Category'])
 df_app=list(df_apps['Category'])
 popAppsCopy['Category']=label_encoder.fit_transform(popAppsCopy['Category'])
 popAppsCopy['Content Rating']=label_encoder.fit_transform(popAppsCopy['Content Rating'])
 popAppsCopy['Genres']=label_encoder.fit_transform(popAppsCopy['Genres'])
 popAppsCopy.dtypes

 popAppsCopy = popAppsCopy.drop(["App","Last Updated","Current Ver","Android Ver"],axis=1)

 countPop = popAppsCopy[popAppsCopy["Installs"] > 100000].count()
 popular_apps="{} Apps are Popular!".format(countPop[0])

 popAppsCopy["Installs"] = (popAppsCopy["Installs"] > 100000)*1

 testPop1 = popAppsCopy[popAppsCopy["Installs"] ==1].sample(1010,random_state=0)
 popAppsCopy = popAppsCopy.drop(testPop1.index)


 testPop0 = popAppsCopy[popAppsCopy["Installs"] ==0].sample(0,random_state=0)
 popAppsCopy = popAppsCopy.drop(testPop0.index)

 testDf = testPop1.append(testPop0)
 trainDf = popAppsCopy
 testDf = testDf.sample(frac=1,random_state=0).reset_index(drop=True)
 trainDf = trainDf.sample(frac=1,random_state=0).reset_index(drop=True)
 y_train = trainDf.pop("Installs")
 X_train = trainDf.copy()
 y_test = testDf.pop("Installs")
 X_test = testDf.copy()
 popularity_classifier = DecisionTreeClassifier(max_leaf_nodes=29,random_state=0)
 popularity_classifier.fit(X_train, y_train)

 predictions = popularity_classifier.predict(X_test)

 accuracy_score(y_true = y_test, y_pred = predictions)
 accuracy=(accuracy_score(y_true = y_test, y_pred = predictions))
 accuracy=100*accuracy

 X_testCopy = X_test.copy()
 X_testCopy["Popular?"] = y_test

 d=list(popAppsCopy['Category'])
 list1=X_testCopy[X_testCopy["Popular?"] ==1]['Category'].unique()
 list2=[None]*len(list1)

 for i in list1:
     list2[i]=df_app[d.index(i)]
 list2=list(filter(None,list2))
 list2=np.array(list2)
 popular_categories=list(np.unique(list2))
 text=""
# print(len(strong_cor))
 for a in strong_cor:
     text= text + str(a) + ", "
 text= "" +str(popular_apps) + " among all. Therefore, with an accuracy of " +str(accuracy) +"%. \n"
 for a in popular_categories:
     text=text + str(a)+','
 text=text+ " categories are trending."


 return text

def main8():
    global screen8
    screen8=tk.Toplevel(screenc1)
    adjustWindow(screen8,screen8)
    screen8.title('Prediction')
    ans=text_parameters(1)
    plot1()
    plot2()
    plot3()
    a1=tk.Label(screen8, text='CATEGORY PREDICTION', font=("Open Sans", 12,'bold'), fg='black',bg='#ffff00')
    a1.pack(side=TOP,fill=X)
    a2=tk.Label(screen8, text=ans, font=("Open Sans", 12,'bold'), fg='black',bg='#66ff33')
    a2.pack(side=TOP,pady=5,fill=X)
    a3=tk.Label(screen8, text='Amongst sports, entertainment,social media,news,events,travel and games. \n\nGAME Category has the most steady growth in recent years.\nHence is most likely to be downloaded in the coming years.', font=("Open Sans", 12,'bold'), fg='black',bg='#66ff33')
    a3.pack(side=TOP,pady=20,fill=X)     
    path1 = "game.png"
    img1=Image.open(path1)
    img1 = ImageTk.PhotoImage(img1, master=screen8)
    panel1 = tk.Label(screen8, image = img1)
    panel1.place(x=50,y=250)
    
    path2 = "entertainment.png"
    img2=Image.open(path2)
    img2 = ImageTk.PhotoImage(img2, master=screen8)
    panel2 = tk.Label(screen8, image = img2)
    panel2.place(x=540,y=250)
    
    path3 = "events.png"
    img3=Image.open(path3)
    img3 = ImageTk.PhotoImage(img3, master=screen8)
    panel3 = tk.Label(screen8, image = img3)
    panel3.place(x=1030,y=250)   
    b1=tk.Button(screen8, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen8,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen8.destroy)
    b2.place(x=110,y=0)
    screen8.mainloop()

###===============================7========================
def plot7():
    
    df= pd.read_excel('googleplaystore_App_data.xlsx')

    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    
    df=df.dropna()

    Installs=[]
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    df=df.dropna()

    for i in df['Installs']: 
        Installs.append(int(i)) 
   
    

    
    n=df['Android Ver']
    s=Installs
    num=['V','A']
    v=[None]*len(n)
    d=[None]*len(n)
    for i in range(0,len(n)):
        if re.search('^V',str(n[i])):
            
            v[i]=s[i]
        else:
            
           d[i]=s[i]

        
    a=[None]*2
    a[0]=sum(list(filter(None, v)))
    a[1]=sum(list(filter(None, d)))
    g=sns.barplot(x=a, y=num, palette='husl')
    plt.title('Android Version type vs. downloads',fontsize=10)
    plt.xlabel('Installs', fontsize = 10)
    plt.ylabel('Android Version', fontsize = 10)
    
    fig=g.get_figure()
    fig.savefig('a.png')
    Image.open('a.png').save('a.png','PNG')
    plt.close()
    
def q7():
    global percent_increase
    df= pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    
    df=df.dropna()
    df=df.reset_index()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    df=df.dropna()
    data={'App':df['App'],'andv':df['Android Ver'],'Installs':df['Installs']}
    df1=pd.DataFrame(data)
    df1 = df1[(df1.andv =='Varies with device') ]
    list1=[]
    for i in df1['Installs']:
        list1.append(i)
    var1=sum(list1)
    
    df2=pd.DataFrame(data)
    df2 = df2[(df2.andv !='Varies with device') ]
    list2=[]
    for i in df2['Installs']:
        list2.append(i)
    var2=sum(list2)
    
    percent_increase=((var1-var2)/(var1+var2))*100



    
def main7(): 
    global screen7
    
    screen7=tk.Toplevel(screent1)
    screen7.title("Installs vs App Size")
    adjustWindow(screen7,screen7)
    plot7()
    q7()
    l2=tk.Label(screen7,text='App Version And Installs', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    l2.pack(fill=X)
    path = "a.png"
    img=Image.open(path)
    img=img.resize((650,650),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen7)
    panel = tk.Label(screen7, image = img)
    panel.place(x=100,y=150)
    s11=round(percent_increase,1)
    l1=tk.Label(screen7,text='All those apps , whose android version is not an issue and can work with varying devices.\nThere is {0}% increase  in downloads'.format(s11), font=("Calibri", 12,'bold'), fg='white', bg='#3d04cf')
    l1.place(x=800,y=250)
    b1=tk.Button(screen7, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen7,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen7.destroy)
    b2.place(x=110,y=0)
    
    screen7.mainloop()
###==========================19================
def Content():
    df=pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()
    a=sns.countplot(x=df['Content Rating'],data=df,palette='pink')
    a.set_xticklabels(a.get_xticklabels(),rotation=90,ha='right')
    plt.ylabel('App Counts')
    plt.title('Content Rating distribution',size=20)
    
    if os.path.isfile('python5.png'):
       os.remove('python5.png')
    plt.savefig('python5.png',bbox_inches='tight')
    Image.open('python5.png').save('python5.png','PNG')
    plt.close()
   

def main19(): 
   global screen19
   
    
   screen19=tk.Toplevel(screenr1)
   screen19.title("Content Rating distribution")
   adjustWindow(screen19,screen19)
#    frame=Frame(screen01)
   l1=tk.Label(screen19,text='Content Rating ', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
   l1.pack(fill=X)
   Content()
   path = "python5.png"
   img=Image.open(path)

   img=img.resize((600,600),Image.ANTIALIAS)
   img = ImageTk.PhotoImage(img, master=screen19)
    
   panel = tk.Label(screen19, image = img)
   panel.pack(side = "bottom", fill = "both", expand = "yes")
   b1=tk.Button(screen19, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr1.destroy)
   b1.place(x=0,y=0)
   b2=tk.Button(screen19,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen19.destroy)
   b2.place(x=110,y=0)
    
   screen19.mainloop() 

####====================20========================

def q20():
    df=pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()
    labels=df['Type'].value_counts(sort=True).index
    sizes=df['Type'].value_counts(sort=True)
    colors=['palegreen','orangered']
    explode=(0.1,0)
    plt.rcParams['figure.figsize']=8,10
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.0f%%',shadow=True,startangle=270)
    plt.title('Percentage of Free and Paid App in store',size=20)
    plt.savefig('freepaid20.png',bbox_inches='tight')
    Image.open('freepaid20.png').save('freepaid20.png','PNG')
    plt.close()
    

def main20():
   global screen20
   
    
   screen20=tk.Toplevel(screent1)
   screen20.title("App types")
   adjustWindow(screen20,screen20)

   l1=tk.Label(screen20,text='Free and Paid Apps', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
   l1.pack(fill=X)
   q20()
   path = "freepaid20.png"
   img=Image.open(path)


   img = ImageTk.PhotoImage(img, master=screen20)
    
   panel = tk.Label(screen20, image = img)

   panel.pack(side = "bottom", fill = "both", expand = "yes")

   b1=tk.Button(screen20, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
   b1.place(x=0,y=0)
   b2=tk.Button(screen20,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen20.destroy)
   b2.place(x=110,y=0)
    
   screen20.mainloop()

####=========================1==========================
def q1():
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df3 = df['Category'].value_counts()
    df3 = df3.reset_index()
    df3 = df3[:30]
    plt.figure(figsize=(30,15))
    plt.pie(x = list(df3['Category']), labels=list(df3['index']), autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.2)
    plt.title('% Installation of apps of different catrgory')
    plt.savefig('q1.png')
    Image.open('q1.png').save('q1.png','PNG')
    plt.close()
#    plt.show()


def main1():
    global screen1
    screen1=tk.Toplevel(screenc1)
    screen1.title("DOWNLOAD SECTION")
    adjustWindow(screen1,screen1)    
    q1()
    a1=tk.Label(screen1, text="PERCENTAGE DOWNLOAD IN EACH CATEGORY", font=('calibri',22,'bold'),fg='white',bg='#66ff33')
    a1.pack(fill=X)
    path = "q1.png"
    img=Image.open(path)
    img=img.resize((1960,880),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen1)
    panel = tk.Label(screen1, image = img)
    panel.pack(pady=60) 
    b1=tk.Button(screen1, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen1.destroy)
    b2.place(x=110,y=0)
    screen1.mainloop()

#####===========================2==============================
def main2():
    global screen2
    df = pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.set_index("App")
    df=df.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    df.dropna()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    screen2=tk.Toplevel(screend1)
    screen2.title("DOWNLOAD SECTION")
    adjustWindow(screen2,screen2)    
    a=df.Installs.value_counts()[10000.0]    #No of apps having downloads between 10 thousand and 50 thousand are
    b=df.Installs.value_counts()[50000.0]
    b1=df.Installs.value_counts()[100000.0]   #No of apps having download between 1.5 lakh and 5 lalkh are
    b2=b+b1                    #No of apps having downloads between 50k and 1.5 lakh are
    c=df.Installs.value_counts()[500000.0]
    d=df.Installs.value_counts()[1000000.0]
    e=c+d             #No apps having downloads between 5 lakh and 50 lakh are
    f=df.Installs.value_counts()[5000000.0]
    g=df.Installs.value_counts()[10000000.0]
    h=df.Installs.value_counts()[50000000.0]
    i=df.Installs.value_counts()[100000000.0]
    j=df.Installs.value_counts()[500000000.0]
    k=df.Installs.value_counts()[1000000000.0]
    l=f+g+h+i+j+k        #"No of apps having downloads more than 50 lakhs are
    a1=tk.Label(screen2, text="NUMBER OF DOWNLOADS", font=('calibri',22,'bold'),fg='black',bg='#66ff33',height='2')
    a1.pack(fill=X)
    a2=tk.Label(screen2, text='Number of apps having downloads between 10,000 and 50,000 are:  %d \n\n Number of apps having downloads between 50000 and 150000 are:   %d\n\n Number of apps having download between 150000 and 500000 are:  %d \n\n Number apps having downloads between 500000 and 5000000 are:  %d \n\n Number of apps having downloads more than 5000000 are: %d'%(a,b,b1,e,l),width='80',height='30' ,font=("Helvetica",10, 'bold', 'italic'), fg='black', bg='#ffff4d')
    a2.pack(pady=50)
    b1=tk.Button(screen2, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen2,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen2.destroy)
    b2.place(x=110,y=0)
    screen2.mainloop()

###=================================3========================
def q3():
    global most_ans,least_ans,avg_list
    df = pd.read_excel('googleplaystore_App_data.xlsx')

    df=df.dropna()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(int)

    alist=df['Category'].unique().tolist()
    most_dict={}
    avg_dict={}
    avg_list=[]
    for i in alist:
    
        df1=df[(df.Category==i)]

        c=[]   
        for j in df1['Installs']:
            c.append(j)
        most_dict.update({i:sum(c)})
        if (sum(c)/len(c))>=250000:
            avg_dict.update({i:sum(c)/len(c)})
    v=list(most_dict.values())
    k=list(most_dict.keys())
    most_ans= k[v.index(max(v))]
    least_ans= k[v.index(min(v))]

    for i in avg_dict:
        avg_list.append(i)


def main3():
    global screen3
    
    screen3=tk.Toplevel(screenc1)
    screen3.title("Category Downloads")
    adjustWindow(screen3,screen3)
    q3()
    a1=tk.Label(screen3,text='Category with Most,Least and Average Downloads', width='10', height="2", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a1.pack(fill=X)
    s1='  Most Downloaded Category:   '+most_ans+'\n\n\nLeast Downloaded Category:   '+least_ans+'\n\n\n'
    l2=tk.Label(screen3,text=s1,width='50',height='20' ,font=("Helvetica",16, 'bold', 'italic'), fg='black', bg='#fa3e3e')
    l2.place(x=80,y=150)
    a2=tk.Label(screen3,text='Categories with an average downloads of atleast 2,50,000 ', height="2",font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    a2.place(x=800,y=80)
    t=tk.Text(screen3,bg='yellow',bd='4',pady='10',padx='20',height=screen3.winfo_screenheight(),font=("Open Sans",10, 'bold'))
    for i in range(len(avg_list)):
        t.insert(END, str(i+1)+"."+avg_list[i]+'\n\n')
    t.config(state='normal')
    t.place(x=750,y=150)
    b1=tk.Button(screen3, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen3,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen3.destroy)
    b2.place(x=110,y=0)
    screen3.mainloop()
#####==============================4==============================
def avgRatings():
    global list1
    df1 = pd.read_excel('googleplaystore_App_data.xlsx')
    df1=df1.set_index("App")
    df1=df1.drop('Life Made WI-Fi Touchscreen Photo Frame',axis=0)
    df1.dropna()
    data={'Category':df1['Category'],'Rating':df1['Rating']}
    df=pd.DataFrame(data)
    
    df=df.dropna()
    ratings={}
    for j in df['Category']:
            k=j
            t2=(df[(df.Category==k)].Rating).tolist()
            ratings.update({j:float(sum(t2)/len(t2))}) 

    list1=[]
    for key,value in ratings.items():
        if value>4.35:
            list1.append(key)

    key = []
    value=[]
    for i in ratings.keys():
        key.append(i)
    for i in ratings.values():
        value.append(i)
    plt.figure(figsize=(15,15))
    plt.ticklabel_format(style='plain', axis='x',)
    dft = pd.DataFrame(dict(category=key, rating=value))
    plt.xticks(rotation=90)
    an=sns.barplot("category","rating",data=dft)
    an.tick_params(axis='both', which='major', labelsize=10)
    for p in an.patches:
      an.annotate(format(p.get_height(), '.1f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 12),rotation=90,fontsize=10, textcoords = 'offset points')
    plt.title("Sentiment Of The Apps")
    plt.savefig('q4.png')
    Image.open('q4.png').save('q4.png','PNG')
    plt.close()
    


def main4():
    global screen4
    screen4=tk.Toplevel(screenr1)
    adjustWindow(screen4,screen4)
    screen4.title('CATEGORY AND RATING')
    avgRatings()
    txt=''
    for i in list1:
        txt=txt+i+','
    txt2=txt+'Category of apps have managed to get\n the highest maximum average ratings from the users.'
    a1=tk.Label(screen4, text=txt2 , font=('calibri',12,'bold'),fg='black',bg='#ffff00')
    a1.place(x=20,y=120)
    a2=tk.Label(screen4, text= "AVERAGE RATING OF EACH CATEGORY", font=('calibri',22,'bold'),fg='black',bg='#66ff33')
    a2.pack(fill=X)
    path = "q4.png"
    img=Image.open(path)
    img=img.resize((804,704),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen4)
    panel = tk.Label(screen4, image = img)
    panel.place(x=600,y=100)   
    b1=tk.Button(screen4, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen4,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen4.destroy)
    b2.place(x=110,y=0)
    screen4.mainloop()

###=============================5================================
def q5():
    global a,b,c
    df= pd.read_excel('googleplaystore_App_data.xlsx')
    df=df.dropna()
    df['Installs']=df['Installs'].str.rstrip('+')
    df['Installs']=df['Installs'].str.replace(',','').astype(float)
    df['Size']=df['Size'].str.rstrip('M')

    df['Size']=pd.to_numeric(df['Size'],errors='coerce')
    x = [10,20,30,100]
    df['Size']=df['Size'].astype(float)
    t1=(df[(10.0<=df.Size) & (df.Size<20.0)].Installs).tolist()
    t2=(df[(20.0<=df.Size) & (df.Size<30.0)].Installs).tolist()
    t3=(df[(30.0<=df.Size) & (df.Size<100.0)].Installs).tolist()
    a=str(int(sum(t1)))
    b=str(int(sum(t2)))
    c=str(int(sum(t3)))
    

    df['Size'] = pd.cut(df['Size'],x)

    df=df.dropna()
    
    df.dtypes
    g=sns.barplot(x=df['Size'],y=df['Installs'],data=df,palette="Blues_d")
    plt.ylabel('Installs (in 10millions)')
    plt.xlabel('Size (in Mb)')

    fig=g.get_figure()
    fig.savefig('q5.png')
    Image.open('q5.png').save('q5.png','PNG')
    plt.close()
   
    
def main5():
    global screen5
    screen5=tk.Toplevel(screend1)
    adjustWindow(screen5,screen5)
    screen5.title('App Size')
    q5()
    l1=tk.Label(screen5,text='Installs and App Size', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
    l1.pack(fill=X)
    path = "q5.png"
    img=Image.open(path)
    img=img.resize((632,488),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master=screen5)
    panel = tk.Label(screen5, image = img)
    panel.place(x=800,y=200)
    s1='Number of Installs for apps having Size between 10Mb and 20 Mb:   '+a+'\n\nNumber of Installs for apps having Size between 20Mb and 30 Mb:   '+b+'\n\nNumber of Installs for apps having Size more than 30MB:     '+c
    l2=tk.Label(screen5,text=s1,width='80',height='30' ,font=("Helvetica",10, 'bold', 'italic'), fg='black', bg='#ffff4d')
    l2.place(x=100,y=200)
    b1=tk.Button(screen5, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
    b1.place(x=0,y=0)
    b2=tk.Button(screen5,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen5.destroy)
    b2.place(x=110,y=0)
    screen5.mainloop()

###=======================6========================
def q6():
    plt.rcParams['figure.figsize']=(8,10)
    df=pd.read_excel('D:\PyInt\googleplaystore_App_data.xlsx')
    df=df.dropna()
    d = pd.DatetimeIndex(df['Last Updated'])
    df['year'] = d.year
    df['month'] = d.month

    categories = list(df["Category"].unique())
    app=[None]*len(categories)
    sum1=[None]*len(categories)
    perc=[None]*len(categories)
    most=[None]*len(categories)
    least=[None]*len(categories)
    recent_year=np.array(df['year'].unique())
    a=[]
    a=recent_year[(recent_year > 2015)]

    c=["#ed3a2d","#001aff","#69fa5f","pink","orange"]
    for y in range(0,len(a)):
        for k in range(0,len(categories)):
            app[k]=df[(df['Category'] == categories[k]) & (df['year']== a[y])]
        
        for i in range (0,len(categories)):

            sum1[i]=(np.sum(app[i].shape[0]))

        m1=max(sum1)
        for i in range (0,len(categories)):
        
            perc[i]=(sum1[i]*100/m1)
     
            j=0
            k=0
            l=0

        for i in range(0,len(categories)):
            if(perc[i]<50):
                least[j]=categories[i]
                j+=1
 

            elif(perc[i]>=50):
                most[l]=categories[i]
                l+=1

            else:
                pass
 

        sm=plt.scatter(perc,categories,color=c[y],s=100,label=a[y])

    plt.grid(True)
    plt.title('Number of Apps installed based on Category',fontsize=10)
    plt.legend(loc="upper right")

    plt.xlabel('Installs', fontsize = 10)
    plt.ylabel('Categories', fontsize = 10)
    plt.savefig('mostleast.png',bbox_inches='tight')
    Image.open('mostleast.png').save('mostleast.png','PNG')
    plt.close()

def main6():
   global screen6
   
    
   screen6=tk.Toplevel(screenc1)
   screen6.title("Downloads")
   adjustWindow(screen6,screen6)

   l1=tk.Label(screen6,text='Category and Downloads', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
   l1.pack(fill=X)
   q6()
   path = "mostleast.png"
   img=Image.open(path)

   img = ImageTk.PhotoImage(img, master=screen6)
    
   panel = tk.Label(screen6, image = img)
   panel.place(x=800,y=100)
   s1='Most Downloaded Category\n\n            2016:  FAMILY\n         2017:  GAME\n         2018:   GAME\n\nLeast Downloaded Category\n\n    2016:  WEATHER\n              2017:  ENTERTAINMENT\n                       2018:   LIBRARIES_AND_DEMO'
   l2=tk.Label(screen6,text=s1,width='80',height='30' ,font=("Helvetica",10, 'bold', 'italic'), fg='black', bg='#ffff4d')
   l2.place(x=100,y=200)
   b1=tk.Button(screen6, text="HOME",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
   b1.place(x=0,y=0)
   b2=tk.Button(screen6,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen6.destroy)
   b2.place(x=110,y=0)
   screen6.mainloop()

###=======================add data===================
    
global dfbb
dfbb = pd.read_excel('googleplaystore_App_data.xlsx')
dfbb=dfbb.dropna()
def get_len1():
    global row1,col1
    wb=xlrd.open_workbook('googleplaystore_App_data.xlsx')

    w_sheet=wb.sheet_by_index(0)
    row1=w_sheet.nrows
    col1=w_sheet.ncols

def save_data1():
    if android_ver1.get()=="":
        messagebox.showerror('Enter Android Version',parent=screen18)
        return
    elif rating.get() == '' or float(rating.get())>5.0:
        messagebox.showerror('Enter Valid Number',parent=screen18)
        return
    elif review_no.get()=='' or review_no.get().isdigit()!=True:
        messagebox.showerror('Enter Valid Number',parent=screen18)
        return
        
    elif size_app.get() == '' or size_app.get().isdigit()!=True:
        messagebox.showerror('Enter Valid App Size',parent=screen18)
        return
    elif size_unit.get()!='k' and size_unit.get()!='M' and size_unit.get()!='G':
        messagebox.showerror('Enter Valid App Size Unit',parent=screen18)
        return
    elif price.get() =='' or price.get().isdigit()!= True or price.get()!='0':
        messagebox.showerror('Enter Valid App Price',parent=screen18)
        return
    try:
        appsize=str(size_app.get())+str(size_unit.get())
        lastDateObj = datetime.strptime(last_update.get(), '%d/%m/%Y')
        lastDateObj=datetime.strftime(lastDateObj, '%d-%b-%y')
        lastDateObj=datetime.strptime(lastDateObj, '%d-%b-%y')
        if price.get()!='0':
            priced='$'+price.get()
        else:
            priced=price.get()
        if android_ver1.get()!='Varies with device':
            if android_ver2.get()=='and up':
                andver=android_ver1.get()+' '+android_ver2.get()
            else:
                andver=android_ver1.get()+'-'+android_ver2.get()
        else:
            andver=android_ver1.get()
        
    
    
        get_len1()
        r=int(row1+1)
        wb=openpyxl.load_workbook('googleplaystore_App_data.xlsx')

    
        w_sheet=wb['in']
    
        insert=(app_name.get(),category.get(),rating.get(),review_no.get(),appsize,install_no.get(),type_app.get(),priced,content_rating.get(),genre.get(),lastDateObj,curr_ver.get(),andver)

        w_sheet.append(insert)
        wb.save('googleplaystore_App_data.xlsx')
        messagebox.showinfo("Save" , "Success!",parent=screen18)
        appNameEntry.config(state='normal')
        app_name.set('')
        reviewNoEntry.config(state='disabled')
        review_no.set('0')
        appSizeEntry.config(state='disabled')
        size_app.set('0')
        priceEntry.config(state='disabled')
        price.set('0')
        currentVerEntry.config(state='disabled')
        androidVerEntry1.config(state='disabled')
        androidVerEntry2.config(state='disabled') 
        droplist_cat.config(state='disabled')
        category.set('----Select App Category----')
        rate.config(state='disabled')
        rating.set('0.0')
        droplist_inst.config(state='disabled')
        install_no.set('----Select App Installs----')
        droplist_content.config(state='disabled')
        content_rating.set('----Select Content Rating----')
        droplist_genre.config(state='disabled')
        genre.set('----Select Genre----')
        unit_option.config(state='disabled')
        size_unit.set('M')
        b1.config(state='disabled')
        type_app.set("Free")
        last_update.set('01/01/2020')
        android_ver2.set('and up')
    except Exception as e:
     print(e)
     messagebox.showerror("Save" ,"Failed to save!",parent=screen18)
#  If error on saving , shows error message.
     

def main18_app():
    global app_name,category,rating,review_no,size_app,install_no,type_app,price,content_rating,genre,last_update,curr_ver,size_unit,b1
    global android_ver1,android_ver2,appNameEntry,droplist_cat,rate,reviewNoEntry,appSizeEntry,unit_option,droplist_inst,priceEntry,screen18
    global droplist_content,droplist_genre,currentVerEntry,androidVerEntry1,androidVerEntry2
    screen18=tk.Toplevel(screena1)
    screen18.title("App Data")
    l0=tk.Label(screen18,text='Add App Data',fg='black', bg='#66ff33', width='10',height='2',font=("Calibri", 15,'bold'))
    l0.pack(fill=X)
    adjustWindow(screen18,screen18)
    mainframe=tk.Frame(screen18,bg='white')
    mainframe.pack(pady='15')
    
    
    mainframe.pack()
    app_name=tk.StringVar(master=screen18)
    category=tk.StringVar(master=screen18)
    rating=tk.StringVar(master=screen18)
    review_no=tk.StringVar(master=screen18)
    size_app=tk.StringVar(master=screen18)
    install_no=tk.StringVar(master=screen18)
    type_app=tk.StringVar(master=screen18)
    price=tk.StringVar(master=screen18)
    content_rating=tk.StringVar(master=screen18)
    genre=tk.StringVar(master=screen18)
    last_update=tk.StringVar(master=screen18)
    curr_ver=tk.StringVar(master=screen18)
    android_ver1=tk.StringVar(master=screen18)
    android_ver2=tk.StringVar(master=screen18)
    size_unit=tk.StringVar(master=screen18)
    

    
    appNameEntry = tk.Entry(mainframe, width=20, textvariable=app_name)                      
    appNameEntry.grid(row=0, column=1 ,padx=5, pady=5)                                     
    appNameEntry.bind("<Return>", lambda event: validate(event, "App Name"))
    appNameEntry.bind("<Tab>", lambda event: validate(event, "App Name"))
    appNameEntry.focus_set()
    
    category_list=dfbb['Category'].unique().tolist()
    droplist_cat=tk.OptionMenu(mainframe,category, *category_list)
    droplist_cat.config(width=50)
    category.set('----Select App Category----')
    droplist_cat.grid(row=1,column=1,padx=5,pady=5)
    droplist_cat.bind("<Return>", lambda event: validate(event, "App Category"))
    droplist_cat.bind("<Tab>", lambda event: validate(event, "App Category"))

    choices=[]   
    [choices.append(i/10) for i in range(0,51)]
    rate=ttk.Combobox(mainframe , width=5, values = choices ,textvariable = rating)
    rate.grid(row=2, column=1, padx=5, pady=5)
    rating.set('0.0')
    
    
    reviewNoEntry = tk.Entry(mainframe, width=20, textvariable=review_no)
    review_no.set('0')
    reviewNoEntry.grid(row=3, column=1 ,padx=5, pady=5)
    reviewNoEntry.bind("<Return>", lambda event: validate(event, "Review NO"))
    reviewNoEntry.bind("<Tab>", lambda event: validate(event, "Review NO"))
    
    sizeframe=tk.Frame(mainframe)
    appSizeEntry = tk.Entry(sizeframe, width=20, textvariable=size_app)
    appSizeEntry.grid(row=0, column=1 ,padx=5, pady=5)
    size_app.set('0')
    appSizeEntry.bind("<Return>", lambda event: validate(event, "App Size"))
    appSizeEntry.bind("<Tab>", lambda event: validate(event, "App Size"))
    unit=['k','M','G']
    unit_option=ttk.Combobox(sizeframe,width=5,values=unit,textvariable=size_unit)
    unit_option.grid(row=0,column=2,padx=5,pady=5)
    size_unit.set('M')
    unit_option.bind("<Return>", lambda event: validate(event, "Size Unit"))
    unit_option.bind("<Tab>", lambda event: validate(event, "Size Unit"))

    sizeframe.grid(row=4,column=1,padx=5,pady=5)
    unit_option.config(state='disabled')
    
    installs_list=dfbb['Installs'].unique().tolist()
    droplist_inst=tk.OptionMenu(mainframe,install_no, *installs_list)
    droplist_inst.config(width=50)
    install_no.set('----Select App Installs----')
    droplist_inst.grid(row=5,column=1,padx=5,pady=5)
    
    droplist_inst.bind("<Return>", lambda event: validate(event, "App Installs"))
    droplist_inst.bind("<Tab>", lambda event: validate(event, "App Installs"))

    
    typeFrame = tk.Frame(mainframe)
    freerad1=ttk.Radiobutton(typeFrame, text="Free" ,variable=type_app,value="Free")
    freerad1.grid(row=0, column=1, padx=5, pady=5)
    freerad1.bind("<Return>", lambda event: validate(event, "Free"))
    freerad1.bind("<Tab>", lambda event: validate(event, "Free"))
    freerad1.bind("<ButtonRelease-1>", lambda event: validate(event, "Free"))
    freerad2=ttk.Radiobutton(typeFrame, text="Paid" ,variable=type_app,value="Paid")
    freerad2.grid(row=0, column=2, padx=5, pady=5)
    freerad2.bind("<Return>", lambda event: validate(event, "Paid"))
    freerad2.bind("<Tab>", lambda event: validate(event, "Paid"))
    freerad2.bind("<ButtonRelease-1>", lambda event: validate(event, "Paid"))
    typeFrame.grid(row=6, column=1, padx=5, pady=5)
    type_app.set("Free")
    
    priceEntry = tk.Entry(mainframe, width=20, textvariable=price)
    priceEntry.grid(row=7, column=1 ,padx=5, pady=5)
    price.set('0')
    priceEntry.bind("<Return>", lambda event: validate(event, "Price"))
    priceEntry.bind("<Tab>", lambda event: validate(event, "Price"))
    
    content_list=dfbb['Content Rating'].unique().tolist()
    droplist_content=tk.OptionMenu(mainframe,content_rating, *content_list)
    droplist_content.config(width=50)
    content_rating.set('----Select Content Rating----')
    droplist_content.grid(row=8,column=1,padx=5,pady=5)
    droplist_content.bind("<Return>", lambda event: validate(event, "Content Rating"))
    droplist_content.bind("<Tab>", lambda event: validate(event, "Content Rating"))

    
    genre_list=dfbb['Genres'].unique().tolist()
    droplist_genre=tk.OptionMenu(mainframe,genre, *genre_list)
    droplist_genre.config(width=50)
    genre.set('----Select Genre----')
    droplist_genre.grid(row=9,column=1,padx=5,pady=5)
    droplist_genre.bind("<Return>", lambda event: validate(event, "Genre"))
    droplist_genre.bind("<Tab>", lambda event: validate(event, "Genre"))

    
    c=DateEntry(mainframe , textvariable = last_update , date_pattern='dd/mm/YYYY')
    c.grid(row=10, column=1, padx=5, pady=5)
    c.bind("<Return>", lambda event: validate(event, "Genre"))
    last_update.set('01/01/2020')

    current_list=['Varies with device']
    currentVerEntry = ttk.Combobox(mainframe, width=20 ,values=current_list,textvariable=curr_ver)
    currentVerEntry.grid(row=11, column=1 ,padx=5, pady=5)
    currentVerEntry.bind("<Return>", lambda event: validate(event, "Current Ver"))
    currentVerEntry.bind("<Tab>", lambda event: validate(event, "Current Ver"))
    
    android_ver1=tk.StringVar(master=screen18)
    android_ver2=tk.StringVar(master=screen18)
    version1=['Varies with device','1.0','1.1','1.5','1.6','2.0','2.0.1','2.1','2.2','2.3','2.3.1','2.3.2','2.3.3','2.3.4','2.3.5','2.3.6','2.3.7','3.0','3.1','3.2','4.0.1','4.0.2','4.0.3','4.0.4','4.1','4.2','4.3','4.4','4.4.1','4.4.2','4.4.3','4.4.4','5.0','5.1','6.0','7.0','7.1','8.0.0','8.1.0','9','10']
    
    androidVerEntry1 =tk.OptionMenu(mainframe,android_ver1,*version1) 
    androidVerEntry1.config(width=20)
                
    androidVerEntry1.grid(row=12, column=1 ,padx=5, pady=5)
    androidVerEntry1.bind("<Return>", lambda event: validate(event, "Android Ver1"))
    androidVerEntry1.bind("<Tab>", lambda event: validate(event, "Android Ver1"))
    
    version2=['and up','1.0','1.1','1.5','1.6','2.0','2.0.1','2.1','2.2','2.3','2.3.1','2.3.2','2.3.3','2.3.4','2.3.5','2.3.6','2.3.7','3.0','3.1','3.2','4.0.1','4.0.2','4.0.3','4.0.4','4.1','4.2','4.3','4.4','4.4.1','4.4.2','4.4.3','4.4.4','5.0','5.1','6.0','7.0','7.1','8.0.0','8.1.0','9','10']
    androidVerEntry2 =OptionMenu(mainframe,android_ver2,*version2) 
    androidVerEntry2.config(width=20)
    
    androidVerEntry2.grid(row=12, column=2 ,padx=5, pady=5)
    android_ver2.set('and up')
    androidVerEntry2.bind("<Return>", lambda event: validate(event, "Android Ver2"))
    androidVerEntry2.bind("<Tab>", lambda event: validate(event, "Android Ver2"))
    
    btnFrame = tk.Frame(mainframe)
    b1=tk.Button(btnFrame, text="Submit" ,bg='#ff0000',fg='white',font=("Calibri", 15,'bold'),width='10',command=save_data1)
    b1.grid(row=0, column=1,padx=5, pady=5)  ##COMMAND
    b2=tk.Button(btnFrame, text="Cancel",bg='#ff0000',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen18.destroy)
    b2.grid(row=0, column=2, padx=5,pady=5)   ##COMMAND
    btnFrame.grid(row=13, column=1, padx=5, pady=5)
    b3=tk.Button(screen18,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen18.destroy)
    b3.place(x=0,y=0)
    
    l1=tk.Label(mainframe, text='App Name:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l1.grid(row=0, column=0,padx=5, pady=5, sticky="w")
    
    l2=tk.Label(mainframe, text='Category:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l2.grid(row=1, column=0,padx=5, pady=5, sticky="w")
    
    l3=tk.Label(mainframe, text='Rating:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l3.grid(row=2, column=0 ,padx=5,pady=5, sticky="w")
    
    l4=tk.Label(mainframe, text='Reviews:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l4.grid(row=3, column=0 ,padx=5, pady=5,sticky="w")
    l5=tk.Label(mainframe, text='App Size:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l5.grid(row=4, column=0 ,padx=5,pady=5, sticky="w")
    l6=tk.Label(mainframe, text='App Installs:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l6.grid(row=5, column=0,padx=5, pady=5, sticky="w")
    l7=tk.Label(mainframe, text='Type:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l7.grid(row=6, column=0 ,padx=5,pady=5, sticky="w")
    l8=tk.Label(mainframe, text='Price:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l8.grid(row=7, column=0 ,padx=5,pady=5, sticky="w")
    l9=tk.Label(mainframe, text='Content Rating:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l9.grid(row=8, column=0 ,padx=5,pady=5, sticky="w")
    l10=tk.Label(mainframe, text='Genres:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l10.grid(row=9, column=0 ,padx=5,pady=5, sticky="w")
    l11=tk.Label(mainframe, text='Last Updated:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l11.grid(row=10, column=0 ,padx=5,pady=5, sticky="w")
    l12=tk.Label(mainframe, text='Current Version:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l12.grid(row=11, column=0 ,padx=5,pady=5, sticky="w")
    l13=tk.Label(mainframe, text='Android Version:*', anchor='w',bg='#ffff00',font=("Calibri", 15,'bold'))
    l13.grid(row=12, column=0 ,padx=5,pady=5, sticky="w")
    
    
    reviewNoEntry.config(state='disabled')
    appSizeEntry.config(state='disabled')
    priceEntry.config(state='disabled')
    currentVerEntry.config(state='disabled')
    androidVerEntry1.config(state='disabled')
    androidVerEntry2.config(state='disabled') 
    droplist_cat.config(state='disabled')
    rate.config(state='disabled')
    droplist_inst.config(state='disabled')
    droplist_content.config(state='disabled')
    droplist_genre.config(state='disabled')
    
    screen18.mainloop()
    
def validate(event,input):
    if input=='App Name':
        if len(app_name.get())==0:
            messagebox.showerror("Enter App Name",parent=screen18)
        else:
            droplist_cat.focus_set()
            droplist_cat.config(state='normal')
    elif input=='App Category':
        if category.get()=='----Select App Category----':
            messagebox.showerror('Select App Category',parent=screen18)
        else:
            rate.focus_set()
            rate.config(state='normal')
            reviewNoEntry.focus_set()
            reviewNoEntry.config(state='normal')
            
    elif input=='Review NO':
        if (review_no.get().isdigit()):
            appSizeEntry.focus_set()
            appSizeEntry.config(state='normal')
        else:
            messagebox.showerror('Invalid Input! Integer Required',parent=screen18)
    elif input=='App Size':
        if (size_app.get().isdigit()):
            unit_option.config(state='normal')
            unit_option.focus_set()
#            droplist_inst.config(state='normal')
        else:
            messagebox.showerror('Enter Valid Size!',parent=screen18)
    elif input=='Size Unit':
        droplist_inst.focus_set()
        droplist_inst.config(state='normal')
        
    elif input=='App Installs':
        if install_no.get()=='----Select App Installs----':
            messagebox.showerror('Select App Installs',parent=screen18)
        else:
            droplist_content.focus_set()
            droplist_content.config(state='normal')
            
            
            
    elif input=='Paid':
        priceEntry.config(state='normal')
        priceEntry.focus_set()
        
        droplist_content.config(state='normal')
    elif input=='Free':
        priceEntry.config(state='disabled')
        droplist_content.focus_set()
        droplist_content.config(state='normal')
        price.set(0)
                
        
    elif input=='Price':
        if (price.get().isdigit()):
            droplist_content.focus_set()
            droplist_content.config(state='normal')
        else:
            messagebox.showerror('Enter valid Price!',parent=screen18)
    elif input=='Content Rating':
        if content_rating.get()=='----Select Content Rating----':
            messagebox.showerror('Give App Rating!',parent=screen18)
        else:
            droplist_genre.focus_set()
            droplist_genre.config(state='normal')
    elif input=='Genre':
        if genre.get()=='----Select Genre----':
            messagebox.showerror('Select Genre',parent=screen18)
        else:
            currentVerEntry.focus_set()
            currentVerEntry.config(state='normal')
    elif input=='Current Ver':
        if len(curr_ver.get())==0:
            messagebox.showerror('Enter Current Version',parent=screen18)
        else:
            androidVerEntry1.focus_set()
            androidVerEntry1.config(state='normal')
            androidVerEntry2.config(state='normal')
    elif input=='Android Version1':
        if android_ver1.get()=="":
            messagebox.showerror('Enter Android Version',parent=screen18)
        else:
            androidVerEntry2.focus_set()


####==================add data 2================
global df11
df11 = pd.read_excel('googleplaystore_user_reviews.xlsx')
df11=df11.dropna()
            
def get_len():
    global row,col
    wb=xlrd.open_workbook('googleplaystore_user_reviews.xlsx')

    w_sheet=wb.sheet_by_index(0)
    row=w_sheet.nrows
    col=w_sheet.ncols



def save_data2():
    if len(review_sent.get())==0:
        messagebox.showinfo("Save" , "Not Validated!",parent=screen18_1)
        return
    try:
        get_len()
        r=int(row+1)
        wb=openpyxl.load_workbook('googleplaystore_user_reviews.xlsx')

    
        w_sheet=wb['in']
    
        insert=(app_name_sent.get(),review_sent.get(),s2,p2,ss)

        w_sheet.append(insert)
        wb.save('googleplaystore_user_reviews.xlsx')
        
        messagebox.showinfo("Save" , "Success!",parent=screen18_1)
    except Exception as e:
     print(e)
     
     messagebox.showerror("Save" ,"Failed to save!",parent=screen18_1)
#  If error on saving , shows error message.
     
        

def calc(event):
    global s2,p2,ss
    if len(review_sent.get())==0:
        messagebox.showinfo("Save" , "Not Validated!",parent=screen18_1)
        return
    
    polaritys=tb(review_sent.get()).sentiment.polarity

    subjectivitys=tb(review_sent.get()).sentiment.subjectivity
    if polaritys>0:
        sentiment='Positive'
    if polaritys<0:
        sentiment='Negative'
    if polaritys==0:
        sentiment='Neutral '
    s2=str(sentiment)
    p2=float(str(polaritys))
    ss=float(str(subjectivitys))
    sentimentLabel=tk.Label(mainframe, text='%s'%sentiment, font=("Calibri", 15,'bold'),anchor='w')

    sentimentLabel.grid(row=2, column=1,padx=5, pady=5, sticky="w")
    polarityLabel=tk.Label(mainframe, text='%f'%polaritys,font=("Calibri", 15,'bold'), anchor='w')

    polarityLabel.grid(row=3, column=1,padx=5, pady=5, sticky="w")
    subjectivityLabel=tk.Label(mainframe, text='%f'%subjectivitys, font=("Calibri", 15,'bold'),anchor='w')

    subjectivityLabel.grid(row=4, column=1,padx=5, pady=5, sticky="w")
    b1submit.config(state='normal')


def validateS(event,input):
    if input=="App Name S":
        if len(app_name_sent.get())==0:
            messagebox.showerror("Enter App Name",parent=screen18_1)
        else:
            reviewSentEntry.focus_set()
            reviewSentEntry.config(state='normal')
    elif input=="ReviewS":
        if len(review_sent.get())==0:
            messagebox.showerror('Enter Review',parent=screen18_1)
        
    
    
def main18_sent():
    global screen18_1,app_name_sent,sentiment,polaritys,subjectivitys,review_sent,appNameSentEntry,reviewSentEntry,mainframe,b1submit
    screen18_1=tk.Toplevel(screena1)
    adjustWindow(screen18_1,screen18_1)
    l1=tk.Label(screen18_1,text='Add User Reviews Data',fg='black', bg='#66ff33', width='10',height='2',font=("Calibri", 15,'bold'))
    l1.pack(fill=X)

    mainframe=tk.Frame(screen18_1,bg='white')
    mainframe.pack(pady='15')
    
    app_name_sent=tk.StringVar(master=screen18_1)
    review_sent=tk.StringVar(master=screen18_1)
    sentiment=tk.StringVar(master=screen18_1)
    subjectivitys=tk.StringVar(master=screen18_1)
    polaritys=tk.StringVar(master=screen18_1)
    
    appNameSentEntry = tk.Entry(mainframe, width=30, textvariable=app_name_sent)             
        
    appNameSentEntry.grid(row=0, column=1 ,padx=5, pady=5)                                     
    appNameSentEntry.bind("<Return>", lambda event: validateS(event, "App Name S"))
    appNameSentEntry.bind("<Tab>", lambda event: validateS(event, "App Name S"))
    appNameSentEntry.focus_set()
    
    reviewSentEntry = tk.Entry(mainframe, width=30, textvariable=review_sent)    
                 
    reviewSentEntry.grid(row=1, column=1 ,padx=5, pady=5)                                     
    reviewSentEntry.bind("<Return>", lambda event: validateS(event, "ReviewS"))
    reviewSentEntry.bind("<Tab>", lambda event: validateS(event, "ReviewS"))
    reviewSentEntry.bind("<Return>",lambda event: calc(event))
    
    l2=tk.Label(mainframe, text='App Name:*',font=("Calibri", 15,'bold'), anchor='w',bg='#ffff00',width='20')

    l2.grid(row=0, column=0,padx=5, pady=5, sticky="w")
    l3=tk.Label(mainframe, text='Review:*',font=("Calibri", 15,'bold'), anchor='w',bg='#ffff00',width='20')

    l3.grid(row=1, column=0,padx=5, pady=5, sticky="w")
    l4=tk.Label(mainframe, text='Sentiment:',font=("Calibri", 15,'bold'), anchor='w',bg='#ffff00',width='20')

    l4.grid(row=2, column=0,padx=5, pady=5, sticky="w")
    l5=tk.Label(mainframe, text='Sentiment Polarity:',font=("Calibri", 15,'bold'), anchor='w',bg='#ffff00',width='20')

    l5.grid(row=3, column=0,padx=5, pady=5, sticky="w")
    l6=tk.Label(mainframe, text='Sentiment Subjectivity:',font=("Calibri", 15,'bold'), anchor='w',bg='#ffff00',width='20')

    l6.grid(row=4, column=0,padx=5, pady=5, sticky="w")
    reviewSentEntry.config(state='disable')
    
    btnFrame = tk.Frame(mainframe)
    b1submit=tk.Button(btnFrame, text="Submit",bg='#ff0000',fg='white',font=("Calibri", 15,'bold'),width='10',command=save_data2)  

    
    b1submit.grid(row=0, column=1,padx=5, pady=5)
    b1submit.config(state='disabled')
    b2=tk.Button(btnFrame, text="Cancel",bg='#ff0000',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen18_1.destroy)

    b2.grid(row=0, column=2, padx=5,pady=5)   
    btnFrame.grid(row=5, column=1, padx=10, pady=10)
    b3=tk.Button(screen18_1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screen18_1.destroy)
    b3.place(x=0,y=0)

    
    
    
    screen18_1.mainloop()


            
###========================menus===================
def download_menu():
     global screend1
     screend1=tk.Toplevel(screenw)
     adjustWindow(screend1,screend1)
     screend1.config(background='#174873')
     screend1.title('Download ')
     a1=tk.Label(screend1,text='Download Section', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33').pack(fill=X)

     b1=tk.Button(screend1, text='Number of Downloads ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main2 )
     b1.pack(pady=20)#2
     b2=tk.Button(screend1, text='Number of Downloads for App Sizes', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main5)
     b2.pack(pady=20)#5
     b3=tk.Button(screend1, text=' Number of Install for Quarter', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main11)
     b3.pack(pady=20)#11
     b4=tk.Button(screend1, text='Month And Download ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main16)
     b4.pack(pady=20)#16
     b5=tk.Button(screend1, text='Number of Downloads and App Sizes', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main17)
     b5.pack(pady=20)#17

     b6=tk.Button(screend1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screend1.destroy)
     b6.place(x=0,y=0)
     screend1.mainloop()
def type_menu():
     global screent1
     screent1=tk.Toplevel(screenc1)
     adjustWindow(screent1,screent1)
     screent1.config(background='#174873')
     screent1.title('Type')
     a1=tk.Label(screent1,text='App Type', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)
     
     b1=tk.Button(screent1, text='Free-Paid', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main20)
     b1.pack(pady=20)#20
     b2=tk.Button(screent1, text='Android Version Type', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main7)
     b2.pack(pady=20)#7
     b3=tk.Button(screent1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screent1.destroy)
     b3.place(x=0,y=0)
     screent1.mainloop()
def cat_menu():
     global screenc1
     screenc1=tk.Toplevel(screenw)
     adjustWindow(screenc1,screenc1)
     screenc1.config(background='#174873')
     screenc1.title('Category')
     a1=tk.Label(screenc1,text='Category Section', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)
     
     b1=tk.Button(screenc1, text='Percentage download in each Category ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main1)
     b1.pack(pady=20)#1

     b2=tk.Button(screenc1, text='Category with Most,Least and Average Downloads', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main3)
     b2.pack(pady=20)#3
     b3=tk.Button(screenc1, text='Category with Most And Least Downloads yearly', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main6)
     b3.pack(pady=20)#6
     b4=tk.Button(screenc1, text='Category downloaded in coming Years', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main8)
     b4.pack(pady=20)#8
     b5=tk.Button(screenc1, text='Category and Month', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main10)
     b5.pack(pady=20)#10
     b6=tk.Button(screenc1, text='App Type ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=type_menu)
     b6.pack(pady=20)
     b7=tk.Button(screenc1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenc1.destroy)
     b7.place(x=0,y=0)
     screenc1.mainloop()
  

def rating_menu():
     global screenr1
     screenr1=tk.Toplevel(screenw)
     adjustWindow(screenr1,screenr1)
     screenr1.config(background='#174873')
     screenr1.title('Rating')
     a1=tk.Label(screenr1,text='Rating Section', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)


     b1=tk.Button(screenr1, text='Rating Above 4.1', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main9)
     b1.pack(pady=20)#9
     b2=tk.Button(screenr1, text='Rating and Category ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main4)
     b2.pack(pady=20)#4
     b3=tk.Button(screenr1, text='Content Rating', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main19)
     b3.pack(pady=20)#19

     b4=tk.Button(screenr1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr1.destroy)
     b4.place(x=0,y=0)
     screenr1.mainloop()

  
def sent_menu():
     global screens1
     screens1=tk.Toplevel(screenw)
     adjustWindow(screens1,screens1)
     screens1.config(background='#174873')
     screens1.title('Sentiment ')
     a1=tk.Label(screens1,text='Sentiment Section', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)

     b1=tk.Button(screens1, text='Sentiments', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main12)
     b1.pack(pady=20)#12
     b2=tk.Button(screens1, text='Polarity and Subjectivity', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main13)
     b2.pack(pady=20)#13
     b3=tk.Button(screens1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screens1.destroy)
     b3.place(x=0,y=0)
     screens1.mainloop()

def review_menu(): 
     global screenr2
     screenr2=tk.Toplevel(screenw)
     adjustWindow(screenr2,screenr2)
     screenr2.config(background='#174873')
     screenr2.title('Review ')
     a1=tk.Label(screenr2,text='Review Section', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)    
     b1=tk.Button(screenr2, text='Reviews', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main14)
     b1.pack(pady=50)#14
     b2=tk.Button(screenr2, text=' 10 Best Foods for You ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main15)
     b2.pack(pady=20)#15
#     Button(screens1, text='Month And Download ', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2).pack(pady=20)
     b3=tk.Button(screenr2,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screenr2.destroy)
     b3.place(x=0,y=0)
     screenr2.mainloop()

     
def add_data_menu():
     global screena1
     screena1=tk.Toplevel(screenw)
     adjustWindow(screena1,screena1)
     screena1.config(background='#174873')
     screena1.title('Add Data ')
     a1=tk.Label(screena1,text='Add Data', width='10', height="3", font=("Calibri", 15,'bold'), fg='black', bg='#66ff33')
     a1.pack(fill=X)

     b1=tk.Button(screena1, text='ADD APP DATA', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main18_app)
     b1.pack(pady=20)
     b2=tk.Button(screena1, text='ADD USER REVIEWS DATA', width=50, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=main18_sent)
     b2.pack(pady=20)
     b3=tk.Button(screena1,text='<<<BACK',bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=screena1.destroy)
     b3.place(x=0,y=0)
     screena1.mainloop()

###===================login========================
def repeat():
    answer=messagebox.askyesno("THANK YOU","EXIT APPLICATION?")
    if answer == True:
        screenw.destroy()
        screenw.quit()
    
def adjustWindow1(window):
 w = screenw.winfo_screenwidth() # width of the screen
 h = screenw.winfo_screenheight() # height of the screen
 window.geometry('%dx%d' % (w, h)) # set the dimensions of the screen and where it is placed
 window.resizable(False, False) # disabling the resize option for the window
 window.configure(background='white') # making the background white of the window

def welcome_page():
 global screenw
 screenw =tk.Tk()
 screenw.title("Welcome")
 adjustWindow(screenw,screenw) 
 
 a1=tk.Label(screenw, text="Welcome " , width='32', height="2",font=("Calibri", 22, 'bold'), fg='white', bg='#66ff33')
 a1.pack(fill=X)
 a2=tk.Label(screenw, text="", bg='#174873', width='568', height='488')
 a2.place(x=0, y=96)
 m1=tk.Message(screenw, text='" GOOGLE PLAYSTORE DATA ANALYSIS "', width='180', font=("Helvetica",10, 'bold', 'italic'), fg='black', bg='#ffff00', anchor = CENTER)
 m1.place(x=10, y=100)

 path = "play_image.png"
 img=Image.open(path)
 img=img.resize((468,388),Image.ANTIALIAS)
 img = ImageTk.PhotoImage(img, master=screenw)
    
 panel = tk.Label(screenw, image = img)
 panel.place(x=20,y=170)
                                                      

 b1=tk.Button(screenw, text='DOWNLOADS', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=download_menu)
 b1.place(x=670, y=150)
 b2=tk.Button(screenw, text='CATEGORY', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=cat_menu)
 b2.place(x=670, y=250)
 b3=tk.Button(screenw, text='RATING', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=rating_menu)
 b3.place(x=670, y=350)
 b4=tk.Button(screenw, text='SENTIMENT', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=sent_menu)
 b4.place(x=670, y=450)
 b5=tk.Button(screenw, text='REVIEWS', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=review_menu)
 b5.place(x=670, y=550)
 b6=tk.Button(screenw, text='ADD DATA', width=40, font=("Open Sans", 13, 'bold'),bg='#ff0000', fg='black',height=2,command=add_data_menu)
 b6.place(x=670, y=650)
 b7=tk.Button(screenw, text="CLOSE",bg='#0066ff',fg='white',font=("Calibri", 15,'bold'),width='10',command=repeat)
 b7.place(x=0,y=0)

 screenw.mainloop()

    
welcome_page()
    

 
 
