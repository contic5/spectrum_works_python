possibleletters=60
phrase="It was the best of times, it was the worst of times."
totalletters=len(phrase)

base=1
exponent=0

for i in range(totalletters):
    base=base*possibleletters
    while(base>=10):
        exponent+=1
        base/=10

print("For a computer to randomly print out")
print(phrase)
print("With",possibleletters,"possible letters to choose from and",totalletters,"total letters in the phrase")
print("The probability is 1/(",base,"*10^",exponent,")",sep="")