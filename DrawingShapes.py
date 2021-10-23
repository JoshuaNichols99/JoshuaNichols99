import turtle
#Variables
pen_size = int()
pen_color = str()
fill_color = str()
ask_shape = str()
ask_location = str()

#Inputs
ask_shape = input("Choose Shape: [square,circle] ")
ask_location = input("Select a Location: [top left,top right, bottom left, bottom right] ")

#Location
if ask_location == "top left":
    pen_size = 3
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
if ask_location == "top right":
    pen_size = 5
    turtle.penup()
    turtle.goto(200, 200)
    turtle.pendown()
if ask_location == "bottom left":
    pen_size = 7
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
if ask_location == "bottom right":
    pen_size = 9
    turtle.penup()
    turtle.goto(200, -200)
    turtle.pendown()

#Drawing a Circle Processes
if ask_shape == "circle":
    pen_color = input("Color of Pen: [red, blue, yellow] ")
    if pen_color == "red":
        fill_color = "blue"
    if pen_color == "blue":
        fill_color = "red"
    if pen_color == "yellow":
        fill_color = "orange"
    
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)

    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

#Drawing a Square Processess
if ask_shape == "square":
    fill_color = input("Color of filled shape: [red,blue,yellow] ")
    if fill_color == "red":
        pen_color = "blue"                  
    if fill_color == "blue":
        pen_color = "red"
    if fill_color == "yellow":
        pen_color = "orange"
    

    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)

    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()
