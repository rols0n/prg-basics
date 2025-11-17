import turtle

import time;

def draw_triangle(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length

    # Draw a square
    for i in range(3):
        pen.forward(length)

        # time.sleep(0.5)
        pen.right(120)



    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()


def draw_rectangle(len_a, len_b):

        # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length

    # Draw a square
    for i in range(2):
        pen.forward(len_a);
        pen.right(90);
        pen.forward(len_b);
        pen.right


    

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()