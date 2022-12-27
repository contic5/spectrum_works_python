#No eval version

print("Basic Calculator")

done=False
while(not done):
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    op=input("Enter the operation (+,-,*,/): ")
    equation=str(num1)+" "+op+" "+str(num2)
    res=-1
    if(op=="+"):
        res=num1+num2
    elif(op=="-"):
        res=num1-num2
    elif(op=="*"):
        res=num1*num2
    elif(op=="/"):
        res=num1/num2
    else:
        res="ERROR"
    print(equation,"=",res)
    checkdone=input("Type anything to exit. Otherwise, type return to calculate another equation.")
    if(len(checkdone)<2):
        done=True
print("Goodbye")

