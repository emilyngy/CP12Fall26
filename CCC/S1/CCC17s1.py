
n = int(input())
s1 = [int(x) for x in input().split()]
s2 = [int(y) for y in input().split()]
sum_s1 = 0
sum_s2 = 0
ans = 0
for i in range(n):
    sum_s1 += s1[i]
    sum_s2 += s2[i]
    if sum_s1 == sum_s2:
        ans = i+1
print(ans)