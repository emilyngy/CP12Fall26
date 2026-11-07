
B = int(input())
T = int(input())
P = int(input())
if B > T-P:
    print("N")
else:
    print("Y", T - P - B)