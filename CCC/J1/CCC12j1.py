
a = int(input())
b = int(input())
if b - a < 1:
    print("Congratulations, you are within the speed limit!")
if 1 <= b - a <= 20:
    print("You are speeding and your fine is $100.")
if 21 <= b - a <= 30:
    print("You are speeding and your fine is $270.")
if 31 <= b - a:
    print("You are speeding and your fine is $500.")