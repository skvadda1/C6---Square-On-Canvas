import turtle

turtle.Screen().bgcolor("Blue")

sc = turtle.Screen()
sc,setup = (400,300)

turtle.title("Welcome To Turtle UI")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(98)
    i = i+1