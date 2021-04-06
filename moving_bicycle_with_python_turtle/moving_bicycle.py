#moving bicycle
#author: froginafog (Liang D.S.)
import turtle
import time
import math

window = turtle.Screen()
window.bgcolor("bisque")
window.setup(width = 1.0, height = 1.0)

ground = turtle.Turtle()
ground.pensize(5)
ground.color("gray")
ground.speed(10)
r = 100
x_min = -800
x_max = 1200
y_min = 0
y_max = 0
num_points = 2000

#draw the ground
ground.penup()
ground.goto(x_min - 200, y_min - 3)
ground.pendown()
ground.goto(x_max + 200, y_max - 3)
ground.penup()
ground.hideturtle()

#-----------------------------------------------------------------
#draw bicycle

def draw_bicycle():
    pen = turtle.Turtle()
    pen.pensize(3)
    pen.speed(1)
    theta = 0
    
    #draw back wheel
    pen.penup()
    x = x_min
    y = y_min
    pen.goto(x, y)
    pen.pendown()
    pen.color("indigo")
    pen.circle(r)
    pen.penup()
    y = y + r 
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta)
    y = y + r * math.sin(-theta)
    pen.color("red")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta)
    y = y - r * math.sin(-theta)
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta - 2*math.pi/3)
    y = y + r * math.sin(-theta - 2*math.pi/3)
    pen.color("green")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta - 2*math.pi/3)
    y = y - r * math.sin(-theta - 2*math.pi/3)
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta - 4*math.pi/3)
    y = y + r * math.sin(-theta - 4*math.pi/3)
    pen.color("blue")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta - 4*math.pi/3)
    y = y - r * math.sin(-theta - 4*math.pi/3)
    pen.goto(x, y)
    
    #draw front wheel
    pen.penup()
    x = x_min + 6 * r 
    y = y_min
    pen.goto(x, y)
    pen.pendown()
    pen.color("indigo")
    pen.circle(r)
    pen.penup()
    y = y + r 
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta - math.pi/2)
    y = y + r * math.sin(-theta - math.pi/2)
    pen.color("red")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta - math.pi/2)
    y = y - r * math.sin(-theta - math.pi/2)
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta - 7*math.pi/6)
    y = y + r * math.sin(-theta - 7*math.pi/6)
    pen.color("green")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta - 7*math.pi/6)
    y = y - r * math.sin(-theta - 7*math.pi/6)
    pen.goto(x, y)
    pen.pendown()
    x = x + r * math.cos(-theta - 11*math.pi/6)
    y = y + r * math.sin(-theta - 11*math.pi/6)
    pen.color("blue")
    pen.goto(x, y)
    pen.penup()
    x = x - r * math.cos(-theta - 11*math.pi/6)
    y = y - r * math.sin(-theta - 11*math.pi/6)
    pen.goto(x, y)

    #draw segments
    pen.penup()
    x = x_min
    y = y_min + r
    pen.goto(x, y)
    pen.color("maroon")
    pen.pendown()
    x = x + (3/2) * r 
    y = y + (3/2) * r 
    pen.goto(x, y)
    x = x + 3 * r
    pen.goto(x, y)
    x = x_min + 6 * r 
    y = y_min + r
    pen.goto(x, y)
    pen.penup()
    x = x_min
    y = y_min + r
    pen.goto(x, y)
    pen.pendown()
    x = x + (3/2) * r
    pen.goto(x, y)
    y = y + (3/2) * r
    pen.goto(x, y)
    pen.penup()
    y = y - (3/2) * r
    pen.goto(x, y)
    pen.pendown()
    x = x + 3 * r
    y = y + (3/2) * r
    pen.goto(x, y)
    x = x + r/3
    y = y + r
    pen.goto(x, y)
    x = x - r/5
    pen.goto(x, y)
    x = x + 2 * r/5
    pen.goto(x, y)
    x = x - r/5
    pen.goto(x, y)
    x = x - r/3
    y = y - r
    pen.goto(x, y)
    x = x - 3 * r
    pen.goto(x, y)
    y = y + r/2
    pen.goto(x, y)
    x = x - r/5
    pen.goto(x, y)
    x = x + r/5
    pen.goto(x, y)
    x = x + r/2
    pen.goto(x, y)
    pen.penup()
    x = x_min
    y = y_min + r
    pen.goto(x, y)
    x = x + (3/2) * r
    pen.goto(x, y)
    pen.pendown()
    pen.color("purple")
    x = x + r * 1 / 2
    pen.goto(x, y)
    x = x - r * 1 / 2
    pen.goto(x, y)
    pen.color("steelblue")
    x = x - r * 1 / 2
    pen.goto(x, y)
    pen.hideturtle()
    pen.clear()
    
