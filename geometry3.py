import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

num_lines = 300
hue = 0.0

for i in range(num_lines):

    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    t.forward(250)
    
    hue += 1 / num_lines
    
    t.right(360 / num_lines + 1)

screen.done()