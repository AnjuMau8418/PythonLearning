# Bid Auction program
print("Welcome to the secret auction program! ")
bidding_finished = False
bids = {}


def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The {winner} is winner with the bid ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name? : ")
    price = int(input("What's your bid? : $"))
    bids[name] = price
    should_continue = input("Are there any extra bidden? type 'Yes' or 'No' ?\n").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
