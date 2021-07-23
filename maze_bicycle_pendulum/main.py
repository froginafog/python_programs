#author: froginafog (Liang D.S.)
import turtle
import time
import math

background_blue = 230

window = turtle.Screen()
turtle.colormode(255)
window.bgcolor(0, 0, background_blue)
window.setup(width = 1.0, height = 1.0)

r_bicycle = 100
x_min_bicycle = -800
x_max_bicycle = 1200
y_min_bicycle = -200
y_max_bicycle = y_min_bicycle
num_points_bicycle = 2000

time.sleep(3)

#-----------------------------------------------------------------
#draw the ground

ground = turtle.Turtle()
ground.pensize(1)
ground.color("silver")
ground.speed(5)

ground.penup()
ground.goto(x_min_bicycle - 200, y_min_bicycle - 3)
ground.pendown()
ground.goto(x_max_bicycle + 200, y_max_bicycle - 3)
ground.penup()
ground.hideturtle()

#-----------------------------------------------------------------
#draw maze
import random
from datetime import datetime

random.seed(datetime.now())

def get_random_rgb():  #get random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_maze():
    pen1 = turtle.Turtle() 
    pen1.pensize(5)
    pen1.penup()               
    pen1.goto(-900, y_min_bicycle)
    pen1.pendown()
    pen1.speed(10)

    pen2 = turtle.Turtle()  
    pen2.pensize(5)
    pen2.penup()               
    pen2.goto(900, y_min_bicycle)
    pen2.pendown()
    pen2.speed(10)

    s = 200 #maze segment length
    ds = 10
    angle_maze = 90

    background_blue = 230
    num_maze_iterations = 0
    while(num_maze_iterations < 4):
        while(s > 0):
            red, green, blue = get_random_rgb()
            pen1.pencolor(red, green, blue)
            pen1.forward(s)
            pen1.right(angle_maze)
            red, green, blue = get_random_rgb()
            pen2.pencolor(red, green, blue)
            pen2.backward(s)
            pen2.left(angle_maze)
            s = s - ds
            background_blue = background_blue - 1
            window.bgcolor(0, 0, background_blue)
        pen1.left(angle_maze)
        pen2.right(angle_maze)
        s = s + ds
        while(s < 200):
            red, green, blue = get_random_rgb()
            pen1.pencolor(red, green, blue)
            pen1.backward(s)
            pen1.left(angle_maze)
            red, green, blue = get_random_rgb()
            pen2.pencolor(red, green, blue)
            pen2.forward(s)
            pen2.right(angle_maze)
            s = s + 10
            background_blue = background_blue - 1
            window.bgcolor(0, 0, background_blue)
        num_maze_iterations = num_maze_iterations + 1
        
    num_concentric_squares = 0
    ds = 15
    while(num_concentric_squares < 6):
        num_maze_iterations = 0
        while(num_maze_iterations < 4):
            red, green, blue = get_random_rgb()
            pen1.pencolor(red, green, blue)
            pen1.forward(s)
            pen1.right(angle_maze)
            num_maze_iterations = num_maze_iterations + 1
        num_maze_iterations = 0
        num_concentric_squares = num_concentric_squares + 1
        pen1.penup()               
        pen1.forward(ds)
        pen1.right(angle_maze)
        pen1.forward(ds)
        pen1.left(angle_maze)
        pen1.pendown()
        s = s - 2 * ds
        background_blue = background_blue - 1
        window.bgcolor(0, 0, background_blue)
    pen1.hideturtle()
    pen2.hideturtle()

draw_maze()

#-----------------------------------------------------------------
#draw bicycle
pen_bicycle = turtle.Turtle()
pen_bicycle.pensize(5)
pen_bicycle.speed(1)
theta_bicycle = 0

