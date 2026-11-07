
A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())
TA = A3 * 3 + A2 * 2 + A1
TB = B3 * 3 + B2 * 2 + B1
if TA > TB:
    print("A")
if TA < TB:
    print("B")
if TA == TB:
    print("T")