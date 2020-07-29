import turtle
import time
import random

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("black")

tm = turtle.Turtle()
tm.shape("turtle")
tm.speed(75)

# draw lines
tm.penup()
tm.goto(-190, -180)
tm.color("yellow")
tm.pensize(6)
tm.pendown()
tm.goto(190,-180)
tm.penup()

tm.penup()
tm.goto(-160, -150)
tm.color("orange")
tm.pensize(6)
tm.pendown()
tm.goto(160,-150)
tm.penup()

tm.penup()
tm.goto(-130, -120)
tm.color("red")
tm.pensize(6)
tm.pendown()
tm.goto(130,-120)
tm.penup()

# draw cake
tm.goto(-74,-110)
tm.pendown()
tm.color("white")
tm.goto(50,-110)
tm.left(90)
tm.forward(60)
tm.left(90)
tm.forward(125)
tm.left(90)
tm.forward(60)
tm.penup()

    #draw candles
tm.goto(-60, -40)
tm.color("aquamarine")
tm.pendown()
tm.pensize(3)
tm.goto(-60, -20)
tm.penup()

tm.goto(-40, -40)
tm.color("yellow")
tm.pendown()
tm.pensize(3)
tm.goto(-40, -20)
tm.penup()

tm.goto(-20, -40)
tm.color("green")
tm.pendown()
tm.pensize(3)
tm.goto(-20, -20)
tm.penup()

tm.goto(0, -40)
tm.color("pink")
tm.pendown()
tm.pensize(3)
tm.goto(0, -20)
tm.penup()

tm.goto(20, -40)
tm.color("blue")
tm.pendown()
tm.pensize(3)
tm.goto(20, -20)
tm.penup()

    # print message
tm.goto(-110, 35)
tm.color("white")
tm.pendown()
style = ('Comic Sans', 30, 'italic')
tm.write('Happy Birthday Dear', font=style, align='center')
tm.hideturtle()

# send the turtle to the corner
tm.penup()
tm.goto(-250, 250)
   

