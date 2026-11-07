
D = int(input())
E = int(input())
for i in range(E):
    symbol = input()
    Q = int(input())
    if symbol == "+":
        D += Q
    elif symbol == "-":
        D -= Q
print(D)