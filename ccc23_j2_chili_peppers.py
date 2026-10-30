# CCC '23 J2 - Chili Peppers
# https://dmoj.ca/problem/ccc23j2
def spicy_level(n):
    heat = 0
    for x in range(n):
        a = input()
        if a == 'Poblano':
            heat += 1500
        elif a == 'Mirasol':
            heat += 6000
        elif a == 'Serrano':
            heat += 15500
        elif a == 'Cayenne':
            heat += 40000
        elif a == 'Thai':
            heat += 75000
        elif a == 'Habanero':
            heat += 125000
    print(heat)

n = int(input())
spicy_level(n)