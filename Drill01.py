import turtle
turtle.reset()
turtle.shape('turtle')

def top_move():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
    
def left_move():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def bottom_move():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def right_move():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

turtle.onkey(top_move,"w")
turtle.onkey(left_move,'a')
turtle.onkey(bottom_move,'s')
turtle.onkey(right_move,'d')
turtle.listen()
turtle.exitonclick()
