import random
import time
from threading import Timer
import pandas as pd
import stdiomask
import csv
corr=[]
incorr=[]
qname=["Music.csv","Sports.csv","Hindi.csv","English.csv","Food.csv","Travel.csv","Politics.csv","GK.csv","MA.csv","Edu.csv"]
qnam=["Music","Sports","Hindi","English","Food","Travel","Politics","GK","MA","Edu"]
qn="__________________________Quiz!___________________________\n1.  Music\n2.  Sports\n3.  Hindi_Movies_and_Webseries\n4.  English_Movies_and_Webseries\n5.  Food\n6.  Travel\n7.  Politics\n8.  General Knowledge\n9.  Mental Ability\n10. Education\n"
timeout=30
poin=300 
def playername():
    print("-------------------------------------------------------------------\n")
    name = input("Enter Your User Id: ")
    passw = stdiomask.getpass("Enter your Password: ")
    print("-------------------------------------------------------------------\n")
    f=pd.read_csv("playerid.csv")
    if name in open('playerid.csv').read() and passw in open('playerid.csv').read():
        print(play(name))
    else:
        print("You Entered Wrong User id or Password! [Note: if you haven't signup please signup first]")
        print(playin())

def leaderboard(k):
    d=pd.read_csv("playerid.csv")
    f=open("playerid.csv")
    x=csv.reader(f)
    z=len(list(x))
    a=z-1
    l=[]
    for i in range(a):
        c=f"{d.iloc[i,0]}sco.csv"
        b=pd.read_csv(c)
        e=b['Total Points'].sum()
        g=round(e,2)
        h=f"{g}       {d.iloc[i,0]}"
        l.append(h)
    l.sort(reverse=True)
    print("Scores       User Id \n")
    for j in range (len(l)):
        print(l[j])
    print("-------------------------------------------------------------------\n")
    if k==1:
        return index()
    elif k==2:
        return playin()

def playerscore(a):
    if a==2:
        print("-------------------------------------------------------------------\n")
        name = input("Enter Your User Id: ")
        passw = stdiomask.getpass("Enter your Password: ")
        print("-------------------------------------------------------------------\n")
        f=pd.read_csv("playerid.csv")
        if name in open('playerid.csv').read() and passw in open('playerid.csv').read():
            z=f"{name}sco.csv"
            df=pd.read_csv(z)
            a=df['Total Points'].sum()
            b=df['Total Points'].max()
            freq=df['Topic'].mode()
            fr=freq[0]
            print(df)
            print(f"Total Score: {a}\n Maximum Score: {b}\n Most Takken Topic: {fr}\n")
            print("-------------------------------------------------------------------\n")
            print(playin())
        else:
            print("You Entered Wrong User id or Password!")
            print(playerscore())
    elif a==1:    
        d=pd.read_csv("playerid.csv")
        f=open("playerid.csv")
        x=csv.reader(f)
        z=len(list(x))
        a=z-1
        for i in range(a):
            print(f"{i+1}.   {d.iloc[i,0]}")
        j=int(input("Enter Your Choice: "))
        print("-------------------------------------------------------------------\n")
        k=j-1
        c=f"{d.iloc[k,0]}sco.csv"
        df=pd.read_csv(c)
        a=df['Total Points'].sum()
        b=df['Total Points'].max()
        freq=df['Topic'].mode()
        fr=freq[0]
        print(df)
        print(f"Total Score: {a}\nYour Maximum Score: {b}\nYour Most Takken Topic: {fr}\n")
        print("-------------------------------------------------------------------\n")
        print(index())

