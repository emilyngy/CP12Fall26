
a = input()
b = a.count(":-)")
c = a.count(":-(")
if b > c:
    print("happy")
elif b < c:
    print("sad")
elif b == 0 and c == 0:
    print("none")
else:
    print("unsure")