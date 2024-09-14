n=int(input("Enter a  number"))
m=int(input("Enter another number"))
r=1
if n<m:
    n=m+n
    m=n-m
    n=n-m
while(r>0):
    r=n%m
    if(r==0):
        HCF=m
        break
    n=m
    m=r
print("HCF=",m)
