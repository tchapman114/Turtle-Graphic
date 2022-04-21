import turtle
import time

#TARA CHAPMAN
#Use of a list
#Single loop
#Turtle will eat apples off a tree and climb back down to display a message to the user
def EatApples():
    reset()
    #declare variables
    colors = ["red", "darkgreen", "yellow"]
    pensize = int()
    radius = int()
    radius = 10
    pen_size = 3
    #drawing tree
    #trunk of the tree, rectangle
    turtle.goto(0,-200)
    turtle.pencolor("brown")
    turtle.fillcolor("brown")
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    #top of the tree, triangle
    turtle.penup()
    turtle.goto(25,235)
    turtle.pencolor("green3")
    turtle.fillcolor("green3")
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(35)
    turtle.forward(270)
    turtle.right(144)
    turtle.forward(410)
    turtle.right(140)
    turtle.forward(250)
    turtle.end_fill()
    #Hole in the middle of the tree, circle
    turtle.penup()
    turtle.goto(40,-65)
    turtle.pencolor("black")
    turtle.fillcolor("black")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(23)
    turtle.end_fill()
    #drawing the apples, using a list and a single loop
    turtle.penup()
    x = 20
    y = 150
    turtle.goto(x,y)
    turtle.pendown()
    for count in range (0,3):
        turtle.fillcolor(colors[count])
        turtle.pencolor(colors[count])
        turtle.begin_fill()
        turtle.circle(radius)
        x = x + 20
        y = y - 30
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.end_fill()
        #end for

    #loop to eat the apples
    turtle.penup()
    x = 20
    y = 150
    turtle.goto(x,y)
    turtle.pendown()
    turtle.shape("turtle")
    for count in range(0,3):
        turtle.fillcolor("green3")
        turtle.pencolor("green3")
        turtle.begin_fill()
        turtle.circle(radius)
        x = x + 20
        y = y - 30
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.end_fill()
        turtle.pencolor("green")
        turtle.fillcolor("green")
        import time
        time.sleep(1)
        #end loop
        
    #turtle climbs down tree and output on screen
    turtle.penup()
    turtle.goto(25,25)
    turtle.right(133)
    turtle.forward(220)
    turtle.right(90)
    turtle.forward(80)
    #message to user
    turtle.pencolor("black")
    turtle.write("Yum! I love apples!",align='right', font=('Arial' , '12', 'bold'))

#CLAIRE MCCOWAN

#turtle will climb up a pyramid
#needs to have an if function
#needs to have an input statement

#declare variables
pensize=int()
pencolor=int()
def TurtleClimb():
    reset()
    #drawing the pyramid
    turtle.setup(600,800)
    turtle.penup()
    turtle.goto(100,-100)
    turtle.pendown()
    turtle.pensize(6)
    #determine pencolor
    if pencolor == "Saddle brown":
        turtle.pencolor("saddle brown")
    elif pencolor == "tan1":
        turtle.pencolor("tan1")
    else:
        turtle.pencolor("blanched almond")
    #ask user for fillcolor
    #colors could be: brown, black, blue, pink, yellow, orange
    fillcolor = input("What color should the fillcolor be? ")
    #drawing the pyramid
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.forward(145)
    turtle.left(127)
    turtle.forward(200)
    turtle.right(228)
    turtle.forward(165)
    #stopping the fill
    turtle.end_fill()
    #turtle climbing
    turtle.penup()
    turtle.goto(-65,-70)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.left(98)
    turtle.forward(40)
    turtle.left(98)
    turtle.forward(40)
    turtle.right(98)
    turtle.forward(40)
    turtle.left(98)
    turtle.forward(40)
    turtle.right(98)
    turtle.forward(40)
    turtle.left(98)
    turtle.forward(40)
    turtle.right(98)
    turtle.forward(40)
    turtle.left(98)
    turtle.forward(28)
    turtle.right(98)
    turtle.forward(28)
    turtle.pencolor("green")
    turtle.fillcolor("green")
    turtle.write("Hurray! Made it to the top!", align="right", font=('Arial', '16', 'bold'))

    
#reset to each partners work
def reset():
    time.sleep(5)
    turtle.reset()
    turtle.setup(600,600)
    turtle.penup()
    turtle.shape("classic")


#main function
def main():
    EatApples()
    TurtleClimb()
    reset()

    
main()
