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
#
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=600, height=600)

# def layout():
#     tim = Turtle()
#     tim.color("white")
#     tim.penup()
#     tim.goto(-280, 280)
#     tim.color("white")
#     tim.pendown()
#     tim.hideturtle()
#     for x in range(4):
#         tim.forward(300)
#         tim.right(90)


# layout()
# screen.exitonclick()