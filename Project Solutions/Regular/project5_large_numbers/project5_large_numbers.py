orig_base=2
orig_exponent=50

ten_base=1
ten_exponent=0

for i in range(orig_exponent):
    ten_base=ten_base*orig_base
    ten_base=round(ten_base,3)
    while(ten_base>=10):
        ten_exponent+=1
        ten_base/=10

ten_base=round(ten_base,3)
print(orig_base,"^",orig_exponent,"=")
print(ten_base,"*10^",ten_exponent,sep="")