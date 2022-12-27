factorialnum=200

base=1
exponent=0

for i in range(factorialnum,0,-1):
    base=base*i
    base=round(base,3)
    while(base>=10):
        exponent+=1
        base/=10

print(factorialnum,"! =",sep="")
print(base,"*10^",exponent,sep="")