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
print("---------------Welcome to Auction Program!!!---------------")
print(logo)

bidder={}
repeat=True
while repeat:
    name=input("Enter the name of the bidder: ")
    price=int(input("Enter the bidding amount: $"))
    bidder[name]=price

    value=input("Is there any other bidder? Type 'yes' or 'no': ").lower()
    if value == 'yes':
        repeat=True
        print('\n'*3)
    elif value == 'no':
        repeat=False
        max_bid = max(bidder,key=bidder.get)
        print(f"The winner is {max_bid} with a bid of ${bidder[max_bid]}.")
    else:
        repeat=False
        print("Invalid Input!")