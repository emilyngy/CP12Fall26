
a = []
for i in range(5):
    a.append(int(input()))
a.sort()
a.pop(0)
a.pop()
b = int(input())
print(sum(a) * b)