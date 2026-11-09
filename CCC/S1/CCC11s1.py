
n = int(input())
text = ''
for i in range(n):
    text += input().lower()
s = 0
t = 0
for letter in text:
    if letter == "s":
        s += 1
    elif letter == "t":
        t += 1
if t > s:
    print('English')
else:
    print('French')