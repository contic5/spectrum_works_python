alphabetletters="abcdefghijklmnopqrstuvwxyz"
alphabetletters=list(alphabetletters)
print("Hangman")

word=input("Enter a word (Make sure it isn't more than 10 characters): ")
hint=input("Optionally, enter a hint, leave blank for no hint.): ")
guessesleft=6

shownletters=["-" for col in range(len(word))]
usedletters=[]

for i in range(len(shownletters)):
    if(not word[i] in alphabetletters):
        shownletters[i]=word[i]

solved=False
while(guessesleft>0 and not solved):
    print("Used letters:",usedletters)
    for i in range(len(shownletters)):
        print(shownletters[i],end=" ")
        if(shownletters[i]==" "):
            print()
    print()
    print("You have",guessesleft,"guesses remaining")
    if(hint!=""):
        print("Hint:",hint)
    letter=input("Enter a letter: ")
    alreadyguessed=False
    if(not letter in usedletters):
        usedletters.append(letter)
    else:
        alreadyguessed=True
    found=False

    if(not alreadyguessed):
        for i in range(len(word)):
            if(word[i]==letter):
                shownletters[i]=word[i]
                found=True
    
    if(not found or alreadyguessed):
        guessesleft-=1
    
    if(found):
        print(letter,"is in the word")
    elif(alreadyguessed):
        print(letter,"has already been guessed")
    else:
        print(letter,"is not in the word")
    print()
    
    allfilled=True
    for i in range(len(shownletters)):
        if(shownletters[i]=="-"):
            allfilled=False
    
    if(allfilled):
        solved=True

if(solved):
    print("You win. The word is",word)
else:
    print("You lose. The word is",word)