def draw_bicycle():
    #draw back wheel
    pen_bicycle.penup()
    x_bicycle = x_min_bicycle
    y_bicycle = y_min_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    pen_bicycle.color("silver")
    pen_bicycle.circle(r_bicycle)
    pen_bicycle.penup()
    y_bicycle = y_bicycle + r_bicycle 
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle)
    pen_bicycle.color("red")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle)
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle - 2*math.pi/3)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle - 2*math.pi/3)
    pen_bicycle.color("green")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle - 2*math.pi/3)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle - 2*math.pi/3)
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle - 4*math.pi/3)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle - 4*math.pi/3)
    pen_bicycle.color("gold")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle - 4*math.pi/3)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle - 4*math.pi/3)
    pen_bicycle.goto(x_bicycle, y_bicycle)
    
    #draw front wheel
    pen_bicycle.penup()
    x_bicycle = x_min_bicycle + 6 * r_bicycle
    y_bicycle = y_min_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    pen_bicycle.color("silver")
    pen_bicycle.circle(r_bicycle)
    pen_bicycle.penup()
    y_bicycle = y_bicycle + r_bicycle 
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle - math.pi/2)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle - math.pi/2)
    pen_bicycle.color("red")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle - math.pi/2)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle - math.pi/2)
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle - 7*math.pi/6)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle - 7*math.pi/6)
    pen_bicycle.color("green")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle - 7*math.pi/6)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle - 7*math.pi/6)
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + r_bicycle * math.cos(-theta_bicycle - 11*math.pi/6)
    y_bicycle = y_bicycle + r_bicycle * math.sin(-theta_bicycle - 11*math.pi/6)
    pen_bicycle.color("gold")
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_bicycle - r_bicycle * math.cos(-theta_bicycle - 11*math.pi/6)
    y_bicycle = y_bicycle - r_bicycle * math.sin(-theta_bicycle - 11*math.pi/6)
    pen_bicycle.goto(x_bicycle, y_bicycle)

    #draw segments
    pen_bicycle.penup()
    x_bicycle = x_min_bicycle
    y_bicycle = y_min_bicycle + r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.color("steelblue")
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + 1.5 * r_bicycle 
    y_bicycle = y_bicycle + 1.5 * r_bicycle 
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + 3 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_min_bicycle + 6 * r_bicycle 
    y_bicycle = y_min_bicycle + r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_min_bicycle
    y_bicycle = y_min_bicycle + r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + 1.5 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    y_bicycle = y_bicycle + 1.5 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    y_bicycle = y_bicycle - 1.5 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    x_bicycle = x_bicycle + 3 * r_bicycle
    y_bicycle = y_bicycle + 1.5 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + r_bicycle/3
    y_bicycle = y_bicycle + r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - r_bicycle/5
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + 2 * r_bicycle/5
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - r_bicycle/5
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - r_bicycle/3
    y_bicycle = y_bicycle - r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - 3 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    y_bicycle = y_bicycle + r_bicycle/2
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - r_bicycle/5
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + r_bicycle/5
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + r_bicycle/2
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.penup()
    x_bicycle = x_min_bicycle
    y_bicycle = y_min_bicycle + r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle + 1.5 * r_bicycle
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.pendown()
    pen_bicycle.color("lightgreen")
    x_bicycle = x_bicycle + r_bicycle/2
    pen_bicycle.goto(x_bicycle, y_bicycle)
    x_bicycle = x_bicycle - r_bicycle/2
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.color("purple")
    x_bicycle = x_bicycle - r_bicycle/2
    pen_bicycle.goto(x_bicycle, y_bicycle)
    pen_bicycle.hideturtle()
    
draw_bicycle()

#-----------------------------------------------------------------
#draw pendulum
def draw_circle(pen, x_center, y_center, r): #r is the radius
    theta = 0
    dtheta = 0.2/r
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
    
def draw_line(pen, x_start, y_start, x_end, y_end):
    pen.penup()
    pen.goto(x_start, y_start)
    pen.pendown()
    pen.goto(x_end, y_end)
    pen.penup()

def theta_pendulum(t, theta_0, w): #theta_0 is the initial angle, w is the angular frequency, w = sqrt(g/L)
    return theta_0 * math.cos(w * t)

pen_pendulum = turtle.Turtle()  
pen_pendulum.color("silver")
pen_pendulum.pensize(2)
pen_pendulum.speed(5)
pen_pendulum.hideturtle()

