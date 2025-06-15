from art import logo

print(logo)
user_bids = {}
is_bid_on = True
while is_bid_on:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid amount: $"))
    user_bids[name] = bid
    continue_bid = input("Are there any other bidders? Enter 'yes' or 'no: ").lower()
    print("\n" * 10)
    if continue_bid == "yes":
        pass
    elif continue_bid == "no":
        max_bidder = max(user_bids, key = user_bids.get)
        print(f"The winner of this auction is {max_bidder} with a "
              f"maximum bid of {user_bids[max_bidder]}!")
        is_bid_on = False
    else:
        print("Incorrect value entered!")
        is_bid_on = False