draw_bicycle()
#-----------------------------------------------------------------
#move bicycle
window.tracer(0)

wheel_1 = turtle.Turtle()
wheel_1.color("indigo")
wheel_1.pensize(3)
wheel_1.speed(20)
wheel_1.hideturtle()

wheel_2 = turtle.Turtle()
wheel_2.color("indigo")
wheel_2.pensize(3)
wheel_2.speed(20)
wheel_2.hideturtle()

line_1 = turtle.Turtle() #line of wheel_1
line_1.color("red")
line_1.pensize(3)
line_1.speed(20)
line_1.hideturtle()

line_2 = turtle.Turtle() #line of wheel_1
line_2.color("green")
line_2.pensize(3)
line_2.speed(20)
line_2.hideturtle()

line_3 = turtle.Turtle() #line of wheel_1
line_3.color("blue")
line_3.pensize(3)
line_3.speed(20)
line_3.hideturtle()

line_4 = turtle.Turtle() #line of wheel_2
line_4.color("red")
line_4.pensize(3)
line_4.speed(20)
line_4.hideturtle()

line_5 = turtle.Turtle() #line of wheel_2
line_5.color("green")
line_5.pensize(3)
line_5.speed(20)
line_5.hideturtle()

line_6 = turtle.Turtle() #line of wheel_2
line_6.color("blue")
line_6.pensize(3)
line_6.speed(20)
line_6.hideturtle()

segment_1 = turtle.Turtle() #segment 1 of the bicycle's body
segment_1.color("maroon")
segment_1.pensize(3)
segment_1.speed(20)
segment_1.hideturtle()

segment_2 = turtle.Turtle() #segment 2 of the bicycle's body
segment_2.color("maroon")
segment_2.pensize(3)
segment_2.speed(20)
segment_2.hideturtle()

segment_3 = turtle.Turtle() #segment 3 of the bicycle's body
segment_3.color("maroon")
segment_3.pensize(3)
segment_3.speed(20)
segment_3.hideturtle()

segment_4 = turtle.Turtle() #segment 4 of the bicycle's body
segment_4.color("maroon")
segment_4.pensize(3)
segment_4.speed(20)
segment_4.hideturtle()

segment_5 = turtle.Turtle() #segment 5 of the bicycle's body
segment_5.color("maroon")
segment_5.pensize(3)
segment_5.speed(20)
segment_5.hideturtle()

segment_6 = turtle.Turtle() #segment 6 of the bicycle's body
segment_6.color("maroon")
segment_6.pensize(3)
segment_6.speed(20)
segment_6.hideturtle()

segment_7 = turtle.Turtle() #segment 7 of the bicycle's body
segment_7.color("maroon")
segment_7.pensize(3)
segment_7.speed(20)
segment_7.hideturtle()

segment_8 = turtle.Turtle() #segment 8 of the bicycle's body
segment_8.color("maroon")
segment_8.pensize(3)
segment_8.speed(20)
segment_8.hideturtle()

segment_9 = turtle.Turtle() #segment 9 of the bicycle's body
segment_9.color("maroon")
segment_9.pensize(3)
segment_9.speed(20)
segment_9.hideturtle()

