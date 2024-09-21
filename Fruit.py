d={}
n=int(input("Enter the no of Fruits and vegetables=\n"))
for i in range(n):
    key=input("Enter the fruits and vegetables=")
    value=input("Enter the fruits and vegetables")
    d[key]=value
print("keys....\n")
for i in d.keys():
    print(i)
print("values.....\n")
for i in d.values():
    print(i)
for k,v in d.items():
    print(k,":",v)
    
