
letters = {'I', 'O', 'S', 'H', 'Z', 'X', 'N'}
word = input().upper()
a = True
for x in word:
    if x not in letters:
        a = False
        break
if a:
    print('YES')
else:
    print('NO')