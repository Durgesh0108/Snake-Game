from turtle import Turtle, Screen
# from turtle import Turtle
screen = Screen()


class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 270)
        self.color("white", "black")
        self.pendown()
        self.hideturtle()
        self.begin_fill()
        for x in range(4):
            self.forward(540)
            self.right(90)
        self.end_fill()
