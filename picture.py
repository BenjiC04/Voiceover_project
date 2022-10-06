#   Add your code here and add comments to your code 
#   to describe what each section of code is doing
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

#face
painter.fillcolor("tan")
painter.begin_fill()
painter.circle(50)
painter.end_fill()
painter.penup()
painter.forward(25)
painter.left(90)
painter.forward(50)

#eye
painter.pendown()
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(7)
painter.end_fill()
painter.penup()

#eye 2
painter.left(90)
painter.forward(40)
painter.right(90)
painter.forward(2)
painter.pendown()
painter.begin_fill()
painter.circle(7)
painter.end_fill()
painter.penup()

#smile
painter.goto(0, 0)
painter.forward(30)
painter.left(90)
painter.forward(20)
painter.right(275)
painter.pendown()
painter.circle(20, 180)
painter.penup()

#body
painter.goto(0, -3)
painter.pensize(10)
painter.pendown()
painter.right(175)
painter.forward(140)
painter.left(45)
painter.forward(90)
painter.left(180)
painter.forward(90)
painter.left(90)
painter.forward(90)
painter.penup()
painter.right(180)
painter.forward(90)
painter.left(45)
painter.forward(70)
painter.left(90)
painter.pendown()
painter.forward(50)
painter.left(180)
painter.forward(100)
painter.penup()

#ground
painter.goto(63.65, -206.65)
painter.pendown()
painter.pencolor("green")
painter.forward(500)
painter.right(180)
painter.forward(1000)

#now that the program is done, try to add inputs to decide eye color
#arm, and foot length




wn = trtl.Screen()
wn.bgcolor("cyan")
wn.mainloop()
