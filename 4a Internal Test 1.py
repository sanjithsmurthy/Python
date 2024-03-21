def insertion_sort(a):
    for i in range(1,len(a)):
        j=i-1
        x=a[i]
        while j>-1 and a[j]>x:
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
        i=j=k=int(0)
        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                a[k]=r[j]
                j+=1
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            k+=1
        while i<len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j<len(r):
            a[k] = r[j]
            j += 1
            k += 1
n=int(input("Enter n: "))
a=[]
for i in range(n):
    a.append(int(input()))
b=a
insertion_sort(a)
merge_sort(b)
print(a)
print(b)
