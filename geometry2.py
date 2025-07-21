import turtle

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.left(90)  # Point the turtle upwards
t.penup()
t.backward(250) # Move to the bottom of the screen
t.pendown()


# --- Recursive Drawing Function ---
def draw_fractal_tree(branch_length, pen):
    if branch_length > 5:
        # Change color based on branch length
        if branch_length < 20:
            pen.pencolor("green") # Leaves
        elif branch_length < 50:
            pen.pencolor("#966F33") # Light brown branches
        else:
            pen.pencolor("#654321") # Dark brown trunk

        # Draw the main branch
        pen.pensize(branch_length / 10)
        pen.forward(branch_length)
        
        # Turn right for the first sub-branch
        pen.right(25)
        # Recursive call for the right sub-branch
        draw_fractal_tree(branch_length - 15, pen)
        
        # Turn left for the second sub-branch
        pen.left(50)
        # Recursive call for the left sub-branch
        draw_fractal_tree(branch_length - 15, pen)
        
        # Go back to the original position before the split
        pen.right(25)
        pen.penup()
        pen.backward(branch_length)
        pen.pendown()

# --- Initial Call to Start Drawing ---
draw_fractal_tree(100, t)
screen.done()