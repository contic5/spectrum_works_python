#Type pip3 install names to install names
import random

total=1000
minval=0
maxval=10000

numbers=[]
for _ in range(total):
    nextval=random.randint(minval,maxval)
    numbers.append(nextval)
numbers.sort()

secretnumber=numbers[random.randint(0,total-1)]

totalsearches=1

for i in range(total):
    if(numbers[i]==secretnumber):
        print(secretnumber,"is at",i)
        break
    totalsearches+=1
print("This took",totalsearches,"searches")
