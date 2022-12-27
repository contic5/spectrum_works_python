import random
minval=1
maxval=100
number=random.randint(minval,maxval)
totalguesses=8

print("Guessing Game")
print("I generated a random number between",minval,"and",maxval)
print("Try to guess it in",totalguesses,"guesses")
while(totalguesses>0):
    print("You have ",totalguesses,"guesses left.")
    guess=int(input("Guess a number between "+str(minval)+" and "+str(maxval)+": "))
    if(guess==number):
        print("Correct",end="\n\n")
        break
    elif(guess<number):
        print("Incorrect. Guess is less than the number.",end="\n\n")
    else:
        print("Incorrect. Guess is greater than the number.",end="\n\n")
    totalguesses-=1

print("The number is ",number)
if(totalguesses>0):
    print("You win")
else:
    print("You lose")