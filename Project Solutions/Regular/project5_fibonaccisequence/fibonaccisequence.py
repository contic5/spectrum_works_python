prev2=1
prev1=1
cur=1

fibindex=10

print("Finding element",fibindex,"of the Fibonacci Sequence")
print(prev2)
print(prev1)

for i in range(fibindex-2):
    cur=prev2+prev1
    print(prev2,"+",prev1,"=",cur)

    prev2=prev1
    prev1=cur
    
print("Element",fibindex,"is",cur)
