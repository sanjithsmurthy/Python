num=input("Enter number")
print("Palindrome") if num==num[::-1] else print("Not Palindrome")
for i in range (10):
    if num.count(str(i))>0:
        print(i," occurs ",num.count(str(i))," times.")