pen_pendulum_line = turtle.Turtle()  
pen_pendulum_line.color("silver")
pen_pendulum_line.pensize(2)
pen_pendulum_line.speed(2)
pen_pendulum_line.hideturtle()

pen_pendulum_circle = turtle.Turtle() 
pen_pendulum_circle.color("lightgreen")
pen_pendulum_circle.pensize(2)
pen_pendulum_circle.speed(0)
pen_pendulum_circle.hideturtle()

dx_pendulum = 20
dy_pendulum = 10
x_pendulum_line = -200
y_pendulum_line = 450

while(x_pendulum_line < -200 + 400 - dx_pendulum):
    draw_line(pen_pendulum, x_pendulum_line, y_pendulum_line + 2 * dy_pendulum, x_pendulum_line + dx_pendulum, y_pendulum_line)
    x_pendulum_line = x_pendulum_line + dx_pendulum

g = 9.8 #gravitational constant
L = 100 #length of the cord
w = math.sqrt(g/L) #frequency
r_pendulum = 20
t = 0
dt = 0.35
theta_pendulum_0 = 20 * math.pi/180 #initial angle of 20 degrees converted into radians

draw_line(pen_pendulum, x_pendulum_line - 400, y_pendulum_line, x_pendulum_line + 33, y_pendulum_line)
draw_line(pen_pendulum_line, 0, y_pendulum_line, -L * math.sin(theta_pendulum(t, theta_pendulum_0, w)),
          y_pendulum_line - L * math.cos(theta_pendulum(t, theta_pendulum_0, w)))
draw_circle(pen_pendulum_circle, -L * math.sin(theta_pendulum(t, theta_pendulum_0, w)),
            y_pendulum_line - L * math.cos(theta_pendulum(t, theta_pendulum_0, w)), r_pendulum)

angle_pendulum_data = []
x_pendulum_circle_data = []
y_pendulum_circle_data = []
num_points_pendulum = num_points_bicycle 

for i in range(0, num_points_pendulum):
    angle_pendulum = theta_pendulum(t, theta_pendulum_0, w)
    x_pendulum_circle_data.append(-L * math.sin(angle_pendulum))
    y_pendulum_circle_data.append(y_pendulum_line - L * math.cos(angle_pendulum))
    t = t + dt
    L = L + 0.2

#-----------------------------------------------------------------
#move bicycle
pen_bicycle.clear()
window.tracer(0)

wheel_1 = turtle.Turtle()
wheel_1.color("silver")
wheel_1.pensize(5)
wheel_1.speed(20)
wheel_1.hideturtle()

wheel_2 = turtle.Turtle()
wheel_2.color("silver")
wheel_2.pensize(5)
wheel_2.speed(20)
wheel_2.hideturtle()

line_1 = turtle.Turtle() #line of wheel_1
line_1.color("red")
line_1.pensize(5)
line_1.speed(20)
line_1.hideturtle()

line_2 = turtle.Turtle() #line of wheel_1
line_2.color("green")
line_2.pensize(5)
line_2.speed(20)
line_2.hideturtle()

line_3 = turtle.Turtle() #line of wheel_1
line_3.color("gold")
line_3.pensize(5)
line_3.speed(20)
line_3.hideturtle()

line_4 = turtle.Turtle() #line of wheel_2
line_4.color("red")
line_4.pensize(5)
line_4.speed(20)
line_4.hideturtle()

line_5 = turtle.Turtle() #line of wheel_2
line_5.color("green")
line_5.pensize(5)
line_5.speed(20)
line_5.hideturtle()

line_6 = turtle.Turtle() #line of wheel_2
line_6.color("gold")
line_6.pensize(5)
line_6.speed(20)
line_6.hideturtle()

segment_1 = turtle.Turtle() #segment 1 of the bicycle's body
segment_1.color("steelblue")
segment_1.pensize(5)
segment_1.speed(20)
segment_1.hideturtle()

segment_2 = turtle.Turtle() #segment 2 of the bicycle's body
segment_2.color("steelblue")
segment_2.pensize(5)
segment_2.speed(20)
segment_2.hideturtle()

