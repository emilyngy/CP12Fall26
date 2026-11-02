import random
while True:
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    level = int(input('Choose your level:'))
    if level == 1:
        words = ['blue', 'red', 'apple', 'banana']
        attempt = 10
        break
    elif level == 2:
        words = ['monkey', 'volcano', 'neutron', 'technology']
        attempt = 12
        break
    elif level == 3:
        words = ['rhythm', 'halloween', 'supercalifragilisticexpialidocious']
        attempt = 15
        break
    else:
        print('Try again')

target = random.choice(words)
progress = ['_'] * len(target)
print(progress)

while attempt > 0:
    guess = input('Enter a letter:')
    if guess not in target:
        attempt -= 1
        print(f'Wrong guess! You have {attempt} attempts left')
    else:
        for i in range(len(progress)):
            if guess == target[i]:
                progress[i] = guess
    print(*progress)
    if '_' not in progress:
        print('Win')
        break
if attempt == 0:
    print('Lose')