segment_10 = turtle.Turtle() #segment 10 of the bicycle's body
segment_10.color("maroon")
segment_10.pensize(3)
segment_10.speed(20)
segment_10.hideturtle()

segment_11 = turtle.Turtle() #segment 11 of the bicycle's body
segment_11.color("steelblue")
segment_11.pensize(3)
segment_11.speed(20)
segment_11.hideturtle()

segment_12 = turtle.Turtle() #segment 11 of the bicycle's body
segment_12.color("purple")
segment_12.pensize(3)
segment_12.speed(20)
segment_12.hideturtle()

dx_wheel_1 = (x_max - x_min)/num_points
dy_wheel_1 = (y_max - y_min)/num_points
dx_wheel_2 = (x_max - x_min)/num_points
dy_wheel_2 = (y_max - y_min)/num_points

x_data_wheel_1 = []
y_data_wheel_1 = []
x_data_wheel_2 = []
y_data_wheel_2 = []

x_data_wheel_center_1 = []
y_data_wheel_center_1 = []
x_data_wheel_center_2 = []
y_data_wheel_center_2 = []
x_data_line_start_1 = []
y_data_line_start_1 = []
x_data_line_end_1 = []
y_data_line_end_1 = []
x_data_line_start_2 = []
y_data_line_start_2 = []
x_data_line_end_2 = []
y_data_line_end_2 = []
x_data_line_start_3 = []
y_data_line_start_3 = []
x_data_line_end_3 = []
y_data_line_end_3 = []

x_data_line_start_4 = []
y_data_line_start_4 = []
x_data_line_end_4 = []
y_data_line_end_4 = []
x_data_line_start_5 = []
y_data_line_start_5 = []
x_data_line_end_5 = []
y_data_line_end_5 = []
x_data_line_start_6 = []
y_data_line_start_6 = []
x_data_line_end_6 = []
y_data_line_end_6 = []

x_wheel_1 = x_min
y_wheel_1 = y_min

x_wheel_2 = x_min + 6 * r 
y_wheel_2 = y_min

x_wheel_center_1 = x_wheel_1
y_wheel_center_1 = y_wheel_1 + r

x_wheel_center_2 = x_wheel_2
y_wheel_center_2 = y_wheel_2 + r

x_line_start_1 = x_wheel_center_1
y_line_start_1 = y_wheel_center_1
x_line_start_2 = x_wheel_center_1
y_line_start_2 = y_wheel_center_1
x_line_start_3 = x_wheel_center_1
y_line_start_3 = y_wheel_center_1

x_line_start_4 = x_wheel_center_2
y_line_start_4 = y_wheel_center_2
x_line_start_5 = x_wheel_center_2
y_line_start_5 = y_wheel_center_2
x_line_start_6 = x_wheel_center_2
y_line_start_6 = y_wheel_center_2

theta = 0
dtheta = 0.05

x_data_segment_start_1 = []
y_data_segment_start_1 = []
x_data_segment_end_1 = []
y_data_segment_end_1 = []

x_data_segment_start_2 = []
y_data_segment_start_2 = []
x_data_segment_end_2 = []
y_data_segment_end_2 = []

x_data_segment_start_3 = []
y_data_segment_start_3 = []
x_data_segment_end_3 = []
y_data_segment_end_3 = []

x_data_segment_start_4 = []
y_data_segment_start_4 = []
x_data_segment_end_4 = []
y_data_segment_end_4 = []

x_data_segment_start_5 = []
y_data_segment_start_5 = []
x_data_segment_end_5 = []
y_data_segment_end_5 = []

x_data_segment_start_6 = []
y_data_segment_start_6 = []
x_data_segment_end_6 = []
y_data_segment_end_6 = []

x_data_segment_start_7 = []
y_data_segment_start_7 = []
x_data_segment_end_7 = []
y_data_segment_end_7 = []

