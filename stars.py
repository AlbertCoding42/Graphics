import turtle


bob = turtle.Turtle()
bob.getscreen().bgcolor("#ABEBC6")
bob.color("red")
bob.speed(0)
bob.penup()
bob.goto((-200),(100))
bob.pendown()
bob.speed(10)

# Draw stars:

def stars(turtle, size):
    if size < 25:
        return
    else:
        for i in range(5):
           turtle.forward(size)
           stars(bob, size / 3)
           turtle.left(216)


stars(bob, 300)
turtle.done()
