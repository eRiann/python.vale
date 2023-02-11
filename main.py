from math import sin, pi
import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
s.bgcolor("#F7E2E2")
t.speed(1)


colors = ["black", "blue", "dodger blue", "deep sky blue", "green", "violet", "pink"]

def color(iteration):
    t.pencolor(colors[iteration % len(colors)])
    
def at(x, y):
    t.penup()
    t.home()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()

def heart(size, shape):
    t.pensize(5)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.right(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 14):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        
hearts()

t.penup()
t.goto(0,-100)
t.color("red")
t.write("Hi, Sayanggg", None, "center", "14pt")
t.goto(1,-125)
t.write("Ini valentine gift special for u", None, "center", "14pt")
t.goto(2,-150)
t.write("Maaf karna cuma dari codingan doang", None, "center", "14pt")
t.goto(3,-175)
t.write("Semoga suka yaaa", None, "center", "14pt")
t.goto(4,-200)
t.write("I LOVE YOUUU 3000 <3", None, "center", "14pt")
t.color("white")
t.goto(0,-300)

s.exitonclick()
