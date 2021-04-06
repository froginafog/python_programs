#pendulum
#author: froginafog (Liang D.S.)
import turtle
import math
import time
import random
from datetime import datetime

random.seed(datetime.now()) #to randomize the seed for "more" randomness

#--------------------------------------------------------------
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
#--------------------------------------------------------------
def draw_line(pen, x_start, y_start, x_end, y_end):
    pen.penup()
    pen.goto(x_start, y_start)
    pen.pendown()
    pen.goto(x_end, y_end)
    pen.penup()
#--------------------------------------------------------------
def theta(t, theta_0, w): #theta_0 is the initial angle, w is the angular frequency, w = sqrt(g/L)
    return theta_0 * math.cos(w * t)
#--------------------------------------------------------------
def get_random_rbg():  #get random color
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)
#--------------------------------------------------------------
window = turtle.Screen()  
window.bgcolor("midnightblue")  
window.setup(width = 1.0, height = 1.0)
window.colormode(255)

pen = turtle.Turtle()  
pen.color("silver")
pen.pensize(2)
pen.speed(5)
pen.hideturtle()

pen_line = turtle.Turtle()  
pen_line.color("silver")
pen_line.pensize(2)
pen_line.speed(2)
pen_line.hideturtle()

pen_circle = turtle.Turtle() 
pen_circle.color("lightgreen")
pen_circle.pensize(2)
pen_circle.speed(0)
pen_circle.hideturtle()

dx = 20
dy = 10
x_line = -200
y_line = 400
draw_line(pen, x_line, y_line, x_line + 400, y_line)

while(x_line < -200 + 400 - dx):
    draw_line(pen, x_line, y_line + 2 * dy, x_line + dx, y_line)
    x_line = x_line + dx

g = 9.8 #gravitational constant
L = 500 #length of the cord
w = math.sqrt(g/L)
r = 50
t = 0
dt = 1
theta_0 = 20 * math.pi/180 #initial angle of 20 degrees converted into radians
draw_line(pen_line, 0, y_line, -L * math.sin(theta(t, theta_0, w)), y_line - L * math.cos(theta(t, theta_0, w)))
draw_circle(pen_circle, -L * math.sin(theta(t, theta_0, w)) , y_line - L * math.cos(theta(t, theta_0, w)), r)
window.tracer(0)
while(True):
    angle = theta(t, theta_0, w)
    x_circle = -L * math.sin(angle) 
    y_circle = y_line - L * math.cos(angle)
    red, green, blue = get_random_rbg()
    pen_circle.color(red, green, blue)
    pen_circle.begin_fill()
    draw_circle(pen_circle, x_circle, y_circle, r)
    pen_circle.end_fill()
    draw_line(pen_line, 0, y_line, x_circle, y_circle)
    window.update()
    pen_circle.clear()
    pen_line.clear()
    t = t + dt
        
