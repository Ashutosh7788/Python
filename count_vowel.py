d={}
vowel={'a','e','i','o','u','A','E','I','O','U'}
s= input("Enter a sting = ")
for i in s:
    if i in vowel:
        d[i]=d.get(i,0)+1
for k, v in d.items():
    print(k,"occcurs",v, " times" )
