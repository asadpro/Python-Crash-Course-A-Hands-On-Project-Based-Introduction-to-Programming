from turtle import Turtle, Screen
import time


# Creating a turtle
tim = Turtle()
tim.pencolor("red")
tim.penup()
tim.hideturtle()

# Creating a screen
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.tracer(0)

counter = 0


watch_is_on = True
while watch_is_on:
    time.sleep(1)
    counter += 1
    tim.write(counter, align="center", font=("courier", 88, "bold"))
    screen.update()
    tim.clear()