def que(num,ab):
    df = pd.read_csv(ab)
    print(df['Question'][num])
    print("1.",df['A'][num])
    print("2.",df['B'][num])
    print("3.",df['C'][num])
    print("4.",df['D'][num])
    print("5 Skip Question")
    print("-------------------------------------------------------------------\n")
    t=Timer(timeout,print,["\nSorry, time's up! \n Enter 0 for next Quetion"])
    t.start()
    x=int(input("Enter your answer: "))
    if x==df['answer'][num]:
        print("Correct\n")
        corr.append(1)
        y=int(input("Enter 0 for next Question: "))
        print("-------------------------------------------------------------------\n")
    elif x==5:
        print("You Skipped this Quetion\n")
        y=int(input("Enter 0 for next Question: "))
        print("-------------------------------------------------------------------\n")
    elif x==1 or x==2 or x==4 or x==3 and x!=df['answer'][num]:
        print("Incorrect\n")
        incorr.append(1)
        y=int(input("Enter 0 for next Question: "))
        print("-------------------------------------------------------------------\n")
    else:
        print("")
        print("-------------------------------------------------------------------\n")
    t.cancel()

def adduser():
    print("-------------------------------------------------------------------\n")
    na=input("Set Your User name: ")
    pa=input("Set your Password: ")
    print("-------------------------------------------------------------------\n")
    with open("playerid.csv","a",newline="") as File:
        Writer=csv.writer(File)
        Writer.writerow([na,pa])
    File.close()
    x=f"{na}sco.csv"
    with open(x,"a",newline="") as Fil:
        Writer=csv.writer(Fil)
        Writer.writerow(["Question Points","Total Points","Time","Topic"])
    Fil.close()
    return playin()

def playin():
    print("-------------------------------------------------------------------\n")
    print("1. login to play\n2. Sign in for new user\n3. leader board\n4. check your own Scores\n5. Scoreboard\n6. Exit")
    print("-------------------------------------------------------------------\n")
    x=int(input("Enter your choice: "))
    if x==1:
        print(playername())
    elif x==2:
        print(adduser())
    elif x==3:
        print(leaderboard(2))
    elif x==4:
        print(playerscore(2))
    elif x==5:
        print(scoca(2))
    elif x==6:
        print(exit())

def scoca(a):
    print("____________________________________________________________________________\n")
    f=pd.read_csv("Scoreboard.csv")
    x=f.sort_values(by='Total Points', ascending=False)
    print(x)
    print("____________________________________________________________________________\n")
    if a==1:
        return index()
    elif a==2:
        return playin()

def checkque():
    print(qn)
    print("-------------------------------------------------------------------\n")
    ac=int(input("Enter your choice: "))
    print("-------------------------------------------------------------------\n")
    x=ac-1
    df=pd.read_csv(qname[x])
    dp=df.set_index('Index')
    dp1=dp.iloc[0:10]
    dp2=dp.iloc[10:20]
    dp3=dp.iloc[20:30]
    dp4=dp.iloc[30:40]
    dp5=dp.iloc[40:50]
    dp6=dp.iloc[50:60]
    dp7=dp.iloc[60:70]
    dp8=dp.iloc[70:80]
    dp9=dp.iloc[80:90]
    dp10=dp.iloc[90:]
    print(dp1,"\n",dp2,"\n",dp3,"\n",dp4,"\n",dp5,"\n",dp6,"\n",dp7,"\n",dp8,"\n",dp9,"\n",dp10,"\n")
    return index()

def changque():
    print(qn)
    print("-------------------------------------------------------------------\n")
    ac=int(input("Enter your choice: "))
    print("-------------------------------------------------------------------\n")
    x=ac-1
    quet(qname[x])

def quea(i):
    print("-------------------------------------------------------------------\n")
    a=input("Enter new Question: ")
    b=input("Enter option 1: ")
    c=input("Enter option 2: ")
    d=input("Enter option 3: ")
    e=input("Enter option 4: ")
    g=int(input("Enter correct option: "))
    print("-------------------------------------------------------------------\n")
    f=open(i)
    x=csv.reader(f)
    z=len(list(x))
    f.close()
    with open(i,"a",newline="") as File:
        Writer=csv.writer(File)
        Writer.writerow([z,a,b,c,d,e,g])
    File.close()
    return index()

def addque():
    print(qn)
    print("-------------------------------------------------------------------\n")
    ac=int(input("Enter your choice: "))
    print("-------------------------------------------------------------------\n")
    ca=ac-1
    quea(qname[ca])

