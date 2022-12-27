import random

singleplayer=True
print("Mastermind")
code=0
if(singleplayer):
    code=str(random.randint(0,99999))
    while(len(code)<5):
        code="0"+code
else:
    code=(input("Setter, enter a 5 digit code:"))

remaningguesses=10
winner=False

matches=""
while(remaningguesses>0 and not winner):
    matches=""
    
    print("Guesser, you have ",remaningguesses,"guess remaining.")
    guess=(input("Guesser, guess a 5 digit code:",))
    for i in range(len(guess)):
        subguess=guess[0:i+1]
        if(guess[i]==code[i]):
            matches+="C\t"
        elif(subguess.count(guess[i])<=code.count(guess[i])):
            matches+="M\t"
        else:
            matches+="X\t"
    
    for i in range(len(guess)):
        print(guess[i],end="\t")
    print()
    print(matches,end="\n\n")

    if(guess==code):
        break
    remaningguesses-=1

print("The code is",code)
if(remaningguesses>0):
    print("Guesser wins")
else:
    print("Setter wins")