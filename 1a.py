t1=int(input("Enter test 1 2 3 marks"))
t2=int(input())
t3=int(input())
if t3<t2 and t3<t1:
    avg=(t1+t2)/2
elif t2<t1 and t2<t3:
    avg=(t1+t3)/2
else:
    avg=(t2+t3)/2
print("Average = ",avg)