segment_3 = turtle.Turtle() #segment 3 of the bicycle's body
segment_3.color("steelblue")
segment_3.pensize(5)
segment_3.speed(20)
segment_3.hideturtle()

segment_4 = turtle.Turtle() #segment 4 of the bicycle's body
segment_4.color("steelblue")
segment_4.pensize(5)
segment_4.speed(20)
segment_4.hideturtle()

segment_5 = turtle.Turtle() #segment 5 of the bicycle's body
segment_5.color("steelblue")
segment_5.pensize(5)
segment_5.speed(20)
segment_5.hideturtle()

segment_6 = turtle.Turtle() #segment 6 of the bicycle's body
segment_6.color("steelblue")
segment_6.pensize(5)
segment_6.speed(20)
segment_6.hideturtle()

segment_7 = turtle.Turtle() #segment 7 of the bicycle's body
segment_7.color("steelblue")
segment_7.pensize(5)
segment_7.speed(20)
segment_7.hideturtle()

segment_8 = turtle.Turtle() #segment 8 of the bicycle's body
segment_8.color("steelblue")
segment_8.pensize(5)
segment_8.speed(20)
segment_8.hideturtle()

segment_9 = turtle.Turtle() #segment 9 of the bicycle's body
segment_9.color("steelblue")
segment_9.pensize(5)
segment_9.speed(20)
segment_9.hideturtle()

segment_10 = turtle.Turtle() #segment 10 of the bicycle's body
segment_10.color("steelblue")
segment_10.pensize(5)
segment_10.speed(20)
segment_10.hideturtle()

segment_11 = turtle.Turtle() #segment 11 of the bicycle's body
segment_11.color("purple")
segment_11.pensize(5)
segment_11.speed(20)
segment_11.hideturtle()

segment_12 = turtle.Turtle() #segment 11 of the bicycle's body
segment_12.color("lightgreen")
segment_12.pensize(5)
segment_12.speed(20)
segment_12.hideturtle()

dx_wheel_1 = (x_max_bicycle - x_min_bicycle)/num_points_bicycle
dy_wheel_1 = (y_max_bicycle - y_min_bicycle)/num_points_bicycle
dx_wheel_2 = (x_max_bicycle - x_min_bicycle)/num_points_bicycle
dy_wheel_2 = (y_max_bicycle - y_min_bicycle)/num_points_bicycle

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

x_wheel_1 = x_min_bicycle
y_wheel_1 = y_min_bicycle

x_wheel_2 = x_min_bicycle + 6 * r_bicycle 
y_wheel_2 = y_min_bicycle

x_wheel_center_1 = x_wheel_1
y_wheel_center_1 = y_wheel_1 + r_bicycle 

x_wheel_center_2 = x_wheel_2
y_wheel_center_2 = y_wheel_2 + r_bicycle 

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

theta_bicycle = 0
dtheta_bicycle = 0.05

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

