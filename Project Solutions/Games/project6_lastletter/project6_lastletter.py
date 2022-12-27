turn=0
tutorial=False
gameover=False
words=["works"]
print("Last letter")

if(tutorial):
    print("Rules")
    print("Each player must name a word. Each player has to use the last letter of the last word as the first letter of their word")
    print("If someone repeats a word, they lose")
    print("Enter any nonletter character to give up",end="\n\n")

    print("Example")
    print("Player 1: Ace")
    print("Player 2: Excel")
    print("Player 1: Lightning")
    print("Player 2: Gaming")
    print("Player 1: Going")
    print("Player 2: Golden")
    print("Player 1: Negate")
    print("Player 2: Elevate")
    print("Player 1: Excel")
    print("Player 1 repeated a word. Player 2 wins!")

print("Use work appropriate words")
print("Words must be at least 3 letters")
print("Do not use words with x at the end (That's overpowered)")
print("Enter () to give up")

word="works"
while not gameover:
    nextword=input("Player "+str(turn+1)+" enter a word that starts with "+word[-1]+": ")
    if(nextword=="()"):
        print("Player",(turn+1),"yields!")
    elif(not word.isalpha):
        print("Invalid characters!")
        break
    elif(nextword[0]!=word[-1]):
        print("Current word does not start with last word's first letter")
        break
    elif(len(nextword)<3):
        print("Current word is less than 3 characters.")
        break
    elif(nextword not in words):
        word=nextword
        print(word)
        words.append(word)
        turn=(turn+1)%2
    else:
        print("Repeated word!")
        break

turn=(turn+1)%2
print("Player",(turn+1),"wins!")