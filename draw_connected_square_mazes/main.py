#draw connected square mazes
#author: froginafog (Liang D.S.)

import turtle
import random
from datetime import datetime

random.seed(datetime.now()) #to randomize the seed for "more" randomness

window = turtle.Screen()  #create the window
window.bgcolor("lightgrey")  #set the window's color
window.colormode(255)
window.setup(width = 1.0, height = 1.0)

pen1 = turtle.Turtle() 
pen1.pensize(5)
pen1.penup()               
pen1.goto(-900, 500)
pen1.pendown()
pen1.speed(50)

pen2 = turtle.Turtle()  
pen2.pensize(5)
pen2.penup()               
pen2.goto(900, 250)
pen2.pendown()
pen2.speed(50)

pen3 = turtle.Turtle() 
pen3.pensize(5)
pen3.penup()               
pen3.goto(-900, 0)
pen3.pendown()
pen3.speed(50)

pen4 = turtle.Turtle()  
pen4.pensize(5)
pen4.penup()               
pen4.goto(900, -250)
pen4.pendown()
pen4.speed(50)

distance = 200
angle = 90

def get_random_rbg():  #get random color
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)

while(True):
    while(distance > 0):
        r, b, g = get_random_rbg()
        pen1.pencolor(r,b,g)
        pen1.forward(distance)
        pen1.right(angle)
        r, b, g = get_random_rbg()
        pen2.pencolor(r,b,g)
        pen2.backward(distance)
        pen2.left(angle)
        r, b, g = get_random_rbg()
        pen3.pencolor(r,b,g)
        pen3.forward(distance)
        pen3.right(angle)
        r, b, g = get_random_rbg()
        pen4.pencolor(r,b,g)
        pen4.backward(distance)
        pen4.left(angle)
        distance = distance - 10
    pen1.left(angle)
    pen2.right(angle)
    pen3.left(angle)
    pen4.right(angle)
    distance = distance + 10
    while(distance < 200):
        r, b, g = get_random_rbg()
        pen1.pencolor(r,b,g)
        pen1.backward(distance)
        pen1.left(angle)
        r, b, g = get_random_rbg()
        pen2.pencolor(r,b,g)
        pen2.forward(distance)
        pen2.right(angle)
        r, b, g = get_random_rbg()
        pen3.pencolor(r,b,g)
        pen3.backward(distance)
        pen3.left(angle)
        r, b, g = get_random_rbg()
        pen4.pencolor(r,b,g)
        pen4.forward(distance)
        pen4.right(angle)
        distance = distance + 10
