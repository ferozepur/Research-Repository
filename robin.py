import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
design = turtle.Turtle()
design.speed(10)  # Set the speed of drawing

# Set the pen color and thickness
design.color("yellow")
design.pensize(5)

# Draw the square using triangles
for _ in range(4):
    for _ in range(3):
        design.forward(150)
        design.right(120)
    design.right(90)

# Hide the turtle and display the drawing
design.hideturtle()
turtle.done()
