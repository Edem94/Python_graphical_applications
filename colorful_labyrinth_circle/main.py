import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.tracer(5)
turtle.width(2)
h = 0.001

for i in range(180):
    turtle.color(colorsys.hsv_to_rgb(h, 1, 1))
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.circle(50)
    turtle.left(240)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    h += 0.02
    turtle.color(colorsys.hsv_to_rgb(h, 1, 1))
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.circle(-50)
    turtle.right(240)
    turtle.forward(100)
    turtle.left(2)
    h += 0.02





