sen=input("Enter sentence: ")
n=w=u=l=0
w=len(sen.split())
for i in sen:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        n+=1
print(w,"\n",u,"\n",l,'\n',n)
