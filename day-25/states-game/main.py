import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
list_states = data.state.to_list()
game_is_on = True
corrects = 0
list_correct = []

while game_is_on:
    answer_state = screen.textinput(title=f"{corrects}/50 States Correct",
                                    prompt="What's another state's name?").title()  # saves doing it on another line

    if answer_state == "Exit":
        break
    if answer_state in list_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        corrects += 1
        list_states.remove(answer_state)
        list_correct.append(answer_state)

        if corrects == 5:
            game_is_on = False
            t.goto(0, 0)
            t.write("YOU WIN!", font=('Arial', 40, 'normal'))

df = pandas.DataFrame(list_states)
df.to_csv("./missed_states.csv")
