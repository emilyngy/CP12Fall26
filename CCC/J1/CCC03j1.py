
t = int(input())
s = int(input())
h = int(input())
space = " " * s
for i in range(t):
    print("*" + space + "*" + space + "*")
print("*" * (3 + 2 * s))
for a in range(h):
    print(space + " *")