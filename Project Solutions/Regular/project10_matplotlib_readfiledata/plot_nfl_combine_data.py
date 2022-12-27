import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt

class Threshold:
    def __init__(self,keyname,value,abovethreshhold) -> None:
        self.keyname=keyname
        self.value=value
        self.abovethreshhold=abovethreshhold

class Filter:
    def __init__(self,keyname,value,equalto):
        self.keyname=keyname
        self.value=value
        self.equalto=equalto

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def get_attendance(game):
    if(game["Attendance"]==""):
        return -1
    if(not is_float(game["Attendance"])):
        return -1
    return game["Attendance"]

def filterdata(players):
    filters=[]

    #filters.append(Filter("SEGMENT","Casual Dining",True))

    #filters.append(Filter("MENU CATEGORY","Italian/Pizza",True))

    for filter in filters:
        playerscopy=[]
        for player in players:
            if(filter.equalto==True and player[filter.keyname]==filter.value):
                playerscopy.append(player)
            if(filter.equalto==False and player[filter.keyname]!=filter.value):
                playerscopy.append(player)
        players=playerscopy
    return players

def sortplayers(players,category,is_reverse):
    curplayers=[]
    for i in range(len(players)):
        if(is_float(players[i][category])):
            curplayers.append(players[i])

    if(not is_reverse):
        for i in range(len(curplayers)):
            minval=1000000000
            minindex=i
            for j in range(i+1,len(curplayers)):
                curval=float(curplayers[j][category])
                if(curval<minval):
                    minval=curval
                    minindex=j
            curplayers[i],curplayers[minindex]=curplayers[minindex],curplayers[i]
    else:
        for i in range(len(curplayers)):
            maxval=-1000000000
            maxindex=i
            for j in range(i+1,len(curplayers)):
                curval=float(curplayers[j][category])
                if(curval>maxval):
                    maxval=curval
                    maxindex=j
            curplayers[i],curplayers[maxindex]=curplayers[maxindex],curplayers[i]
    return curplayers

def writetofile(filename,curplayers,categories):
    results=""
    for i in range(len(categories)):
        results+=categories[i]
        if(i<len(categories)-1):
            results+=","

    results+="\n"
    for i in range(len(curplayers)):
        curplayer=curplayers[i]
        keyon=0
        for key, value in curplayer.items():
            results+=str(value)
            if(keyon<len(categories)-1):
                results+=","
            keyon+=1
        results+="\n"
    
    myfile=open(filename+".csv","w")
    myfile.write(results)
    myfile.close()

def main():
    players=[]
    playerfile=open("NFL_2020_Combine.csv","r")
    lines=playerfile.readlines()
    lineon=0
    for line in lines:
        line = line. rstrip('\n') 
        line = line. strip('\ufeff')
        if(lineon==0):
            categories=line.split(",")
        else:
            parts=line.split(",")
            player={}
            for category,part in zip(categories,parts):
                if(part.isdigit()):
                    player[category]=int(part)
                if(part.isdecimal()):
                    player[category]=float(part)
                else:
                    player[category]=part
            players.append(player)
        lineon+=1
    
    players=filterdata(players)
    
    for category in categories:
        print(category,end=" ")
    print(end="\n\n")

    #plt.style.use('_mpl-gallery')

    sortcategories=["40yd","Vertical","Bench","Broad Jump","Shuttle","3Cone"]
    labelnames=["Time","Inches","Reps","Inches","Time","Time"]
    is_reverse=[False,True,True,True,False,False]
    for x in range(len(sortcategories)):
        print(category)
        vals=[]
        #sort players
        category=sortcategories[x]
        curplayers=sortplayers(players,category,is_reverse[x])

        for i in range(len(curplayers)):
            if(is_float(curplayers[i][category])):
                vals.append(float(curplayers[i][category]))

        # plot:
        fig, ax = plt.subplots()
        

        ax.hist(vals, bins=8, linewidth=0.5, edgecolor="blue")
        
        maxval=max(vals)
        minval=min(vals)
        stepval=(maxval-minval)/8
        print(maxval,minval,stepval)
        plt.title("NFL Combine: "+category)
        ax.set(xlabel=labelnames[x])
        #ax.set(xlim=(minval, maxval), xticks=np.arange(maxval, minval,stepval))

        '''
        ax.set(xlim=(minval, maxval), xticks=np.arange(maxval, minval,stepval),
            ylim=(0, 56), yticks=np.linspace(0, 56, 9))
        '''

        '''
        plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
        '''

        plt.show()
        
main()