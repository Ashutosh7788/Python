Dec=int(input("Enter a decimal number"))
Bin=0
c=0
while(Dec>0):
    r=Dec%2
    Bin=Bin+10**c*r
    c=c+1
    Dec=Dec//2
print("binary equivalent=",Bin)
