import turtle

for i in range(10, 150, 5):
    turtle.circle(i, steps=4)
    turtle.left(15)
    turtle.forward(5)
    
turtle.hideturtle()
turtle.done()