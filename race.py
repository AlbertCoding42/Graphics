import turtle
import time
from turtle import Turtle
from random import randint

# Window setup:

window = turtle.Screen()
window.title("TURTLE RACE")
turtle.hideturtle()
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-100,200)
turtle.write("Turtle Race", font = ("Arial", 30, "bold"))
turtle.penup()

# Dirt:
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
for i in range(2):
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()

# finishline:

stamp_size = 20
square_size = 15
finish_line = 200
turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size)- (j * square_size * 2)))
    turtle.stamp()

# Turtle 1:

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

# Turtle 2:

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# Turtle 3:

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("yellow")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# Turtle 4:

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("magenta")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(2)

# Race timer:

turtle.setpos(-175, 25)
turtle.color("white")
turtle.write("Race begins in: ", font = ("Arial", 35, "bold"))
turtle.setpos(-25, -25)
turtle.color("red")
turtle.write("3", font = ("Arial", 25, "bold"))
time.sleep(1)
turtle.color("forestgreen")
turtle.write("3", font = ("Arial", 25, "bold"))
turtle.color("red")
turtle.write("2", font = ("Arial", 25, "bold"))
time.sleep(1)
turtle.color("forestgreen")
turtle.write("2", font = ("Arial", 25, "bold"))
turtle.color("red")
turtle.write("1", font = ("Arial", 25, "bold"))
time.sleep(1)

turtle.color("forestgreen")
turtle.write("1", font = ("Arial", 25, "bold"))
turtle.setpos(-175, 25)
turtle.color("forestgreen")
turtle.write("Race begins in: ", font = ("Arial", 35, "bold"))

# Move turtles:

for i in range(145):
    turtle1.fd(randint(1,5))
    turtle2.fd(randint(1,5))
    turtle3.fd(randint(1,5))
    turtle4.fd(randint(1,5))

coords = []

coords.append(turtle1.xcor())
coords.append(turtle2.xcor())
coords.append(turtle3.xcor())
coords.append(turtle4.xcor())
time.sleep(1)

# Winner:

if turtle1.xcor() == max(coords):
    turtle.setpos(-175, 25)
    turtle.color("black")
    turtle.write("Black Wins!", font=("Arial", 35, "bold"))
elif turtle2.xcor() == max(coords):
    turtle.setpos(-175, 25)
    turtle.color("cyan")
    turtle.write("Cyan Wins!", font=("Arial", 35, "bold"))
elif turtle3.xcor() == max(coords):
    turtle.setpos(-175, 25)
    turtle.color("yellow")
    turtle.write("Yellow Wins!", font=("Arial", 35, "bold"))
elif turtle4.xcor() == max(coords):
    turtle.setpos(-175, 25)
    turtle.color("magenta")
    turtle.write("Magenta Wins!", font=("Arial", 35, "bold"))

turtle.exitonclick()

turtle.done()