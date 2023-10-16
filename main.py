import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

score = 0
while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name? ").title()
    if answer_state in guessed_states:
        pass
    elif answer_state == "Exit":
        state_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                state_to_learn.append(state)
        new_data = pandas.DataFrame(state_to_learn)
        new_data.to_csv("state_to_learn.csv")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        score += 1
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
