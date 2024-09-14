n=int(input("Enter a number"))
i=2
while(i<=n//2):
    if n%i==0:
        print("composite number")
        break
    i=i+1
if i>n//2:
    print("prime number")
