import hlgame_data
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)

value=True
while value:
    score = 0
    game_over = True
    i = 0
    current = hlgame_data.data[i]

    while game_over and i < len(hlgame_data.data) - 1:
        next_item = hlgame_data.data[i+1]
        
        for key, value in current.items():
            if key != 'follower_count':
                print(f"{key.capitalize()} : {value}")
        print(vs)
        for key, value in next_item.items():
            if key != 'follower_count':
                print(f"{key.capitalize()} : {value}")

        if current['follower_count'] < next_item['follower_count']:
            winner = 'B'
            next_current = next_item
        elif current['follower_count'] > next_item['follower_count']:
            winner = 'A'
            if i == len(hlgame_data.data) - 2:
                next_current = hlgame_data.data[0]
            else:
                next_current = current

        guess = input(f"\nWho have more followers {current['name']} or {next_item['name']}?\nType 'A' for first one or 'B' for second one: ").upper()
        
        if guess == winner:
            score += 1
            print(f"\n----------Current score: {score}----------\n")
            current = next_current
            i += 1
            game_over = True
        else:
            print("You lose!")
            print(f"----------Final Score: {score}----------")
            game_over = False

    repeat=input("Do you want to play again? Type 'yes' to play again or 'no' to exit the game: ").lower()
    if repeat == 'yes':
        value=True
        print("\n")
    elif repeat == 'no':
        value=False
        print("* * *Thank you for playing the game!* * *")
    else:
        value == False
        print("You entered wrong input!")