from array import array
import turtle
from turtle import *

def drawRings(num:int , colors:array)->None:
    turtle.width(3.5)
    turtle.penup()
    turtle.goto(-130, 0)
    #tracer(False)
    for i in range(num):
        turtle.pencolor(colors[i])
        turtle.pendown()
        if i % 2: 
            turtle.circle(45, steps=90)
            turtle.penup()
            turtle.goto(turtle.xcor()+ 60, turtle.ycor() +40)
        else : 
            turtle.circle(45, steps=90)
            turtle.penup()
            turtle.goto(turtle.xcor()+ 60, turtle.ycor() -40)
        # print(turtle.xcor(), turtle.ycor())
    #tracer(True)




if __name__ == "__main__":
    # Creating the screen object
    screen = Screen()
    # Setting the screen color-mode
    screen.colormode(255)
    colors = [(0, 129, 200), (252, 177, 49), (0, 0, 0), (0, 166, 81) , (238, 51, 78)]
    drawRings(5, colors) 
    turtle.hideturtle()
    turtle.done()