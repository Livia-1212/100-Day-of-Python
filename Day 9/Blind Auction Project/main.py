# TODO-1: Ask the user for input
import art
print(art.logo)

name = ""
price = 0
bidding_dictionary = {}

# TODO-2: Save data into dictionary {name: price}
# biding_dictionary[name] = price


# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)

    highest_bid = bidding_dictionary[winner]

    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")

# TODO-3: Whether if new bids need to be added

# question = input("Are there any other bidders? Type 'yes' or 'no'. \n")

continue_bidding = True
while continue_bidding:
    name = input("Enter your name if you are going to bid: ")
    price = int(input("What is the price that you are bidding: $"))
    bidding_dictionary[name] = price
    question = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if question == 'no':
        continue_bidding = False
        find_highest_bidder(bidding_dictionary)
    elif question == 'yes':
        print("\n" * 20)


