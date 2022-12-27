import random

print("Rock Paper Scissors")
print("Enter your choice (0: Rock, 1: Paper, 2:Scissors)")
choice=int(input())
roll=random.randint(0,2)
if(choice==0):
    if(roll==0):
        print("Player and Computer both chose rock. Tie.")
    elif(roll==1):
        print("Player chose rock and Computer chose paper. Computer wins.")
    else:
        print("Player chose rock and computer chose scissors. Player wins.")
elif(choice==1):
    if(roll==0):
        print("Player chose paper and computer chose rock. Player wins.")
    elif(roll==1):
        print("Player and Computer both chose paper. Tie.")
    else:
        print("Player chose paper and computer chose scissors. Computer wins.")
else:
    if(roll==0):
        print("Player chose scissors and Computer chose rock. Computer wins.")
    elif(roll==1):
        print("Player chose scissors and computer chose paper. Player wins.")
    else:
        print("Player and Computer both chose scissors. Tie.")
