def insertion(a):
    for i in range(1,len(a)):
        j=i-1
        x=a[i]
        while j>-1 and a[i]>x:
            a[j+1]=a[j]
            j-=1
        a[j+1]=x
def merge_sort(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            if l[i]>r[j]:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            k+=1
            i+=1
        while j<len(r):
            a[k]=r[j]
            k+=1
            j+=1
a=[]
n=int(input("Enter n "))
for i in range(n):
    elem=int(input())
    a.append(elem)
b=a
insertion(a)
merge_sort(b)
print("Insertion Sort\n",a,"\nMerge Sort\n",b)