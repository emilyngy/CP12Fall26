
teacher = []
student = []
qs = int(input())
for i in range(qs):
    teacher.append(input())
for i in range(qs):
    student.append(input())
score = 0
for i in range(qs):
    if teacher[i] == student[i]:
        score += 1
print(score)