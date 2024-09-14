n=int(input("Enter a no"))
m=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
if m==rev:
    print("palindrome number")
else:
    print("Not a palimdrome number")
