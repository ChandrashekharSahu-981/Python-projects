import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 2)


# Helper function to dynamically calculate scores and handle ANY number of Aces
def calculate_score(hand):
    score = sum(hand)
    # Loop ensures that if you have multiple aces, they ALL convert to 1 if you are busting
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

# Check initial states
s1_user = calculate_score(user_cards)
s2_computer = calculate_score(computer_cards)

print("User cards are: ", user_cards, f" (Score: {s1_user})")
print("Computer's first card is: ", computer_cards[0])

# Check for immediate Blackjacks
if s1_user == 21:
    print("User has a BlackJack!\nYou Win!")
elif s2_computer == 21:
    print("Computer has a BlackJack!\nYou Lose!")
else:
    # USER'S TURN: Keep asking until they type 'no' or bust
    user_busted = False
    while True:
        ask = input("Do you want another card (yes/no): ").lower()
        if ask == "yes":
            user_cards.append(random.choice(cards))
            s1_user = calculate_score(user_cards)
            print("Your new cards are: ", user_cards, f" (Score: {s1_user})")

            if s1_user > 21:
                print("You bust! You lose!")
                user_busted = True
                break
        else:
            break

    # COMPUTER'S TURN: Runs only if the user didn't bust
    if not user_busted:
        print("\nComputer is playing...")
        # The classic dealer rule: Must hit until score is at least 17
        while s2_computer < 17:
            computer_cards.append(random.choice(cards))
            s2_computer = calculate_score(computer_cards)

        print(f"Final Scores -> User: {s1_user} {user_cards}, Computer: {s2_computer} {computer_cards}")

        # Final win conditions
        if s2_computer > 21:
            print("Computer busted! You Win!")
        elif s1_user > s2_computer:
            print("You win!")
        elif s1_user < s2_computer:
            print("You lose!")
        else:
            print("It's a draw!")