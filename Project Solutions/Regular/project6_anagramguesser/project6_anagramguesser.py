import random
import copy

print("Anagram Guesser")

orig=input("Setter, enter a word: ")
for i in range(20):
    print()
shuffledword=copy.deepcopy(orig)
letters=list(shuffledword)

random.shuffle(letters)
shuffledword="".join(letters)
print(shuffledword)

guessesmade=0
maxguesses=5
guess=""

while(guessesmade<maxguesses):
    guess=input("Enter your guess: ")
    if(guess==orig):
        break
    for i in range(len(orig)):
        if(i<len(guess)):
            if(guess[i]==orig[i]):
                print(orig[i],end=" ")
            else:
                print("-",end=" ")
        else:
            print("-",end=" ")
    print()
    guessesmade+=1

print("The word is",orig)
if(guessesmade<maxguesses):
    print("The guesser wins")
else:
    print("The setter wins")
