import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Drawing 福")

t = turtle.Turtle()
t.speed(3)
t.color("#FF2D00")  
t.pensize(20)       
t.hideturtle()

t.shape("circle")
t.shapesize(stretch_wid=0.5, stretch_len=0.5) 

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


move_to(-120, 110)
t.goto(-110, 100)

move_to(-140, 80)
t.goto(-80, 85)

move_to(-110, 100)
t.goto(-115, 0)

move_to(-95, 10)
t.goto(-85, -5)

left_x, right_x = -60, 60
top_y, bottom_y = 100, -80
mid_x = (left_x + right_x) / 2  
mid_y = (top_y + bottom_y) / 2  

move_to(left_x, 120)
t.goto(right_x, 120)

move_to(left_x, top_y)
t.goto(left_x, bottom_y)

move_to(left_x, top_y)
t.goto(right_x, top_y)
t.goto(right_x, bottom_y)

move_to(left_x, mid_y)
t.goto(right_x, mid_y)

move_to(mid_x, top_y)
t.goto(mid_x, bottom_y)

move_to(left_x, bottom_y)
t.goto(right_x, bottom_y)

turtle.mainloop()