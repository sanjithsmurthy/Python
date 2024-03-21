def insert(a):
    for i in range(1,len(a)):
        j=i-1
        x=a[i]
        while j>-1 and a[j]>x:
            a[j+1]=a[j]
            j-=1
        a[j+1]=x
n=int(input("enter number of elements"))
list=[]
for i in range(n):
    list.append(int(input()))
insert(list)
print("sorted list using insertion sort:",list)