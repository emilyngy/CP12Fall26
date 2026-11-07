
score = []
n = int(input())
for i in range(n):
    score.append(int(input()))
score.sort(reverse=True)
goldIndex = 0
goldCount = score.count(score[goldIndex])
silverIndex = goldCount
silverCount = score.count(score[silverIndex])
bronzeIndex = goldCount + silverCount
bronzeCount = score.count(score[bronzeIndex])

print(score[bronzeIndex], bronzeCount)