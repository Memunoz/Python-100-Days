import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States Game")
screen.bgpic("blank_states_img.gif")

ALIGN = "center"
FONT = ("Arial", 10, "normal")

df_state = pd.read_csv("50_states.csv")
total_states = len(df_state["state"])
knowed_states = []

while len(knowed_states) < 50:
    answer_state = screen.textinput(
        title=f"States {len(knowed_states)}/{total_states}:",
        prompt="What's another state name?",
    )

    if answer_state is None or answer_state == "Exit":
        break

    answer_state = answer_state.title()

    if answer_state in df_state.state.values and answer_state not in knowed_states:
        state_data = df_state[df_state.state == answer_state].iloc[0]
        x = int(state_data["x"])
        y = int(state_data["y"])
        knowed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state, align=ALIGN, font=FONT)
        t.hideturtle()
    else:
        t.hideturtle()
        t.goto(0, 0)

screen.mainloop()