x_data_segment_start_8 = []
y_data_segment_start_8 = []
x_data_segment_end_8 = []
y_data_segment_end_8 = []

x_data_segment_start_9 = []
y_data_segment_start_9 = []
x_data_segment_end_9 = []
y_data_segment_end_9 = []

x_data_segment_start_10 = []
y_data_segment_start_10 = []
x_data_segment_end_10 = []
y_data_segment_end_10 = []

x_data_segment_start_11 = []
y_data_segment_start_11 = []
x_data_segment_end_11 = []
y_data_segment_end_11 = []

x_data_segment_start_12 = []
y_data_segment_start_12 = []
x_data_segment_end_12 = []
y_data_segment_end_12 = []

for i in range(0, num_points):
    x_data_wheel_1.append(x_wheel_1)
    y_data_wheel_1.append(y_wheel_1)
    x_data_wheel_2.append(x_wheel_2)
    y_data_wheel_2.append(y_wheel_2)
    x_wheel_center_1 = x_wheel_1
    y_wheel_center_1 = y_wheel_1 + r
    x_wheel_center_2 = x_wheel_2
    y_wheel_center_2 = y_wheel_2 + r
    x_data_wheel_center_1.append(x_wheel_center_1)
    y_data_wheel_center_1.append(y_wheel_center_1)
    x_data_wheel_center_2.append(x_wheel_center_2)
    y_data_wheel_center_2.append(y_wheel_center_2)
    
    x_line_start_1 = x_wheel_center_1
    y_line_start_1 = y_wheel_center_1
    x_data_line_start_1.append(x_line_start_1)
    y_data_line_start_1.append(y_line_start_1)
    x_line_end_1 = x_line_start_1 + r * math.cos(-theta)
    y_line_end_1 = y_line_start_1 + r * math.sin(-theta)
    x_data_line_end_1.append(x_line_end_1)
    y_data_line_end_1.append(y_line_end_1)
    x_line_start_2 = x_wheel_center_1
    y_line_start_2 = y_wheel_center_1
    x_data_line_start_2.append(x_line_start_2)
    y_data_line_start_2.append(y_line_start_2)
    x_line_end_2 = x_line_start_2 + r * math.cos(-theta - 2*math.pi/3)
    y_line_end_2 = y_line_start_2 + r * math.sin(-theta - 2*math.pi/3)
    x_data_line_end_2.append(x_line_end_2)
    y_data_line_end_2.append(y_line_end_2)
    x_line_start_3 = x_wheel_center_1
    y_line_start_3 = y_wheel_center_1
    x_data_line_start_3.append(x_line_start_3)
    y_data_line_start_3.append(y_line_start_3)
    x_line_end_3 = x_line_start_3 + r * math.cos(-theta - 4*math.pi/3)
    y_line_end_3 = y_line_start_3 + r * math.sin(-theta - 4*math.pi/3)
    x_data_line_end_3.append(x_line_end_3)
    y_data_line_end_3.append(y_line_end_3)
    x_line_start_4 = x_wheel_center_2
    y_line_start_4 = y_wheel_center_2
    x_data_line_start_4.append(x_line_start_4)
    y_data_line_start_4.append(y_line_start_4)
    x_line_end_4 = x_line_start_4 + r * math.cos(-theta - math.pi/2)
    y_line_end_4 = y_line_start_4 + r * math.sin(-theta - math.pi/2)
    x_data_line_end_4.append(x_line_end_4)
    y_data_line_end_4.append(y_line_end_4)
    x_line_start_5 = x_wheel_center_2
    y_line_start_5 = y_wheel_center_2
    x_data_line_start_5.append(x_line_start_5)
    y_data_line_start_5.append(y_line_start_5)
    x_line_end_5 = x_line_start_5 + r * math.cos(-theta - 7*math.pi/6)
    y_line_end_5 = y_line_start_5 + r * math.sin(-theta - 7*math.pi/6)
    x_data_line_end_5.append(x_line_end_5)
    y_data_line_end_5.append(y_line_end_5)
    x_line_start_6 = x_wheel_center_2
    y_line_start_6 = y_wheel_center_2
    x_data_line_start_6.append(x_line_start_6)
    y_data_line_start_6.append(y_line_start_6)
    x_line_end_6 = x_line_start_6 + r * math.cos(-theta - 11*math.pi/6)
    y_line_end_6 = y_line_start_6 + r * math.sin(-theta - 11*math.pi/6)
    x_data_line_end_6.append(x_line_end_6)
    y_data_line_end_6.append(y_line_end_6)

    x_segment_start_1 = x_wheel_center_1
    y_segment_start_1 = y_wheel_center_1
    x_segment_end_1 = x_wheel_center_1 + (3/2) * r 
    y_segment_end_1 = y_wheel_center_1 + (3/2) * r
    x_data_segment_start_1.append(x_segment_start_1)
    y_data_segment_start_1.append(y_segment_start_1)
    x_data_segment_end_1.append(x_segment_end_1)
    y_data_segment_end_1.append(y_segment_end_1)

    x_segment_start_2 = x_segment_end_1
    y_segment_start_2 = y_segment_end_1
    x_segment_end_2 = x_segment_start_2 + 3 * r
    y_segment_end_2 = y_segment_start_2
    x_data_segment_start_2.append(x_segment_start_2)
    y_data_segment_start_2.append(y_segment_start_2)
    x_data_segment_end_2.append(x_segment_end_2)
    y_data_segment_end_2.append(y_segment_end_2)

    x_segment_start_3 = x_segment_end_2
    y_segment_start_3 = y_segment_end_2
    x_segment_end_3 = x_wheel_center_2
    y_segment_end_3 = y_wheel_center_2
    x_data_segment_start_3.append(x_segment_start_3)
    y_data_segment_start_3.append(y_segment_start_3)
    x_data_segment_end_3.append(x_segment_end_3)
    y_data_segment_end_3.append(y_segment_end_3)

    x_segment_start_4 = x_segment_end_1
    y_segment_start_4 = y_segment_end_1
    x_segment_end_4 = x_segment_start_4
    y_segment_end_4 = y_segment_start_1
    x_data_segment_start_4.append(x_segment_start_4)
    y_data_segment_start_4.append(y_segment_start_4)
    x_data_segment_end_4.append(x_segment_end_4)
    y_data_segment_end_4.append(y_segment_end_4)

    x_segment_start_5 = x_segment_end_4
    y_segment_start_5 = y_segment_end_4
    x_segment_end_5 = x_wheel_center_1
    y_segment_end_5 = y_wheel_center_1
    x_data_segment_start_5.append(x_segment_start_5)
    y_data_segment_start_5.append(y_segment_start_5)
    x_data_segment_end_5.append(x_segment_end_5)
    y_data_segment_end_5.append(y_segment_end_5)

    x_segment_start_6 = x_segment_end_4
    y_segment_start_6 = y_segment_end_4
    x_segment_end_6 = x_segment_end_2
    y_segment_end_6 = y_segment_end_2
    x_data_segment_start_6.append(x_segment_start_6)
    y_data_segment_start_6.append(y_segment_start_6)
    x_data_segment_end_6.append(x_segment_end_6)
    y_data_segment_end_6.append(y_segment_end_6)

    x_segment_start_7 = x_segment_end_2
    y_segment_start_7 = y_segment_end_2
    x_segment_end_7 = x_segment_end_2 + r/3
    y_segment_end_7 = y_segment_end_2 + r
    x_data_segment_start_7.append(x_segment_start_7)
    y_data_segment_start_7.append(y_segment_start_7)
    x_data_segment_end_7.append(x_segment_end_7)
    y_data_segment_end_7.append(y_segment_end_7)

    x_segment_start_8 = x_segment_end_7 - r/5
    y_segment_start_8 = y_segment_end_7
    x_segment_end_8 = x_segment_end_7 + r/5
    y_segment_end_8 = y_segment_end_7
    x_data_segment_start_8.append(x_segment_start_8)
    y_data_segment_start_8.append(y_segment_start_8)
    x_data_segment_end_8.append(x_segment_end_8)
    y_data_segment_end_8.append(y_segment_end_8)

    x_segment_start_9 = x_segment_end_1 
    y_segment_start_9 = y_segment_end_1
    x_segment_end_9 = x_segment_start_9
    y_segment_end_9 = y_segment_start_9 + r/2
    x_data_segment_start_9.append(x_segment_start_9)
    y_data_segment_start_9.append(y_segment_start_9)
    x_data_segment_end_9.append(x_segment_end_9)
    y_data_segment_end_9.append(y_segment_end_9)

    x_segment_start_10 = x_segment_end_9 - r/5
    y_segment_start_10 = y_segment_end_9 
    x_segment_end_10 = x_segment_end_9 + r/2
    y_segment_end_10 = y_segment_end_9
    x_data_segment_start_10.append(x_segment_start_10)
    y_data_segment_start_10.append(y_segment_start_10)
    x_data_segment_end_10.append(x_segment_end_10)
    y_data_segment_end_10.append(y_segment_end_10)

    x_segment_start_11 = x_wheel_center_1 + (3/2) * r 
    y_segment_start_11 = y_wheel_center_1 
    x_segment_end_11 = x_segment_start_11 + r * math.cos(-theta) / 2
    y_segment_end_11 = y_segment_start_11 + r * math.sin(-theta) / 2
    x_data_segment_start_11.append(x_segment_start_11)
    y_data_segment_start_11.append(y_segment_start_11)
    x_data_segment_end_11.append(x_segment_end_11)
    y_data_segment_end_11.append(y_segment_end_11)

    x_segment_start_12 = x_wheel_center_1 + (3/2) * r 
    y_segment_start_12 = y_wheel_center_1 
    x_segment_end_12 = x_segment_start_12 - r * math.cos(-theta) / 2
    y_segment_end_12 = y_segment_start_12 - r * math.sin(-theta) / 2
    x_data_segment_start_12.append(x_segment_start_12)
    y_data_segment_start_12.append(y_segment_start_12)
    x_data_segment_end_12.append(x_segment_end_12)
    y_data_segment_end_12.append(y_segment_end_12)
    
    x_wheel_1 = x_wheel_1 + dx_wheel_1
    y_wheel_1 = y_wheel_1 + dy_wheel_1
    x_wheel_2 = x_wheel_2 + dx_wheel_2
    y_wheel_2 = y_wheel_2 + dy_wheel_2
    theta = theta + dtheta

