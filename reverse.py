n=int(input("Enter a number"))
Rev=0
while(n!=0):
    R=n%10
    Rev=Rev*10+R
    n=n//10
print("Reverse no=",Rev)
