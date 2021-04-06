#author: froginafog (Liang D.S.)

#'Up' arrow to move the circle upward
#'Down' arrow to move the circle downward
#'Left' arrow to move the circle to the left
#'Right' arrow to move the circle to the right

#'w' to move the sqaure upward
#'s' to move the square downward
#'a' to move the square to the left
#'d' to move the square to the right

#'l' to draw a diagonal from the origin to the circle
#'k' to draw a diagonal from the origin to the square
#'p' to draw a diagonal from the square to the circle

#click on a point to stamp the coordinates on that point

import turtle
import math

#----------------------------------
def draw_line(pen, x_start, y_start, x_end, y_end):
    pen.penup()
    pen.goto(x_start, y_start)
    pen.pendown()
    pen.goto(x_end, y_end)
    pen.penup()
#----------------------------------
def circle_move_up():
    global y_circle
    global y_max
    global dy
    if(y_circle <= y_max - dy):
        y_circle = y_circle + dy
#----------------------------------
def circle_move_down():
    global y_circle
    global y_min
    global dy
    if(y_circle >= y_min + dy):
        y_circle = y_circle - dy
#----------------------------------
def circle_move_left():
    global x_circle
    global x_min
    global dx 
    if(x_circle >= x_min + dx):
        x_circle = x_circle - dx
#----------------------------------
def circle_move_right():
    global x_circle
    global x_max
    global dx
    if(x_circle <= x_max - dx):
        x_circle = x_circle + dx
#----------------------------------
def draw_line_from_origin_to_circle():
    global x_circle
    global y_circle
    line.color("lightgreen")
    line.penup()
    line.goto(0, 0)
    line.pendown()
    line.goto(x_circle, y_circle)
    line.penup()
#----------------------------------
def square_move_up():
    global y_square
    global y_max
    global dy
    if(y_square <= y_max - dy):
        y_square = y_square + dy
#----------------------------------
def square_move_down():
    global y_square
    global y_min
    global dy
    if(y_square >= y_min + dy):
        y_square = y_square - dy
#----------------------------------
def square_move_left():
    global x_square
    global x_min
    global dx 
    if(x_square >= x_min + dx):
        x_square = x_square - dx
#----------------------------------
def square_move_right():
    global x_square
    global x_max
    global dx
    if(x_square <= x_max - dx):
        x_square = x_square + dx
#----------------------------------
def draw_line_from_origin_to_square():
    global x_square
    global y_square
    line.color("yellow")
    line.penup()
    line.goto(0, 0)
    line.pendown()
    line.goto(x_square, y_square)
    line.penup()
#----------------------------------
def draw_line_from_circle_to_square():
    global x_circle
    global y_circle
    global x_square
    global y_square
    line.color("purple")
    line.penup()
    line.goto(x_circle, y_circle)
    line.pendown()
    line.goto(x_square, y_square)
    line.penup()
#----------------------------------
def f(x, y):
    text.goto(x, y)
    text.write("(" + str(x) + "," + str(y) + ")", move = False, align = 'center', font = ('arial', 28, 'normal'))
#----------------------------------

window = turtle.Screen()  
window.bgcolor("midnightblue")  
window.setup(width = 1.0, height = 1.0)

#set the keys
turtle.listen()
turtle.onkey(circle_move_up, "Up") #move the circle upward
turtle.onkey(circle_move_down, "Down") #move the circle downward
turtle.onkey(circle_move_left, "Left") #move the circle to the left
turtle.onkey(circle_move_right, "Right") #move the circle to the right
turtle.onkey(draw_line_from_origin_to_circle, "l") #press 'l' to draw a line from the origin to the circle

turtle.onkey(square_move_up, "w") #move the square upward
turtle.onkey(square_move_down, "s") #move the square downward
turtle.onkey(square_move_left, "a") #move the square to the left
turtle.onkey(square_move_right, "d") #move the square to the right
turtle.onkey(draw_line_from_origin_to_square, "k") #press 'k' to draw a line from the origin to the square

turtle.onkey(draw_line_from_circle_to_square, "p") #press 'p' to draw a line from the origin to the square

window.onclick(f)

x_min = -800
x_max = 800
y_min = -500
y_max = 500
dx = 100
dy = 100

#grid
grid = turtle.Turtle()
grid.color("silver")
grid.speed(0)
grid.pensize(5)
draw_line(grid, x_min, 0, x_max, 0)
draw_line(grid, 0, y_min, 0, y_max)
grid.pensize(1)
grid.hideturtle()

y = y_min
while(y <= y_max):
    draw_line(grid, x_min, y, x_max, y)
    y = y + dy
    
x = x_min
while(x <= x_max):
    draw_line(grid, x, y_min, x, y_max)
    x = x + dx

#circle
circle = turtle.Turtle()
circle.color("lightgreen")
circle.shape("circle")
circle.shapesize(1)
circle.pensize(5)
#circle.penup()
circle.speed(0)
x_circle = 0
y_circle = 0
circle.goto(x_circle, y_circle)
x_circle_previous = x_circle
y_circle_previous = y_circle

#square
square = turtle.Turtle()
square.color("yellow")
square.shape("square")
square.shapesize(1)
square.pensize(5)
#square.penup()
square.speed(0)
x_square = 0
y_square = 0
square.goto(x_square, y_square)
x_square_previous = x_square
y_square_previous = y_square

#line
line = turtle.Turtle()
line.color("yellow")
line.pensize(5)
line.speed(0)
line.hideturtle()
line.penup()

#text
text = turtle.Turtle()
text.color("red")
text.pensize(5)
text.speed(0)
text.hideturtle()
text.penup()

while(True):
    circle.goto(x_circle, y_circle)
    square.goto(x_square, y_square)
    
print("END")
