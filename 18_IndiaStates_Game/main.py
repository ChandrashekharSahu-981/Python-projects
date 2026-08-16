from pathlib import Path
import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(width=630, height=750)

image_path = Path(__file__).parent / "india_outline_map.gif"
screen.bgpic(str(image_path))

file_path = Path(__file__).parent / "indian_states.csv"
data = pandas.read_csv(file_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"States guessed: {len(guessed_states)}/28", prompt="What's another state's name?")
   
    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        file_path = Path(__file__).parent / "missing_states.csv"
        new_data.to_csv(file_path,index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())
