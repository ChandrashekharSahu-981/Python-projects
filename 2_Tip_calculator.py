print("Welcome to Tip calculator!")
amount=float(input("What was the total bill? :"+"$"))
tip=int(input("How much tip you like to give? (10, 15, or 20 percent): "))
amount += (amount * tip/100)
people=int(input("How many people to split the bill? :"))
split=amount/people
print(f"Each person should pay: ${split:.2f}")