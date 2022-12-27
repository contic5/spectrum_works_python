def sumpower(start,end,power):
    res=0
    for i in range(start,end+1):
        res+=i**power
    return res
def writeequation(start,end,power):
    val=sumpower(start,end,power)
    res="The sum of i"+"^"+str(power)
    res+=" from "+str(start)+" to "+str(end)
    res+="="+str(val)
    return res

eq1=writeequation(1,5,1)
print(eq1)

eq2=writeequation(1,5,2)
print(eq2)

eq3=writeequation(10,20,1)
print(eq3)

eq4=writeequation(10,20,2)
print(eq4)
