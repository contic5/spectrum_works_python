'''
Avatar intro

"Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
Then, everything changed when the Fire Nation attacked. 
Only the Avatar, master of all four elements, could stop them, 
but when the world needed him most, he vanished. 
A hundred years passed and my brother and I discovered the new Avatar, 
an airbender named Aang. 
And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
But I believe Aang can save the world."
'''

element1=input("Enter an element: ")
element2=input("Enter an element: ")
element3=input("Enter an element: ")
element4=input("Enter an element: ")

number1=input("Enter a number: ")

noun=input("Enter a noun: ")

verb1=input("Enter a verb: ")
pastverb1=input("Enter a past tense verb: ")

number2=input("Enter a number: ")
name=input("Enter a name: ")

adjective=input("Enter an adjective: ")
verb2=input("Enter a verb: ")
verb3=input("Enter a verb: ")

print("For extra fun, put this in a text to speech device so you can hear it in a natural voice.")
print()
print(element1,".",element2,".",element3,".",element4,". Long ago, the ",number1," nations lived together in harmony",sep="")
print("Then, everything changed when the ",element3," nation attacked",sep="")
print("Only the ",noun,", master of all ",number1," elements, could stop them,",sep="")
print("but when the world needed him most he ",pastverb1,sep="")
print("A ",number2," years passed and my brother and I discovered the new ",noun,sep="")
print("An ",element4,"bender named ",name,sep="")
print("And although his ",element4,"bending skills are ",adjective," he has a lot to learn before he's ready to ",verb2," anyone.",sep="")
print("But I believe ",name," can ",verb3," the world",sep="")