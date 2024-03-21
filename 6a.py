import os
import sys
file=input("enter file name")
if not os.path.isfile(file):
    print("file not found")
    sys.exit(0)
infile=open(file,"r")
L=infile.readlines()
for i in L:
    print(i)
word=input("enter word")
cnt=0
for i in L:
    cnt+=i.count(word)
print(word," occurs ",cnt," times")
