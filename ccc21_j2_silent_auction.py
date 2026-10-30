# CCC '21 J2 - Silent Auction
# https://dmoj.ca/problem/ccc21j2
def winner():
    n = int(input())
    highest_bid = 0
    for x in range(n):
        name = input()
        bid = int(input())
        if bid > highest_bid:
            highest_bid = bid
            the_winner = name
    print(the_winner)
winner()