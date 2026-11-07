
a = int(input())
b = int(input())
if (a == 2 and b < 18) or a < 2:
    print("Before")
if (a == 2 and b > 18) or a > 2:
    print("After")
if a == 2 and b == 18:
    print("Special")