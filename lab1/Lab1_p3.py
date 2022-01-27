'''
Done by : Ow Yong Chee Seng
SID: 61164992
'''

from array import array
import turtle
from turtle import *

def drawRings(num:int , colors:array)->None:
    #setting the thickness of the circle
    turtle.width(3.5)

    #always raise pen before going to coor
    turtle.penup()
    turtle.goto(-130, 0)
    # tracer(False) #tracer used to speed up debugging

    for i in range(num):
        #set pen color, and get ready to draw circle
        turtle.pencolor(colors[i])
        turtle.pendown()
        if i % 2: #number is 1, 3, means bottom circle (1 means true in boolaplha)
            turtle.circle(45, steps=90)
            turtle.penup()
            turtle.goto(turtle.xcor()+ 60, turtle.ycor() +40)
        else : #if number is 0, 2, 4, means top circle
            turtle.circle(45, steps=90)
            turtle.penup()
            turtle.goto(turtle.xcor()+ 60, turtle.ycor() -40)
        # print(turtle.xcor(), turtle.ycor())
    # tracer(True)
    

if __name__ == "__main__":
    # Creating the screen object
    screen = Screen()
    # Setting the screen color-mode
    screen.colormode(255)
    #the exact RGB colours of olympic rings in wikipedia
    colors = [(0, 129, 200), (252, 177, 49), (0, 0, 0), (0, 166, 81) , (238, 51, 78)]
    drawRings(5, colors) 
    turtle.hideturtle()
    # print("done!")
    turtle.done()
    