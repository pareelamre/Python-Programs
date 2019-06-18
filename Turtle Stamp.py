import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)

wn.exitonclick()
    
