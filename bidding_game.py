
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bid = {}


def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bidding_amount =int( bidding_dictionary[bidder])
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder

    print(f"{winner} is highest bid RS {highest_bid}")


continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    bid_price = input("What is your bid? ")
    bid[name] = bid_price
    should_continue = input("Would you like to continue (y/n)? ")
    if should_continue == "n":
        continue_bidding = False
        find_highest_bid(bid)

    elif should_continue == "y":
        print("\n" * 40)








