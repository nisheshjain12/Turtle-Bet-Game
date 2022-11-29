from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
userBet = screen.textinput(title="Make your Bet",prompt="which turtle will win the race?")
colors = ["red","orange","yellow","blue","green","purple"]
y_pos  = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    t1 = Turtle(shape='turtle')
    t1.penup()
    t1.color(colors[turtle_index])
    t1.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(t1)
    
if userBet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner  == userBet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_dis = random.randint(0,10)
        turtle.forward(rand_dis)


screen.exitonclick()