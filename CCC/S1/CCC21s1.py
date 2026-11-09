
n = int(input())
a = 0
h = [int(x) for x in input().split()]
w = [int(y) for y in input().split()]
for i in range(n):
    b = w[i]*(h[i]+h[i+1])/2
    a += b
print(a)