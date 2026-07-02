import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States game")
image = "map.gif"
screen.setup(width=734, height=862)
turtle.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("red")

states_df = pd.read_csv("states_name.csv")
guessed_states=[]

while len(guessed_states)<len(states_df['state']):
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states_df['state'])} correct guess", prompt="what is the state name?").strip().title()
    # print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state in states_df["state"].values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = states_df[states_df["state"] == answer_state]
        x=state_data.x.item()
        y=state_data.y.item()
        writer.goto(x, y)
        writer.write(answer_state)
        writer.pencolor("red")

remaining_guesses = [state
                     for state in states_df['state']
                     if state not in guessed_states
                     ]

df = pd.DataFrame(remaining_guesses)
df.to_csv("states_to_learn.csv", index=False)
