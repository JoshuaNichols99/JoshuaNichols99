import turtle
import random
import time
#Variable
colors = ["red", "blue", "yellow", "green"]
#Sets screen size of window
turtle.setup(600,600)
#Text for screen of window
turtle.write(arg = "Ready for more circles?",align = "center" ,font = ("Airal", 16,"bold"))
#Pauses text of screen of window and clears text
time.sleep(3.0)
turtle.clear()
#Loop to draw Circles.
for count in range(0,20,1):
    #Sets the fill color, pen size, and fill color
    turtle.fillcolor(random.choice(colors))
    turtle.pensize(random.randint(0,10))
    turtle.begin_fill()
    #Draws a Circle
    turtle.circle(random.randint(25,125))
    #Moving the turtle
    turtle.penup()
    turtle.goto(random.randint(-150,150),random.randint(-150,150))
    turtle.pendown()
    turtle.end_fill()
    
