print("Decimal to binary")
decimal=int(input("Enter a decimal number: "))
origdecimal=decimal

binary=""

while(decimal>0):
    nextdigit=decimal%2
    nextdigit=str(nextdigit)
    print(nextdigit)
    binary=nextdigit+binary

    decimal=decimal//2
print(origdecimal,"in binary=",binary)