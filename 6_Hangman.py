import random
print("Welcome to Hangman game!")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
word_list = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure",
    "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle",
    "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords",
    "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle",
    "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves",
    "embezzle", "equip", "espionage", "euouae", "exodus",
    "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny",
    "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess",
    "haiku", "haphazard", "hyphen",
    "iatrogenic", "icebox", "injury", "ivory", "ivy",
    "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo",
    "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack",
    "larynx", "lengths", "lucky", "luxury", "lymph",
    "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify",
    "naphtha", "nightclub", "nowadays", "numbskull", "nymph",
    "onyx", "ovary", "oxidize", "oxygen",
    "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling",
    "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum",
    "razzmatazz", "rhubarb", "rhythm", "rickshaw",
    "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome",
    "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths",
    "unknown", "unworthy", "unzip", "uptown",
    "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism",
    "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern",
    "xylophone",
    "yachtsman", "yippee", "yoked", "youthful", "yummy",
    "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie",
]

lives=6
print("You have only 6 lives to play the game!")
choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
n=len(choosen_word)
for pos in range(n):
    placeholder+='_'
print(placeholder)

correct_letters=[]
game_over = False
while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess=input("Enter your guess: ")

    if guess in correct_letters:
        print(f"{guess} is already guessed!")

    display=""
    for letter in choosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    print(display)
    
    if guess not in choosen_word:
        lives -= 1
        print("Incorrect guess!")
        print(f"{guess} is not in the choosen word!")
        if lives == 0:
            game_over = True
            print("\t***********You Lose!***********\n\t\t***Game Over***")
    if display == choosen_word:
        game_over=True
        print("You guessed the correct word!")
        print("\t***********You win!***********\n\t\t***Game Over***")

    print(stages[lives])