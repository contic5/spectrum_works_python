import random

rollcounts=[]
percents=[]
totalrolls=-1


def rolldice(totalrolls=1,minval=1,maxval=6):
    rollcounts=[0]*(maxval-minval+1)
    for i in range(totalrolls):
        roll=random.randint(minval,maxval)
        rollindex=roll-minval
        rollcounts[rollindex]+=1
    return rollcounts

def calculatepercents(rollcounts,totalrolls):
    percents=[]
    for i in range(len(rollcounts)):
        percent=round(100*rollcounts[i]/totalrolls,3)
        percents.append(percent)
    return percents

def displayresults(rollcounts,percents,totalrolls,minval,maxval):
    if(totalrolls>1):
        print("Results from rolling a dice with sides from",minval,"to",maxval,"a total of",totalrolls,"times")
    else:
        print("Results from rolling a dice with sides from",minval,"to",maxval,"a total of",totalrolls,"time")

    for i in range(len(percents)):
        val=i+minval
        print(val," ",rollcounts[i]," ",percents[i],"%",sep="")

def handle_int_input(message,defaultvalue):
    val=input(message)
    if(val!="" and val.isdigit):
        val=int(val)
    else:
        val=defaultvalue
    return val

done=False
while (not done):
    totalrolls=handle_int_input("Enter the total number of rolls (default is 1): ",1)
    minval=handle_int_input("Enter the minimum value (default is 1): ",1)
    maxval=handle_int_input("Enter the maximum value (default is 6): ",6)
    
    rollcounts=rolldice(totalrolls,minval,maxval)
    percents=calculatepercents(rollcounts,totalrolls)
    displayresults(rollcounts,percents,totalrolls,minval,maxval)
    