import turtle
from turtle import Turtle,Screen
LINE=300
from turtle import Turtle


class Game_Screen:

    def __init__(self):
        self.draw_board()

    def draw_board(self):
        line_spacing = 30
        line = Turtle()
        line.color("white")
        line.penup()
        line.speed("fastest")
        line.hideturtle()
        line.goto(0, 290)  # Start position for the dashed line
        line.setheading(270)  # Set the initial direction to down

        # Draw the dashed line
        for _ in range(20):
            line.pendown()
            line.forward(line_spacing)  # Draw a dash
            line.penup()
            line.forward(line_spacing)  # Move without drawing to create a gap

        line.hideturtle()



