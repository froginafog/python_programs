#Control the shuttle (triangle).
#Avoid the asteroids (circles).
#Capture the resource (square) for points.
#Left arrow on the keyboard to turn left.
#Right arrow on the keyboard to turn right.
#Up arrow on the keyboard to increase speed.
#The speed of the shuttle increases slightly everytime we capture a resource.

#author: froginafog (Liang D.S.)
import turtle
import math
import random

#from datetime import datetime
#random.seed(datetime.now())

random.seed(0)

#----------------------------------
def turn_left():
    shuttle.left(5)
#----------------------------------
def turn_right():
    shuttle.right(5)
#----------------------------------
def increase_speed():
    global shuttle_speed
    shuttle_speed = shuttle_speed + 0.03
#----------------------------------
"""
def decrease_speed():
    global shuttle_speed
    if(shuttle_speed >= 0.05):
        shuttle_speed = shuttle_speed - 0.05
"""
#----------------------------------
def draw_line(pen, x_start, y_start, x_end, y_end):
    pen.penup()
    pen.goto(x_start, y_start)
    pen.pendown()
    pen.goto(x_end, y_end)
    pen.penup()
#----------------------------------

radians_to_degrees = 180/math.pi
    
window = turtle.Screen()  
window.bgcolor("midnightblue")  
window.setup(width = 1.0, height = 1.0)
window.tracer(0)

#shuttle
text = turtle.Turtle()
text.color("yellow")
text.pensize(20)
text.penup()
text.hideturtle()
text.speed(0)

#shuttle
shuttle = turtle.Turtle()  
shuttle.color("lightgreen")
shuttle.shape("arrow")
shuttle.shapesize(2)
shuttle.penup()
shuttle.speed(0)
shuttle_speed = 0.1

#set the keys
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
#turtle.onkey(decrease_speed, "Down")

#draw wall
wall = turtle.Turtle()
wall.color("silver")
wall.pensize(2)
wall.hideturtle()
wall.speed(0)
draw_line(wall, -600, 400, 600, 400)
draw_line(wall, 600, 400, 600, -400)
draw_line(wall, 600, -400, -600, -400)
draw_line(wall, -600, -400, -600, 400)

#draw asteroid 1
asteroid_1 = turtle.Turtle()
asteroid_1.color("silver")
asteroid_1.shape("circle")
asteroid_1.shapesize(2)
asteroid_1.penup()
asteroid_1.speed(0)
asteroid_1_speed = 0.1
asteroid_1.goto(-500, 0)
asteroid_1.left(45)

#draw asteroid 2
asteroid_2 = turtle.Turtle()
asteroid_2.color("lightblue")
asteroid_2.shape("circle")
asteroid_2.shapesize(2)
asteroid_2.penup()
asteroid_2.speed(0)
asteroid_2_speed = 0.2
asteroid_2.goto(-400, 0)
asteroid_2.right(45)

#draw asteroid 3
asteroid_3 = turtle.Turtle()
asteroid_3.color("darkgreen")
asteroid_3.shape("circle")
asteroid_3.shapesize(2)
asteroid_3.penup()
asteroid_3.speed(0)
asteroid_3_speed = 0.3
asteroid_3.goto(-300, 0)
asteroid_3.left(45)

#draw square
square = turtle.Turtle()  
square.color("yellow")
square.shape("square")
square.shapesize(1)
square.penup()
square.speed(0)
x_square = random.randint(-550, 550)
y_square = random.randint(-350, 350)
square.goto(x_square, y_square)

orbitter = turtle.Turtle()
orbitter.color("purple")
orbitter.shape("circle")
orbitter.shapesize(1)
orbitter.penup()
orbitter.speed(0)
orbitter_speed = 0.1
r_orbit = 100
theta_orbit = 0
x_orbitter = x_square + r_orbit * math.cos(theta_orbit)
y_orbitter = y_square + r_orbit * math.sin(theta_orbit)
orbitter.goto(x_orbitter, y_orbitter)

num_points = 0
text.goto(0, 500)
text.write("points: " + str(num_points), move = False, align = 'center', font = ('arial', 20, 'normal'))

encouragement = ["good", "great", "awesome", "fantastic", "extraordinary"]

