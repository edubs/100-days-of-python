import os


print("--- auction art ---")

bids = {
    "tom": 1,
    "jim": 233,
    "Erik": 14,
    "jimborino": 1341
}
bidding_open = True
highest_bid = 0
highest_bidder = ""
while bidding_open:
    name = input("What is your name?\n")
    bid = input("What is your bid? \n$")
    bids[name] = bid

    keep_bidding = int(input("Are there other users who want to bid? Enter '1' for yes, enter '0' for no.\n"))
    if not keep_bidding:
        bidding_open = False
    else:
        os.system('clear')

for b in bids:
    print(b)
    print(bids[b])
    if int(bids[b]) > highest_bid:
        highest_bid = bids[b]
        highest_bidder = b
print(f"Highest bid {highest_bid} from {highest_bidder}")