for i in range(0, num_points):
    wheel_1.penup()
    wheel_1.goto(x_data_wheel_1[i], y_data_wheel_1[i])
    wheel_1.pendown()
    wheel_1.circle(r)
    wheel_2.penup()
    wheel_2.goto(x_data_wheel_2[i], y_data_wheel_2[i])
    wheel_2.pendown()
    wheel_2.circle(r)
    
    line_1.penup()
    line_1.goto(x_data_line_start_1[i], y_data_line_start_1[i])
    line_1.pendown()
    line_1.goto(x_data_line_end_1[i], y_data_line_end_1[i])
    line_2.penup()
    line_2.goto(x_data_line_start_2[i], y_data_line_start_2[i])
    line_2.pendown()
    line_2.goto(x_data_line_end_2[i], y_data_line_end_2[i])
    line_3.penup()
    line_3.goto(x_data_line_start_3[i], y_data_line_start_3[i])
    line_3.pendown()
    line_3.goto(x_data_line_end_3[i], y_data_line_end_3[i])
    line_4.penup()
    line_4.goto(x_data_line_start_4[i], y_data_line_start_4[i])
    line_4.pendown()
    line_4.goto(x_data_line_end_4[i], y_data_line_end_4[i])
    line_5.penup()
    line_5.goto(x_data_line_start_5[i], y_data_line_start_5[i])
    line_5.pendown()
    line_5.goto(x_data_line_end_5[i], y_data_line_end_5[i])
    line_6.penup()
    line_6.goto(x_data_line_start_6[i], y_data_line_start_6[i])
    line_6.pendown()
    line_6.goto(x_data_line_end_6[i], y_data_line_end_6[i])

    segment_1.penup()
    segment_1.goto(x_data_segment_start_1[i], y_data_segment_start_1[i])
    segment_1.pendown()
    segment_1.goto(x_data_segment_end_1[i], y_data_segment_end_1[i])

    segment_2.penup()
    segment_2.goto(x_data_segment_start_2[i], y_data_segment_start_2[i])
    segment_2.pendown()
    segment_2.goto(x_data_segment_end_2[i], y_data_segment_end_2[i])

    segment_3.penup()
    segment_3.goto(x_data_segment_start_3[i], y_data_segment_start_3[i])
    segment_3.pendown()
    segment_3.goto(x_data_segment_end_3[i], y_data_segment_end_3[i])

    segment_4.penup()
    segment_4.goto(x_data_segment_start_4[i], y_data_segment_start_4[i])
    segment_4.pendown()
    segment_4.goto(x_data_segment_end_4[i], y_data_segment_end_4[i])

    segment_5.penup()
    segment_5.goto(x_data_segment_start_5[i], y_data_segment_start_5[i])
    segment_5.pendown()
    segment_5.goto(x_data_segment_end_5[i], y_data_segment_end_5[i])

    segment_6.penup()
    segment_6.goto(x_data_segment_start_6[i], y_data_segment_start_6[i])
    segment_6.pendown()
    segment_6.goto(x_data_segment_end_6[i], y_data_segment_end_6[i])

    segment_7.penup()
    segment_7.goto(x_data_segment_start_7[i], y_data_segment_start_7[i])
    segment_7.pendown()
    segment_7.goto(x_data_segment_end_7[i], y_data_segment_end_7[i])

    segment_8.penup()
    segment_8.goto(x_data_segment_start_8[i], y_data_segment_start_8[i])
    segment_8.pendown()
    segment_8.goto(x_data_segment_end_8[i], y_data_segment_end_8[i])

    segment_9.penup()
    segment_9.goto(x_data_segment_start_9[i], y_data_segment_start_9[i])
    segment_9.pendown()
    segment_9.goto(x_data_segment_end_9[i], y_data_segment_end_9[i])

    segment_10.penup()
    segment_10.goto(x_data_segment_start_10[i], y_data_segment_start_10[i])
    segment_10.pendown()
    segment_10.goto(x_data_segment_end_10[i], y_data_segment_end_10[i])

    segment_11.penup()
    segment_11.goto(x_data_segment_start_11[i], y_data_segment_start_11[i])
    segment_11.pendown()
    segment_11.goto(x_data_segment_end_11[i], y_data_segment_end_11[i])

    segment_12.penup()
    segment_12.goto(x_data_segment_start_12[i], y_data_segment_start_12[i])
    segment_12.pendown()
    segment_12.goto(x_data_segment_end_12[i], y_data_segment_end_12[i])
    
    window.update() 
    time.sleep(0.01)
    wheel_1.undo()
    wheel_2.undo()
    line_1.undo()
    line_2.undo()
    line_3.undo()
    line_4.undo()
    line_5.undo()
    line_6.undo()
    
    segment_1.undo()
    segment_2.undo()
    segment_3.undo()
    segment_4.undo()
    segment_5.undo()
    segment_6.undo()
    segment_7.undo()
    segment_8.undo()
    segment_9.undo()
    segment_10.undo()
    segment_11.undo()
    segment_12.undo()

#----------------------------------------------------------------

window.mainloop() 