while(True):
    window.update()
    shuttle.forward(shuttle_speed)
    x_shuttle = shuttle.xcor()
    y_shuttle = shuttle.ycor()
    if(x_shuttle < -600 + shuttle_speed * 10):
        dx = x_shuttle - x_shuttle_previous
        dy = y_shuttle - y_shuttle_previous
        if(dy < 0):
            shuttle.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            shuttle.left(180)
        else: #dy > 0
            shuttle.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
    elif(x_shuttle > 600 - shuttle_speed * 10):
        dx = x_shuttle - x_shuttle_previous
        dy = y_shuttle - y_shuttle_previous
        if(dy < 0):
            shuttle.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            shuttle.left(180)
        else: #dy > 0
            shuttle.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))  
    elif(y_shuttle < -400 + shuttle_speed * 10):
        dx = x_shuttle - x_shuttle_previous
        dy = y_shuttle - y_shuttle_previous
        if(dx < 0):
            shuttle.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            shuttle.left(180)
        else: #dx > 0
            shuttle.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    elif(y_shuttle > 400 - shuttle_speed * 10):
        dx = x_shuttle - x_shuttle_previous
        dy = y_shuttle - y_shuttle_previous
        if(dx < 0):
            shuttle.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            shuttle.left(180)
        else: #dx > 0
            shuttle.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    x_shuttle_previous = x_shuttle
    y_shuttle_previous = y_shuttle

    asteroid_1.forward(asteroid_1_speed)
    x_asteroid_1 = asteroid_1.xcor()
    y_asteroid_1 = asteroid_1.ycor()
    if(x_asteroid_1 < -600 + asteroid_1_speed * 10):
        dx = x_asteroid_1 - x_asteroid_1_previous
        dy = y_asteroid_1 - y_asteroid_1_previous
        if(dy < 0):
            asteroid_1.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_1.left(180)
        else: #dy > 0
            asteroid_1.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
    elif(x_asteroid_1 > 600 - asteroid_1_speed * 10):
        dx = x_asteroid_1 - x_asteroid_1_previous
        dy = y_asteroid_1 - y_asteroid_1_previous
        if(dy < 0):
            asteroid_1.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_1.left(180)
        else: #dy > 0
            asteroid_1.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))  
    elif(y_asteroid_1 < -400 + asteroid_1_speed * 10):
        dx = x_asteroid_1 - x_asteroid_1_previous
        dy = y_asteroid_1 - y_asteroid_1_previous
        if(dx < 0):
            asteroid_1.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_1.left(180)
        else: #dx > 0
            asteroid_1.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    elif(y_asteroid_1 > 400 - asteroid_1_speed * 10):
        dx = x_asteroid_1 - x_asteroid_1_previous
        dy = y_asteroid_1 - y_asteroid_1_previous
        if(dx < 0):
            asteroid_1.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_1.left(180)
        else: #dx > 0
            asteroid_1.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    x_asteroid_1_previous = x_asteroid_1
    y_asteroid_1_previous = y_asteroid_1

    asteroid_2.forward(asteroid_2_speed)
    x_asteroid_2 = asteroid_2.xcor()
    y_asteroid_2 = asteroid_2.ycor()
    if(x_asteroid_2 < -600 + asteroid_2_speed * 10):
        dx = x_asteroid_2 - x_asteroid_2_previous
        dy = y_asteroid_2 - y_asteroid_2_previous
        if(dy < 0):
            asteroid_2.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_2.left(180)
        else: #dy > 0
            asteroid_2.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
    elif(x_asteroid_2 > 600 - asteroid_2_speed * 10):
        dx = x_asteroid_2 - x_asteroid_2_previous
        dy = y_asteroid_2 - y_asteroid_2_previous
        if(dy < 0):
            asteroid_2.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_2.left(180)
        else: #dy > 0
            asteroid_2.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))  
    elif(y_asteroid_2 < -400 + asteroid_2_speed * 10):
        dx = x_asteroid_2 - x_asteroid_2_previous
        dy = y_asteroid_2 - y_asteroid_2_previous
        if(dx < 0):
            asteroid_2.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_2.left(180)
        else: #dx > 0
            asteroid_2.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    elif(y_asteroid_2 > 400 - asteroid_2_speed * 10):
        dx = x_asteroid_2 - x_asteroid_2_previous
        dy = y_asteroid_2 - y_asteroid_2_previous
        if(dx < 0):
            asteroid_2.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_2.left(180)
        else: #dx > 0
            asteroid_2.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    x_asteroid_2_previous = x_asteroid_2
    y_asteroid_2_previous = y_asteroid_2

    asteroid_3.forward(asteroid_3_speed)
    x_asteroid_3 = asteroid_3.xcor()
    y_asteroid_3 = asteroid_3.ycor()
    if(x_asteroid_3 < -600 + asteroid_3_speed * 10):
        dx = x_asteroid_3 - x_asteroid_3_previous
        dy = y_asteroid_3 - y_asteroid_3_previous
        if(dy < 0):
            asteroid_3.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_3.left(180)
        else: #dy > 0
            asteroid_3.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
    elif(x_asteroid_3 > 600 - asteroid_3_speed * 10):
        dx = x_asteroid_3 - x_asteroid_3_previous
        dy = y_asteroid_3 - y_asteroid_3_previous
        if(dy < 0):
            asteroid_3.right(2 * abs(math.atan((dx/dy)) * radians_to_degrees))
        elif(dy == 0):
            asteroid_3.left(180)
        else: #dy > 0
            asteroid_3.left(2 * abs(math.atan((dx/dy)) * radians_to_degrees))  
    elif(y_asteroid_3 < -400 + asteroid_3_speed * 10):
        dx = x_asteroid_3 - x_asteroid_3_previous
        dy = y_asteroid_3 - y_asteroid_3_previous
        if(dx < 0):
            asteroid_3.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_3.left(180)
        else: #dx > 0
            asteroid_3.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    elif(y_asteroid_3 > 400 - asteroid_3_speed * 10):
        dx = x_asteroid_3 - x_asteroid_3_previous
        dy = y_asteroid_3 - y_asteroid_3_previous
        if(dx < 0):
            asteroid_3.left(2 * abs(math.atan((dy/dx)) * radians_to_degrees))
        elif(dx == 0):
            asteroid_3.left(180)
        else: #dx > 0
            asteroid_3.right(2 * abs(math.atan((dy/dx)) * radians_to_degrees)) 
    x_asteroid_3_previous = x_asteroid_3
    y_asteroid_3_previous = y_asteroid_3

    if(x_asteroid_1 - 22 <= x_shuttle and x_shuttle <= x_asteroid_1 + 22):
        if(y_asteroid_1 - 22 <= y_shuttle and y_shuttle <= y_asteroid_1 + 22):
            text.goto(0, -500)
            text.write("collision detected\nend of the game", move = False, align = 'center', font = ('arial', 20, 'normal'))
            break
    elif(x_asteroid_2 - 22 <= x_shuttle and x_shuttle <= x_asteroid_2 + 22):
        if(y_asteroid_2 - 22 <= y_shuttle and y_shuttle <= y_asteroid_2 + 22):
            text.goto(0, -500)
            text.write("collision detected\nend of the game", move = False, align = 'center', font = ('arial', 20, 'normal'))
            break
    elif(x_asteroid_3 - 22 <= x_shuttle and x_shuttle <= x_asteroid_3 + 22):
        if(y_asteroid_3 - 22 <= y_shuttle and y_shuttle <= y_asteroid_3 + 22):
            text.goto(0, -500)
            text.write("collision detected\nend of the game", move = False, align = 'center', font = ('arial', 20, 'normal'))
            break

    x_square = square.xcor()
    y_square = square.ycor()

    if(x_square - 16 <= x_shuttle and x_shuttle <= x_square + 16):
        if(y_square - 16 <= y_shuttle and y_shuttle <= y_square + 16):
            num_points = num_points + 1
            text.goto(0, 500)
            text.clear()
            text.write("points: " + str(num_points), move = False, align = 'center', font = ('arial', 20, 'normal'))
            text.goto(0, 470)
            text.write(encouragement[(num_points - 1) % 5], move = False, align = 'center', font = ('arial', 20, 'normal'))
            square.goto(random.randint(-500, 500), random.randint(-300, 300))
            increase_speed()
            x_square = square.xcor()
            y_square = square.ycor()
            theta_orbit = 0

    x_orbitter = x_square + r_orbit * math.cos(theta_orbit)
    y_orbitter = y_square + r_orbit * math.sin(theta_orbit)
    orbitter.goto(x_orbitter, y_orbitter)
    theta_orbit = theta_orbit + 0.001

    if(x_orbitter - 16 <= x_shuttle and x_shuttle <= x_orbitter + 16):
        if(y_orbitter - 16 <= y_shuttle and y_shuttle <= y_orbitter + 16):
            text.goto(0, -500)
            text.write("collision detected\nend of the game", move = False, align = 'center', font = ('arial', 20, 'normal'))
            break
            
        
print("END")
