from tkinter import *
from pathlib import Path
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Define file paths
front_image_path = Path(__file__).parent / "images" / "card_front.png"
back_image_path = Path(__file__).parent / "images" / "card_back.png"
right_image_path = Path(__file__).parent / "images" / "right.png"
wrong_image_path = Path(__file__).parent / "images" / "wrong.png"
data_path = Path(__file__).parent / "data" / "periodic_table_flashcards.csv"
learn_path = Path(__file__).parent / "data" / "elements_to_learn.csv"

# If the learning file already exists, load it.
# Otherwise, start with the original file containing all elements.
if learn_path.exists():
    data = pandas.read_csv(learn_path)
else: 
    data = pandas.read_csv(data_path)
    
to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    
    # Cancel the previous flip timer
    if flip_timer:
        window.after_cancel(flip_timer)
    
    # Display completion message when all elements are learned
    if not to_learn:
        canvas.itemconfig(card_title, text="Completed!", fill="black")
        canvas.itemconfig(card_word,text="You learned all 118 elements!",fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        return 
    
    # Select and display a random element
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Symbol", fill="black")
    canvas.itemconfig(card_word, text=current_card["Symbol"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    # Flip the card automatically after 3 seconds
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    # Show element information on the back of the card
    canvas.itemconfig(card_title, text="Info", fill="white")
    canvas.itemconfig(card_word,  text=f'Element Name: {current_card["Element"]}\n'
         f'Atomic Number: {current_card["Atomic Number"]}', fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    # Remove the learned element and save the remaining elements
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)  
    data.to_csv(Path(__file__).parent / "data" /"elements_to_learn.csv", index=False)
    next_card()

# ---------------------------- INTERFACE ------------------------------- #
window = Tk()
window.title("Periodic Table Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create the flashcard canvas and load images
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=front_image_path)
card_back_img = PhotoImage(file=back_image_path)

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 20, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Start the application
next_card()
window.mainloop()