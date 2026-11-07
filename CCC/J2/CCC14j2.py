
V = int(input())
X = input()
A = X.count("A")
B = X.count("B")
if A > B:
    print("A")
if A < B:
    print("B")
if A == B:
    print("Tie")