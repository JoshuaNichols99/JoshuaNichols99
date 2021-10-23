import turtle
import time
import random

def Mountains(color,size):
    turtle.reset()
    #Settings for PenColor and PenSize 
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.shape("turtle")
    #Moves Turtle up the Mountains
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for count in range (0,4,1):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
       
    turtle.forward(50)
    DisplayMessage("Hurray! Made it to the top!",200)
    turtle.color("green")

def DisplayMessage(text,space):
    #Positions Turtle to display a Message
    turtle.penup()
    turtle.left(180)
    turtle.forward(space)
    turtle.left(180)
    turtle.pendown()
    #Settings for PenColor and PenSize 
    turtle.pensize(6)
    turtle.pencolor("black")   
    #Displays Message
    turtle.pendown()
    turtle.write(arg = text,font = ("Airal", 16,"bold"))
    turtle.penup()
    turtle.forward(space)

def Swim(color,size):
    turtle.reset()
    #Settings for PenColor and PenSize 
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.shape("classic")
    #Location of the Pond
    turtle.penup()
    turtle.goto(-150,50)
    turtle.pendown()
    #Creates a Pond for the turtle
    turtle.begin_fill()
    turtle.circle(110)
    turtle.fillcolor("white")
    turtle.end_fill()
    turtle.penup() 
    turtle.pensize(size)
    turtle.pencolor("blue")
    #Creates a Pond for the turtle
    turtle.shape("turtle")
    turtle.pendown()
    turtle.pensize(size)
    turtle.pencolor("blue")
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.begin_fill()
    turtle.shape("classic")
    turtle.circle(90)
    turtle.fillcolor("blue")
    turtle.end_fill()
    turtle.penup()
    #Displays Message
    turtle.goto(-150,150)
    DisplayMessage("Yeah! I'm swimming!",170)
    turtle.shape("turtle")
    turtle.color("green")
    turtle.left(90)

def Eat():
    turtle.reset()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-200,-200)
    turtle.pendown()
    #Variables
    colors = ["red", "blue", "yellow","pink","purple","pink","orange"]
    #Sets the Turtle's Meal
    for counter in range(0,4):
        #Sets Colors of Circles Random
        sets = random.choice(colors)
        turtle.pencolor(sets)
        #Creates a Circles
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(sets)
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        #Moves Position Up
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
    #Lets the Turtle eat its Meal
    turtle.penup()
    turtle.goto(-200,-201)
    turtle.pendown()
    for counter in range(0,4):
        #Sets Color to Circles
        turtle.pencolor("white")
        #Creates a Circles
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(11)
        turtle.end_fill()
        turtle.penup()
        #Moves Position Up
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.color("green")
        time.sleep(2)

    turtle.color("green")
    DisplayMessage("Wow! What a great meal!",200)

def Sleep():
    turtle.reset()
    turtle.shape("classic")
    #Location of Cabin to rest
    turtle.penup()
    turtle.goto(200,-200)
    turtle.pendown()
    #Create a Cabin for turtle to sleep
    turtle.pencolor("brown")    
    turtle.begin_fill()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    #Step to get to create a Pillow
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    #Create a Pillow for turtle in the Cabin
    turtle.pencolor("white")    
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.pendown()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.end_fill()
    #Displays Message
    turtle.right(90)
    turtle.forward(20)
    turtle.shape("turtle")
    turtle.color("green")
    DisplayMessage("Good Night!",105)
    turtle.left(90)

def main():
    turtle.setup(800,600)
    Mountains("brown",5)
    time.sleep(7)
    Swim("brown",5)
    time.sleep(7)
    Eat()
    time.sleep(7)
    Sleep()

main()
