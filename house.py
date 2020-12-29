#https://www.101computing.net/python-turtle-my-house/

import turtle

pen = turtle.Turtle()
pen.speed(100)
pen.color(0, 0, 0)
window = turtle.Screen()
#window.screensize(500, 500)
window.colormode(255)
window.bgcolor((66, 202, 244))

def drawSun(pen, x, y, size):
    pen.setheading(0)
    pen.fillcolor("yellow")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

def drawCloud(pen, x, y):
    pen.setheading(90)
    pen.fillcolor("white")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.color("white")
    for x in range(10):
        pen.circle(20)
        pen.right(36)
        pen.forward(10)
    pen.end_fill()
    pen.setheading(90)

def drawBush(pen, x, y):
    pen.setheading(90)
    pen.fillcolor("darkgreen")
    pen.width(5)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()

    pen.color("darkgreen")
    for x in range(10):
        pen.circle(15)
        pen.right(36)
        pen.forward(10)
    pen.end_fill()
    pen.setheading(90)

def drawDoor(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(90)
    pen.fillcolor(180, 0, 0)
    pen.begin_fill()
    for x in range(2):
        pen.forward(80)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.fillcolor("yellow")
    pen.penup()
    pen.goto(x, y+40)
    pen.begin_fill()
    pen.circle(4)
    pen.end_fill()

def drawHouse(pen):
    pen.color(0,0,0)
    pen.penup()
    pen.goto(-160, -20)
    pen.pendown()
    pen.setheading(90)
    pen.fillcolor("white")
    pen.begin_fill()
    pen.forward(150)
    roof1 = pen.position()
    pen.right(90)
    pen.forward(300)
    roof2 = pen.position()
    pen.right(90)
    pen.forward(150)
    pen.right(90)
    pen.forward(300)
    pen.right(90)
    pen.end_fill()

    pen.penup()
    pen.goto(roof1)
    pen.fillcolor(244, 131, 66)
    pen.begin_fill()
    pen.pendown()
    pen.goto(-10, 200)
    pen.goto(roof2)
    pen.goto(roof1)
    pen.end_fill()
    pen.setheading(90)

def drawWindows(pen, x, y, shape):
    pen.width(4)
    pen.color("black")
    pen.fillcolor("lightblue")

    if shape == "square":
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()

        for y in range(4):
            for x in range(4):
                pen.forward(20)
                pen.right(90)
            pen.left(90)
        pen.end_fill()
    elif shape == "circle":
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.backward(20)
        pen.right(90)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()

        pen.goto(x,y)
        for x in range(2):
            pen.forward(20)
            pen.backward(40)
            pen.forward(20)
            pen.right(90)

def drawPath(pen):
    pen.setheading(90)
    pen.color(0, 0, 0)
    pen.fillcolor(150, 80, 0)
    pen.penup()
    pen.goto(-55, -200)
    pen.begin_fill()
    pen.pendown()
    pen.right(10)
    pen.forward(200)
    pen.right(80)
    pen.forward(40)
    pen.right(80)
    pen.forward(200)
    pen.right(80)
    pen.end_fill()
    pen.setheading(90)

def drawGrass(pen):
    pen.setheading(90)
    pen.fillcolor(5, 115, 3)
    pen.penup()
    pen.setheading(90)
    pen.goto(-400, -200)
    pen.begin_fill()

    for x in range(2):
        pen.forward(200)
        pen.right(90)
        pen.forward(800)
        pen.right(90)
    pen.end_fill()

def drawFence(pen):
    pen.setheading(90)
    pen.color(0, 0, 0)
    pen.penup()
    pen.goto(-200, -200)
    pen.pendown()
    pen.setheading(90)

    pen.fillcolor(115, 79, 3)
    pen.begin_fill()
    for x in range(13):
        pen.forward(100)
        pen.right(45)
        pen.forward(20)
        pen.right(90)
        pen.forward(20)
        pen.right(45)
        pen.forward(100)
        pen.left(90)
        pen.forward(4)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(50, -140)
    pen.pendown()
    pen.fillcolor(177, 188, 177)
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()



drawCloud(pen, 75, 160)
drawSun(pen, -460, 290, 100)
drawGrass(pen)
drawBush(pen, 120, 35)
drawPath(pen)
drawHouse(pen)
drawFence(pen)
drawDoor(pen, -25, -20)
drawWindows(pen,-95, 15,"square")
drawWindows(pen,75, 15,"square")
drawWindows(pen, -95, 100, "square")
drawWindows(pen, 75, 100, "square")
drawWindows(pen, -10, 100, "circle")
turtle.exitonclick()