def quet(i):
    df=pd.read_csv(i)
    dp=df.set_index('Index')
    dp1=dp.iloc[0:10]
    dp2=dp.iloc[10:20]
    dp3=dp.iloc[20:30]
    dp4=dp.iloc[30:40]
    dp5=dp.iloc[40:50]
    dp6=dp.iloc[50:60]
    dp7=dp.iloc[60:70]
    dp8=dp.iloc[70:80]
    dp9=dp.iloc[80:90]
    dp10=dp.iloc[90:]
    print(dp1,"\n",dp2,"\n",dp3,"\n",dp4,"\n",dp5,"\n",dp6,"\n",dp7,"\n",dp8,"\n",dp9,"\n",dp10,"\n")
    print("-------------------------------------------------------------------\n")
    a=int(input("Enter Number of Question you want to change: "))
    dp.loc[a, 'Question']=input("Enter new Question: ")
    dp.loc[a, 'A']=input("Enter Option 1: ")
    dp.loc[a, 'B']=input("Enter Option 2: ")
    dp.loc[a, 'C']=input("Enter Option 3: ")
    dp.loc[a, 'D']=input("Enter Option 4: ")
    dp.loc[a, 'answer']=input("Enter no. of correct option: ")
    print("-------------------------------------------------------------------\n")
    dp.to_csv(i)

def index():
    print("                           Welcome Sir!")
    print("____________________________________________________________________________\n")
    print("1. Check Score Card\n2. Change Questions\n3. Check Questions\n4. Add Question\n5. Leaderboard\n6. Check Indiviual Player Score\n7. Exit")
    print("____________________________________________________________________________\n")
    a=int(input("Please select one option: "))
    print("____________________________________________________________________________\n")
    if a==1:
        y=scoca(1)
    elif a==2:
        y=changque()
    elif a==3:
        checkque()
    elif a==4:
        addque()
    elif a==5:
        leaderboard(1)
    elif a==6:
        playerscore(1)
    elif a==7:
        exit()
    else:
        print("Incorret Input")
        print("____________________________________________________________________________\n")
    return index()

def owner():
    password=stdiomask.getpass("Enter your Password: ")
    print("---------------------------------------------------------------------------\n")
    if password=="12345678":
        x=index()
    else:
        print("Wrong Password! Please Try again.")
        print("____________________________________________________________________________\n")
        x=owner()
    return x

def play(nam):
    print(qn)
    print("-------------------------------------------------------------------\n")
    abc=int(input("Enter your choice: "))
    print("-------------------------------------------------------------------\n")
    cba=abc-1
    f=open(qname[cba])
    x=csv.reader(f)
    z=len(list(x))
    xyz=z-2
    initial=time.time()
    for i in range(1,11):
        y=random.randint(0,xyz)
        que(y,qname[cba])     
    a=time.time()-initial
    b=round(a,2)
    sumc=0
    sumic=0
    for i in range(len(corr)):
        sumc=sumc+corr[i]
    for j in range(len(incorr)):
        sumic=sumic+incorr[j]
    c=poin-b
    poi=(sumc*100)-(sumic*25)
    point=poi+c

    x=f"{nam}sco.csv"
    with open(x,"a",newline="") as Fil:
        Writer=csv.writer(Fil)
        Writer.writerow([poi,point,b,qnam[cba]])
    Fil.close()
    with open("Scoreboard.csv","a",newline="") as Fil:
        Writer=csv.writer(Fil)
        Writer.writerow([nam,poi,point,b,qnam[cba]])
    Fil.close()

    print(f"You Completed Quiz in {b} secs\nYou Got {c} points Extra\nCorrect: {sumc}\nIncorrect: {sumic}\nQuetion Points: {poi}\nTotal Points: {point}")
    print("-------------------------------------------------------------------\n")
    return exit()

def pmain():
    print("_________________________Welcome To Quiz!__________________________\n")
    print("1. Play Quiz\n2. Owner\n3. Exit")
    print("-------------------------------------------------------------------\n")
    ty=int(input("Select One: "))
    if ty==1:
        print(playin())
    elif ty==2:
        print(owner())
    elif ty==3:
        exit()


print(pmain())
