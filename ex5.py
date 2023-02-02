first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first > second else second
while gcd:
    if first % gcd == 0 and second % gcd == 0:
        print(gcd)
        break
    gcd -= 1