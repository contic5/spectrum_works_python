print("Binary to decimal")
binary=input("Enter a binary number (all 0s and 1s): ")
decimal=0
for i in range(len(binary)-1,-1,-1):
    place=len(binary)-1-i
    addval=int(binary[i])*(2**place)
    print(addval)
    decimal+=addval
print(binary,"in decimal=",decimal)