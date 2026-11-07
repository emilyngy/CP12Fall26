
t1 = int(input())
t2 = int(input())
a = [t1, t2]
while t1 >= t2:
    t3 = t1 - t2
    a.append(t3)
    t1 = t2
    t2 = t3
print(len(a))