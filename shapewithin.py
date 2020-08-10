import turtle

shape = turtle.Turtle()
shape.color("red", "blue")
coords = []
sub = []
shape.speed(6)

# Draws a polygon with 'n' number of sides:

def polygon(n):
    x = 0
    y = 0
    t = 180*(n-2) / n
    for i in range(n):
        coords.append(shape.pos())
        shape.lt(180 - t)
        shape.fd(1000/n)
    for j in coords:
        sub.append(list(j))
    for k in range(n):
        x += sub[k][0]
        y += sub[k][1]
    x /= n
    y /= n
    invert = False
    for j in range(n):

        if invert == True:
            shape.color("red", "blue")
            shape.begin_fill()
            shape.goto(sub[j][0], sub[j][1])
            shape.goto(x, y)
            shape.goto(sub[j + 1][0], sub[j + 1][1])
            shape.end_fill()
            invert = False
        else:
            shape.color("red", "yellow")
            shape.begin_fill()
            shape.goto(sub[j][0], sub[j][1])
            shape.goto(x, y)
            shape.goto(sub[j + 1][0], sub[j + 1][1])
            shape.end_fill()
            invert = True
# turtle.done()



polygon(7)
turtle.done()



















