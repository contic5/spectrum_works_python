import math
def quadraticformula(a,b,c):
    if(a==0):
        r1=-c/b
        return [r1]
    
    d=b**2-(4*a*c)
    if(d<0):
        return []
    elif(d==0):
        return [-b/(2*a)]
    else:
        r1=-b+math.sqrt(b**2-4*a*c)
        r1/=(2*a)

        r2=-b-math.sqrt(b**2-4*a*c)
        r2/=(2*a)
        return [r1,r2]

def writeequation(a,b,c):
    equation=""
    awritten=str(a)
    bwritten=str(b)
    cwritten=str(c)

    equation+=awritten+"x^2"
    if(b>0):
        equation+="+"
    equation+=bwritten+"x"
    if(c>0):
        equation+="+"
    equation+=cwritten
    return equation

def displayresults():
    if(len(res)==2):
        print("The roots for the",equation," are",res[0],"and",res[1])
    elif(len(res)==1):
        print("The root for the equation,",equation,"is",res[0])
    else:
        print("The equation",equation,"has no real roots")
        
print("Quadratic Formula calculator")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))


equation=writeequation(a,b,c)
res=quadraticformula(a,b,c)
displayresults()
