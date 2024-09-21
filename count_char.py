d={}
s=input("Enter a string =")
for i in s:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,"occurs", v,"times")
