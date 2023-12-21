import turtle

turtle.speed(2)
turtle.bgcolor("black")

def sun():
    turtle.penup()
    turtle.color("yellow")
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    turtle.penup()
    turtle.color("yellow")
    for _ in range(12):
        turtle.goto(0, 40)
        turtle.pendown()
        turtle.forward(150)
        turtle.right(30)

    turtle.penup()
    turtle.color("black")
    turtle.goto(-40, 40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(40, 40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.width(5)
    turtle.goto(-30, -10)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30, 180)

sun()
turtle.exitonclick()
