#author: froginafog (Liang D.S.)
import turtle
import math
import time

#--------------------------------------------------------------
def draw_circle(pen, x_center, y_center, r): #r is the radius
    theta = 0
    dtheta = 0.8/r
    pen.penup()
    x = x_center
    y = y_center
    pen.goto(x, y)
    x = x + r
    pen.goto(x, y)
    pen.pendown()
    while(theta <= 2 * math.pi):
        x = x_center + r * math.cos(-theta)
        y = y_center + r * math.sin(-theta)
        pen.goto(x, y)
        theta = theta + dtheta
    pen.penup()
    x = x_center
    y = y_center
    pen.goto(x, y)
#--------------------------------------------------------------
window = turtle.Screen()  #create the window
window.bgcolor("midnightblue")  #set the window's color
window.tracer(0) #so that there is no tracing (the object appear instantaneously)
window.setup(width = 1.0, height = 1.0)

pen_line_1 = turtle.Turtle()
pen_line_1.color("gold")
pen_line_1.pensize(3)
pen_line_1.hideturtle()
pen_line_1.penup()

pen_line_2 = turtle.Turtle()
pen_line_2.color("mediumseagreen")
pen_line_2.pensize(3)
pen_line_2.hideturtle()
pen_line_2.penup()

pen_line_3 = turtle.Turtle()
pen_line_3.color("red")
pen_line_3.pensize(3)
pen_line_3.hideturtle()
pen_line_3.penup()

pen_line_4 = turtle.Turtle()
pen_line_4.color("mediumorchid")
pen_line_4.pensize(3)
pen_line_4.hideturtle()
pen_line_4.penup()

x_min = -500
y_min = 0
x_max = 500
y_max = 0

pen_1 = turtle.Turtle()  #create the pen at the center of the screen
pen_1.color("gold")
pen_1.pensize(2)
pen_1.hideturtle()
x_circle_1 = x_min
y_circle_1 = y_min
r_circle_1 = 20
dx_circle_1 = 3
dy_circle_1 = 0

d_1_2 = 12 * r_circle_1 #distance between the center of circle_1 and the center of circle_2
r_circle_2 = 0.8 * r_circle_1
pen_2 = turtle.Turtle()  #create the pen at the center of the screen
pen_2.color("mediumseagreen")
pen_2.pensize(2)
pen_2.hideturtle()

d_2_3 = 8 * r_circle_2 
r_circle_3 = 0.8 * r_circle_2
pen_3 = turtle.Turtle()  
pen_3.color("red")
pen_3.pensize(2)
pen_3.hideturtle()

d_3_4 = 4 * r_circle_3
r_circle_4 = 0.8 * r_circle_3
pen_4 = turtle.Turtle()  
pen_4.color("mediumorchid")
pen_4.pensize(2)
pen_4.hideturtle()

theta = 0
dtheta = math.pi/200

cycle = 1
freq = 1

x_line_1 = r_circle_1 * 10
y_line_1 = 0
pen_line_1.goto(x_line_1, y_line_1)
pen_line_1.pendown()

x_line_2 = x_line_1 + d_1_2
y_line_2 = 0
pen_line_2.goto(x_line_2, y_line_2)
pen_line_2.pendown()

x_line_3 = x_line_1 + d_1_2 + d_2_3 
y_line_3 = 0
pen_line_3.goto(x_line_3, y_line_3)
pen_line_3.pendown()

x_line_4 = x_line_1 + d_1_2 + d_2_3 + d_3_4
y_line_4 = 0
pen_line_4.goto(x_line_4, y_line_4)
pen_line_4.pendown()

while(True):
    x_circle_1 = r_circle_1 * math.cos(2*theta) * 10
    y_circle_1 = r_circle_1 * math.sin(2*theta) * math.cos(2*theta) * 10
    pen_1.begin_fill()
    draw_circle(pen_1, x_circle_1 , y_circle_1 , r_circle_1)
    pen_1.end_fill()

    x_line_1 = x_circle_1
    y_line_1 = y_circle_1
    pen_line_1.goto(x_line_1, y_line_1)
    
    x_circle_2 = x_circle_1 + d_1_2 * math.cos(-2*freq*theta)
    y_circle_2 = y_circle_1 + d_1_2 * math.sin(-2*freq*theta)
    pen_2.begin_fill()
    draw_circle(pen_2, x_circle_2 , y_circle_2 , r_circle_2)
    pen_2.end_fill()
    
    x_circle_3 = x_circle_2 + d_2_3 * math.cos(-4*freq*theta)
    y_circle_3 = y_circle_2 + d_2_3 * math.sin(-4*freq*theta)
    pen_3.begin_fill()
    draw_circle(pen_3, x_circle_3 , y_circle_3 , r_circle_3)
    pen_3.end_fill()

    x_circle_4 = x_circle_3 + d_3_4 * math.cos(-6*freq*theta)
    y_circle_4 = y_circle_3 + d_3_4 * math.sin(-6*freq*theta)
    pen_4.begin_fill()
    draw_circle(pen_4, x_circle_4 , y_circle_4 , r_circle_4)
    pen_4.end_fill()

    x_line_2 = x_circle_2
    y_line_2 = y_circle_2
    pen_line_2.goto(x_line_2, y_line_2)

    x_line_3 = x_circle_3
    y_line_3 = y_circle_3
    pen_line_3.goto(x_line_3, y_line_3)

    x_line_4 = x_circle_4
    y_line_4 = y_circle_4
    pen_line_4.goto(x_line_4, y_line_4)
    
    theta = theta + dtheta
    window.update() 
    time.sleep(0.01)
    pen_1.clear()
    pen_2.clear()
    pen_3.clear()
    pen_4.clear()

    if(cycle*math.pi - dtheta/2 <= theta and theta <= cycle*math.pi + dtheta/2):
        if(cycle % 2 == 0):
            pen_line_1.color("gold")
            pen_line_2.color("mediumseagreen")
            pen_line_3.color("red")
            pen_line_4.color("mediumorchid")
            freq = freq + 1
            window = turtle.Screen()
            window.bgcolor("midnightblue") 
            window.tracer(0) 
            window.setup(width = 1.0, height = 1.0)
        else:
            pen_line_1.color("midnightblue")
            pen_line_2.color("midnightblue")
            pen_line_3.color("midnightblue")
            pen_line_4.color("midnightblue")
        cycle = cycle + 1








