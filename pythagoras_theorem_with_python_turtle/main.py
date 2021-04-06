#pythagoras theorem demo
#author: froginafog (Liang D.S.)
import turtle
import time

window = turtle.Screen() 
window.bgcolor("lightgreen")  
window.setup(width = 1.0, height = 1.0)

pen = turtle.Turtle()  
pen.color("gray")
pen.pensize(2)
pen.speed(3)

def draw_stairs(starting_x, starting_y, step_width, step_height, num_steps):
    pen.penup()
    x = starting_x
    y = starting_y
    pen.goto(x, y)
    pen.pendown()
    step_number = 0
    while(step_number < num_steps):
        y = y + step_height
        pen.goto(x, y)
        x = x + step_width
        pen.goto(x, y)
        step_number = step_number + 1
    pen.goto(x, starting_y)
    pen.goto(starting_x, starting_y) 

number_of_steps = input("Enter the number of steps: ")
number_of_steps = int(number_of_steps)

time.sleep(3)

starting_x_position = -700
starting_y_position = -400
width_of_each_step = 200
height_of_each_step = 100
pen.fillcolor("gray")
pen.begin_fill()
draw_stairs(starting_x_position, starting_y_position, width_of_each_step, height_of_each_step, number_of_steps)
pen.end_fill()

#--------------------------------------------------------------------

#draw the hypothenuse of the stairs
pen.color("navy")
x = starting_x_position + width_of_each_step * number_of_steps
y = starting_y_position + height_of_each_step * number_of_steps
pen.goto(x, y)

#--------------------------------------------------------------------

#draw the labels
pen.penup()

step_number = 0
x = starting_x_position - width_of_each_step / 12
y = starting_y_position + height_of_each_step / 3
while(step_number < number_of_steps):
    pen.goto(x, y)
    label = "b"
    pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))
    x = x + width_of_each_step
    y = y + height_of_each_step
    pen.goto(x, y)
    step_number = step_number + 1

step_number = 0
x = starting_x_position + width_of_each_step / 2
y = starting_y_position + height_of_each_step
while(step_number < number_of_steps):
    pen.goto(x, y)
    label = "a"
    pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))
    x = x + width_of_each_step
    y = y + height_of_each_step
    pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))
    pen.goto(x, y)
    step_number = step_number + 1

step_number = 0
x = starting_x_position + width_of_each_step / 2
y = starting_y_position + height_of_each_step / 2
while(step_number < number_of_steps):
    pen.goto(x, y)
    label = "h"
    pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))
    x = x + width_of_each_step
    y = y + height_of_each_step
    pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))
    pen.goto(x, y)
    step_number = step_number + 1

x = starting_x_position + width_of_each_step * number_of_steps * 0.4
y = starting_y_position + height_of_each_step * number_of_steps * 0.3
pen.goto(x, y)
label = "H"
pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))

x = starting_x_position + width_of_each_step * number_of_steps * 0.5
y = starting_y_position * 1.1
pen.goto(x, y)
label = "A"
pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))

x = starting_x_position + width_of_each_step * number_of_steps * 1.02
y = starting_y_position + height_of_each_step * number_of_steps * 0.5
pen.goto(x, y)
label = "B"
pen.write(label, move = False, align = 'center', font = ('arial', 20, 'normal'))

#--------------------------------------------------------------------

#print the equations
pen.speed(1)

def convert_number_to_superscript(n):
    super = list(map(chr,[8304,185,178,179,8308,8309,8310,8311,8312,8313]))
    s = ""
    for x in str(n):
        s = s + super[int(x)]
    return(s)

pen.penup()
x = -850
y = 490
pen.goto(x, y)
label = "Pythagoras Theorem"
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 450
pen.goto(x, y)
label = "a" + convert_number_to_superscript(2) + " + " + "b" + convert_number_to_superscript(2) + " = " + "h" + convert_number_to_superscript(2) 
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 400
pen.goto(x, y)
label = "A = " + str(number_of_steps) + "a"   
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -650
y = 400
pen.goto(x, y)
label = "B = " + str(number_of_steps) + "b"   
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -450
y = 400
pen.goto(x, y)
label = "H = " + str(number_of_steps) + "h"   
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 350
pen.goto(x, y)
label = "A" + convert_number_to_superscript(2) + " + " + "B" + convert_number_to_superscript(2) + " = " + "H" + convert_number_to_superscript(2) 
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 300
pen.goto(x, y)
label = "(" + str(number_of_steps) + "a)" + convert_number_to_superscript(2) + " + " + "(" + str(number_of_steps) + "b)" + convert_number_to_superscript(2) + " = (" + str(number_of_steps) + "h)" + convert_number_to_superscript(2) 
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 250
pen.goto(x, y)
label = str(number_of_steps) + convert_number_to_superscript(2) + "a" + convert_number_to_superscript(2) + " + " + str(number_of_steps) + convert_number_to_superscript(2) + "b" + convert_number_to_superscript(2) + " = " + str(number_of_steps) + convert_number_to_superscript(2) + "h" + convert_number_to_superscript(2) 
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))

time.sleep(3)

x = -850
y = 200
pen.goto(x, y)
label = "a" + convert_number_to_superscript(2) + " + " + "b" + convert_number_to_superscript(2) + " = " + "h" + convert_number_to_superscript(2) 
pen.write(label, move = False, align = 'left', font = ('arial', 20, 'normal'))