for i in range(0, num_points_bicycle):
    x_data_wheel_1.append(x_wheel_1)
    y_data_wheel_1.append(y_wheel_1)
    x_data_wheel_2.append(x_wheel_2)
    y_data_wheel_2.append(y_wheel_2)
    x_wheel_center_1 = x_wheel_1
    y_wheel_center_1 = y_wheel_1 + r_bicycle
    x_wheel_center_2 = x_wheel_2
    y_wheel_center_2 = y_wheel_2 + r_bicycle
    x_data_wheel_center_1.append(x_wheel_center_1)
    y_data_wheel_center_1.append(y_wheel_center_1)
    x_data_wheel_center_2.append(x_wheel_center_2)
    y_data_wheel_center_2.append(y_wheel_center_2)
    
    x_line_start_1 = x_wheel_center_1
    y_line_start_1 = y_wheel_center_1
    x_data_line_start_1.append(x_line_start_1)
    y_data_line_start_1.append(y_line_start_1)
    x_line_end_1 = x_line_start_1 + r_bicycle * math.cos(-theta_bicycle)
    y_line_end_1 = y_line_start_1 + r_bicycle * math.sin(-theta_bicycle)
    x_data_line_end_1.append(x_line_end_1)
    y_data_line_end_1.append(y_line_end_1)
    x_line_start_2 = x_wheel_center_1
    y_line_start_2 = y_wheel_center_1
    x_data_line_start_2.append(x_line_start_2)
    y_data_line_start_2.append(y_line_start_2)
    x_line_end_2 = x_line_start_2 + r_bicycle * math.cos(-theta_bicycle - 2*math.pi/3)
    y_line_end_2 = y_line_start_2 + r_bicycle * math.sin(-theta_bicycle - 2*math.pi/3)
    x_data_line_end_2.append(x_line_end_2)
    y_data_line_end_2.append(y_line_end_2)
    x_line_start_3 = x_wheel_center_1
    y_line_start_3 = y_wheel_center_1
    x_data_line_start_3.append(x_line_start_3)
    y_data_line_start_3.append(y_line_start_3)
    x_line_end_3 = x_line_start_3 + r_bicycle * math.cos(-theta_bicycle - 4*math.pi/3)
    y_line_end_3 = y_line_start_3 + r_bicycle * math.sin(-theta_bicycle - 4*math.pi/3)
    x_data_line_end_3.append(x_line_end_3)
    y_data_line_end_3.append(y_line_end_3)
    x_line_start_4 = x_wheel_center_2
    y_line_start_4 = y_wheel_center_2
    x_data_line_start_4.append(x_line_start_4)
    y_data_line_start_4.append(y_line_start_4)
    x_line_end_4 = x_line_start_4 + r_bicycle * math.cos(-theta_bicycle - math.pi/2)
    y_line_end_4 = y_line_start_4 + r_bicycle * math.sin(-theta_bicycle - math.pi/2)
    x_data_line_end_4.append(x_line_end_4)
    y_data_line_end_4.append(y_line_end_4)
    x_line_start_5 = x_wheel_center_2
    y_line_start_5 = y_wheel_center_2
    x_data_line_start_5.append(x_line_start_5)
    y_data_line_start_5.append(y_line_start_5)
    x_line_end_5 = x_line_start_5 + r_bicycle * math.cos(-theta_bicycle - 7*math.pi/6)
    y_line_end_5 = y_line_start_5 + r_bicycle * math.sin(-theta_bicycle - 7*math.pi/6)
    x_data_line_end_5.append(x_line_end_5)
    y_data_line_end_5.append(y_line_end_5)
    x_line_start_6 = x_wheel_center_2
    y_line_start_6 = y_wheel_center_2
    x_data_line_start_6.append(x_line_start_6)
    y_data_line_start_6.append(y_line_start_6)
    x_line_end_6 = x_line_start_6 + r_bicycle * math.cos(-theta_bicycle - 11*math.pi/6)
    y_line_end_6 = y_line_start_6 + r_bicycle * math.sin(-theta_bicycle - 11*math.pi/6)
    x_data_line_end_6.append(x_line_end_6)
    y_data_line_end_6.append(y_line_end_6)

    x_segment_start_1 = x_wheel_center_1
    y_segment_start_1 = y_wheel_center_1
    x_segment_end_1 = x_wheel_center_1 + (3/2) * r_bicycle 
    y_segment_end_1 = y_wheel_center_1 + (3/2) * r_bicycle
    x_data_segment_start_1.append(x_segment_start_1)
    y_data_segment_start_1.append(y_segment_start_1)
    x_data_segment_end_1.append(x_segment_end_1)
    y_data_segment_end_1.append(y_segment_end_1)

    x_segment_start_2 = x_segment_end_1
    y_segment_start_2 = y_segment_end_1
    x_segment_end_2 = x_segment_start_2 + 3 * r_bicycle
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
    x_segment_end_7 = x_segment_end_2 + r_bicycle/3
    y_segment_end_7 = y_segment_end_2 + r_bicycle
    x_data_segment_start_7.append(x_segment_start_7)
    y_data_segment_start_7.append(y_segment_start_7)
    x_data_segment_end_7.append(x_segment_end_7)
    y_data_segment_end_7.append(y_segment_end_7)

    x_segment_start_8 = x_segment_end_7 - r_bicycle/5
    y_segment_start_8 = y_segment_end_7
    x_segment_end_8 = x_segment_end_7 + r_bicycle/5
    y_segment_end_8 = y_segment_end_7
    x_data_segment_start_8.append(x_segment_start_8)
    y_data_segment_start_8.append(y_segment_start_8)
    x_data_segment_end_8.append(x_segment_end_8)
    y_data_segment_end_8.append(y_segment_end_8)

    x_segment_start_9 = x_segment_end_1 
    y_segment_start_9 = y_segment_end_1
    x_segment_end_9 = x_segment_start_9
    y_segment_end_9 = y_segment_start_9 + r_bicycle/2
    x_data_segment_start_9.append(x_segment_start_9)
    y_data_segment_start_9.append(y_segment_start_9)
    x_data_segment_end_9.append(x_segment_end_9)
    y_data_segment_end_9.append(y_segment_end_9)

    x_segment_start_10 = x_segment_end_9 - r_bicycle/5
    y_segment_start_10 = y_segment_end_9 
    x_segment_end_10 = x_segment_end_9 + r_bicycle/2
    y_segment_end_10 = y_segment_end_9
    x_data_segment_start_10.append(x_segment_start_10)
    y_data_segment_start_10.append(y_segment_start_10)
    x_data_segment_end_10.append(x_segment_end_10)
    y_data_segment_end_10.append(y_segment_end_10)

    x_segment_start_11 = x_wheel_center_1 + (3/2) * r_bicycle 
    y_segment_start_11 = y_wheel_center_1 
    x_segment_end_11 = x_segment_start_11 + r_bicycle * math.cos(-theta_bicycle) / 2
    y_segment_end_11 = y_segment_start_11 + r_bicycle * math.sin(-theta_bicycle) / 2
    x_data_segment_start_11.append(x_segment_start_11)
    y_data_segment_start_11.append(y_segment_start_11)
    x_data_segment_end_11.append(x_segment_end_11)
    y_data_segment_end_11.append(y_segment_end_11)

    x_segment_start_12 = x_wheel_center_1 + (3/2) * r_bicycle 
    y_segment_start_12 = y_wheel_center_1 
    x_segment_end_12 = x_segment_start_12 - r_bicycle * math.cos(-theta_bicycle) / 2
    y_segment_end_12 = y_segment_start_12 - r_bicycle * math.sin(-theta_bicycle) / 2
    x_data_segment_start_12.append(x_segment_start_12)
    y_data_segment_start_12.append(y_segment_start_12)
    x_data_segment_end_12.append(x_segment_end_12)
    y_data_segment_end_12.append(y_segment_end_12)
    
    x_wheel_1 = x_wheel_1 + dx_wheel_1
    y_wheel_1 = y_wheel_1 + dy_wheel_1
    x_wheel_2 = x_wheel_2 + dx_wheel_2
    y_wheel_2 = y_wheel_2 + dy_wheel_2
    theta_bicycle = theta_bicycle + dtheta_bicycle

for i in range(0, num_points_bicycle):    
    wheel_1.penup()
    wheel_1.goto(x_data_wheel_1[i], y_data_wheel_1[i])
    wheel_1.pendown()
    wheel_1.circle(r_bicycle)
    wheel_2.penup()
    wheel_2.goto(x_data_wheel_2[i], y_data_wheel_2[i])
    wheel_2.pendown()
    wheel_2.circle(r_bicycle)
    
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

    #--------------------------------------------------------------------------------
    #animate pendulum
    red, green, blue = get_random_rgb()
    pen_pendulum_circle.color(red, green, blue)
    pen_pendulum_circle.begin_fill()
    draw_circle(pen_pendulum_circle, x_pendulum_circle_data[i], y_pendulum_circle_data[i], r_pendulum)
    pen_pendulum_circle.end_fill()
    draw_line(pen_pendulum_line, 0, y_pendulum_line, x_pendulum_circle_data[i], y_pendulum_circle_data[i])
    r_pendulum = r_pendulum + 0.08

    #--------------------------------------------------------------------------------

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

    pen_pendulum_circle.clear()
    pen_pendulum_line.clear()

#----------------------------------------------------------------

#window.mainloop() 
