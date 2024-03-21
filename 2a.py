def f(n):
    if n == 1 or n == 2:
        return n - 1
    else:
        return f(n - 1) + f(n - 2)


n = int(input("Enter n"))
print(f(n)) if n > 0 else print("enter n above 0")
