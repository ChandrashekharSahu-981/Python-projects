print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island !!!")
print("Your mission is to find the hidden treasure.\n")

direction = input(
    "You are at a crossroad.\n"
    "Type 'l' to go left.\n"
    "Type 'r' to go right.\n"
).lower()

if direction == "l":

    print("\nYou have reached the bank of a river.")

    choose = input(
        "Type 'w' to wait for a boat.\n"
        "Type 's' to swim across the river.\n"
    ).lower()

    if choose == "w":

        print("\nA boat arrives and takes you safely to the island.")
        print("You have reached Treasure Island!")

        path = input(
            "\nThere are two paths in front of you.\n"
            "Type 'c' to enter the cave.\n"
            "Type 'f' to follow the forest path.\n"
        ).lower()

        if path == "c":

            print("\nYou enter a dark cave.")
            print("You find a small wooden box containing a key! 🔑")

            key = input(
                "\nDo you want to take the key?\n"
                "Type 'y' for yes or 'n' for no.\n"
            ).lower()

            if key == "y":

                print("\nYou take the key and continue deeper into the cave.")
                print("You find a large room with three doors.")

                door = input(
                    "\nChoose a door:\n"
                    "Type 'r' for the red door.\n"
                    "Type 'b' for the blue door.\n"
                    "Type 'g' for the green door.\n"
                ).lower()

                if door == "g":

                    print("\nThe key unlocks the green door!")
                    print("Inside you find a huge chest full of gold! 💰")
                    print("\nCONGRATULATIONS! YOU FOUND THE TREASURE!")
                    print("*** YOU WIN! ***")

                elif door == "r":

                    print("\nYou open the red door.")
                    print("A giant snake attacks you! 🐍")
                    print("*** GAME OVER ***")

                elif door == "b":

                    print("\nYou open the blue door.")
                    print("The room is filled with water!")
                    print("You are trapped.")
                    print("*** GAME OVER ***")

                else:

                    print("\nYou chose an invalid door.")
                    print("*** GAME OVER ***")

            else:

                print("\nYou leave the key behind.")
                print("Unfortunately, you cannot open the treasure room.")
                print("*** GAME OVER ***")

        elif path == "f":

            print("\nYou enter the forest.")
            print("You find a mysterious old man.")

            choice = input(
                "He offers you two objects:\n"
                "Type 'm' to take the map.\n"
                "Type 'p' to take the potion.\n"
            ).lower()

            if choice == "m":

                print("\nThe map leads you directly to the treasure!")
                print("You find a chest full of diamonds! 💎")
                print("*** YOU WIN! ***")

            elif choice == "p":

                print("\nYou drink the potion.")
                print("It was actually poison! ☠️")
                print("*** GAME OVER ***")

            else:

                print("\nYou walk away from the old man.")
                print("You get lost in the forest.")
                print("*** GAME OVER ***")

        else:

            print("\nYou chose an invalid path.")
            print("*** GAME OVER ***")

    else:

        print("\nYou try to swim across the river.")
        print("A shark attacks you! 🦈")
        print("*** GAME OVER ***")

elif direction == "r":

    print("\nYou walk towards the valley.")
    print("The ground suddenly disappears beneath your feet!")

    choice = input(
        "You are falling!\n"
        "Type 'jump' to try to grab a tree branch.\n"
        "Type 'wait' and hope someone saves you.\n"
    ).lower()

    if choice == "jump":

        print("\nYou grab a tree branch!")
        print("You climb back up safely.")
        print("You discover a hidden path leading to the treasure!")

        print("\nCONGRATULATIONS! YOU FOUND THE TREASURE!")
        print("*** YOU WIN! ***")

    elif choice == "wait":

        print("\nNobody comes to rescue you.")
        print("You fall into the valley.")
        print("*** GAME OVER ***")

    else:

        print("\nYou made the wrong choice.")
        print("*** GAME OVER ***")

else:

    print("\nYou entered an invalid direction.")
    print("*** GAME OVER ***")