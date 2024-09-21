d={}
n=int(input("Enter the number of Students="))
for i in range(n):
    key=input("Enter the roll no=")
    value=input("Enter Name=")
    d[key]=value
print("keys....\n")
for i in d.keys():
    print(i)
print("values.....\n")
for i in d.values():
    print(i)
for k,v in d.items():
    print(k,":",v)
    
