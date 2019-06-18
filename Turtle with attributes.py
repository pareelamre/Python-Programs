import turtle

wn = turtle.Screen()
cl = input("Set beckground color: ")
wn.bgcolor(cl)

tess = turtle.Turtle()
clr = input("Set tess color: ")
tess.color(clr)
sz = input("Set pensize: ")
tess.pensize(int(sz))

wn.exitonclick()
