#AYMEN DEV 
#TESLA

import turtle

t = turtle.Turtle()

t.getscreen().bgcolor('white')
t.pencolor('black')
t.speed(1)

t.color('red')
t.penup()
t.goto(-160, 160)
t.pendown()

t.begin_fill()
t.left(18)
t.circle(-500, 40)
t.right(90)
t.forward(17)

t.right(89.5)
t.circle(500, 39)
t.right(90)
t.forward(17)
t.end_fill()


t.penup()
t.goto(-155, 133)
t.pendown()

t.begin_fill()
t.right(90.5)
t.circle(-500, 38)
t.right(70)
t.circle(-30, 80)
t.left(90)
t.circle(-20, -70)
t.right(10)
t.circle(-300, -15)
t.right(93)
t.forward(280)
t.right(160)
t.forward(280)
t.left(80)
t.circle(300, 15)
t.circle(20, 70)
t.left(80)
t.circle(30, -80)
t.end_fill()

t.penup()
t.goto(-20, 155)
t.pendown()
t.pencolor('black')
t.color('white')
t.begin_fill()
t.left(30)
t.forward(60)
t.left(130)
t.forward(65)
t.end_fill()

t.hideturtle()
turtle.done()
