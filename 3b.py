s1=input("Enter 1: ")
s2=input("Enter 2: ")
count=0
if len(s1)>len(s2):
    s=len(s2)
    l=len(s1)
else:
    s=len(s1)
    l=len(s2)
for i in range(s):
    if s1[i]==s2[i]:
        count+=1
similarity=count/l
print(similarity)
