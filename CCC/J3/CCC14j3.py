
a = 100
d = 100
n = int(input())
for i in range(n):
    b, c = [int(x) for x in input().split()]
    if b < c:
        a -= c
    elif b > c:
        d -= b
print(a)
print(d)