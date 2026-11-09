
n = int(input())
a = []
max = 0
for i in range(n):
    t, x = [int(x) for x in input().split()]
    a.append([t, x])
a.sort()
for i in range(n-1):
    t1, x1 = a[i]
    t2, x2 = a[i+1]
    if x2 >= x1:
        speed = (x2-x1)/(t2-t1)
    elif x2 < x1:
        speed = (x1-x2)/(t2-t1)
    if speed > max:
        max = speed
print(max)