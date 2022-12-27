import random
minval=1
maxval=100
number=random.randint(minval,maxval)

print("Guessing Game")
number=int(input("Enter a number between "+str(minval)+" and "+str(maxval)+": "))
totalguesses=1
val=1
while(val<number):
    val*=2
    totalguesses+=1

minpossible=minval
maxpossible=maxval

while(totalguesses>0):
    print("You have ",totalguesses,"guesses left.")
    print("Number can be between",minval,"and",maxval)
    guess=(minval+maxval)//2
    print(guess)

    if(guess==number):
        print("Correct",end="\n\n")
        break
    elif(guess<number):
        minval=guess+1
        print("Incorrect. Guess is less than the number.",end="\n\n")
    else:
        maxval=guess-1
        print("Incorrect. Guess is greater than the number.",end="\n\n")
    totalguesses-=1

print("The number is ",number)
if(totalguesses>0):
    print("You win")
else:
    print("You lose")