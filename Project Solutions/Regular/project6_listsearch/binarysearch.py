#Type pip3 install names to install names
import random

total=1000
loc=total//2
minval=0
maxval=10000

numbers=[]
for _ in range(total):
    nextval=random.randint(minval,maxval)
    numbers.append(nextval)
numbers.sort()

secretnumber=numbers[random.randint(0,total-1)]

totalsearches=0
while(2**totalsearches<total):
    totalsearches+=1

minindex=0
maxindex=total-1
curindex=(minindex+maxindex)//2
for i in range(totalsearches):
    print(minindex,curindex,maxindex)
    if(numbers[curindex]==secretnumber):
        print(secretnumber,"is at",curindex)
        print("This took",totalsearches,"searches")
        break
    elif(numbers[curindex]>secretnumber):
        print(numbers[curindex],"is greater than",secretnumber)
        maxindex=curindex
        curindex=(maxindex+minindex)//2
    elif(numbers[curindex]<secretnumber):
        print(numbers[curindex],"is less than",secretnumber)
        minindex=curindex
        curindex=(maxindex+minindex)//2
    