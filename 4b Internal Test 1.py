roman=input("Enter roman")
roman=roman.upper()
value={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
res=int(0)
for i in range(len(roman)):
    if i>0 and value[roman[i]]>value[roman[i-1]]:
        res+=value[roman[i]]-2*value[roman[i-1]]
    else:
        res+=value[roman[i]]
print(res)
