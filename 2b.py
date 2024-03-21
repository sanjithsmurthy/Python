def conv(n,f):
    if n==0 or n==1:
        return n
    else:
        return n%10+f*conv(n//10,f)
def otoh(n):
    hex=""
    while n>0:
        i=n%16
        if i<=9 and i>=0:
            hex+=str(i)
        elif i>=10 and i<16:
            hex+=chr(i+55)
        n=n//16
    return hex[::-1]
b=int(input("Enter binary and octal number: "))
o=int(input())
print(conv(b,2))
print(otoh(conv(o,8)))