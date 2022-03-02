# Th1s 1s mY MaD hOuSe D3SiGn

# By @ Tioluwanimofe
import turtle as tt
import random as rd


window = tt.Screen()
window.title("MaD hOuSe @ Tioluwanimofe")
window.bgcolor("gray")
window.setup(width=800, height=600)
window.tracer(0)

# Creating props
# Ball
ball = tt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(380, -10)
ball.dx = 0.05
ball.dy = 0.05

ball_2 = tt.Turtle()
ball_2.speed(0)
ball_2.shape("circle")
ball_2.color("pink")
ball_2.penup()
ball_2.goto(-380, -10)
ball_2.dx = 0.05
ball_2.dy = 0.05

user = input("Hello, what's your name: ")
pen = tt.Turtle()
pen.speed()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 0)
pen.write(user, align="center", font=("Courier", 24, "normal"))
# Upgrades

# Define a function to check alternate each text in the sentence from uppercase to lowercase

# Hoop A
# hoop_a = tt.Turtle()
# hoop_a.speed(0)
# hoop_a.shape("square")
# hoop_a.color("pink")
# hoop_a.shapesize(stretch_wid=5, stretch_len=1)
# hoop_a.penup()
# hoop_a.goto(350, 0)

# Hoop B
# hoop_b = tt.Turtle()
# hoop_b.speed(0)
# hoop_b.shape("circle")
# hoop_b.color("pink")
# hoop_b.shapesize(stretch_wid=5, stretch_len=1)
# hoop_b.penup()
# hoop_b.goto(350, 0)


# Main design loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= +1
    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1
    if ball.xcor() < -380:
        ball.setx(-380)
        ball.dx *= +1

    if ball_2.ycor() > 280:
        ball_2.sety(280)
        ball_2.dy *= -1
    if ball_2.ycor() < -280:
        ball_2.sety(-280)
        ball_2.dy *= +1
    if ball_2.xcor() > -380:
        ball_2.setx(-380)
        ball_2.dx *= -1
    if ball_2.xcor() < 380:
        ball_2.setx(380)
        ball_2.dx *= +1

window.listen()
window.onkeypress("m")
window.onkeypress("o")
window.onkeypress("f")
window.onkeypress("e")

# Functions of the hoops and texts that define their actions
# def check_for_letter():
#    if window.listen == "a" or "A":
#       print("A")
#    if window.listen == "b" or "B":
#       print("B")
#    if window.listen == "c" or "C":
#       print("C")
#    if window.listen == "d" or "D":
#       print("D")
#    if window.listen == "e" or "E":
#       print("E")
# if window.listen == "f" or "F":
# print("F")
# if window.listen == "g" or "G":
# print("G")
# if window.listen == "h" or "H":
# print("H")
# if window.listen == "i" or "I":
# print("I")
# if window.listen == "j" or "J":
# print("J")
# if window.listen == "k" or "K":
# print("K")
# if window.listen == "l" or "L":
# print("L")
# if window.listen == "m" or "M":
# print("M")
# if window.listen == "n" or "N":
# print("N")
# if window.listen == "o" or "O":
# print("O")
# if window.listen == "p" or "P":
# print("P")
# if window.listen == "q" or "Q":
# print("Q")
# if window.listen == "r" or "R":
# print("R")
# if window.listen == "s" or "S":
# print("S")
# if window.listen == "t" or "T":
# print("T")
# if window.listen == "u" or "U":
# print("U")
# if window.listen == "v" or "V":
# print("V")
# if window.listen == "w" or "W":
# print("W")
# if window.listen == "x" or "X":
# print("X")
# if window.listen == "Y" or "Y":
# print("Y")
# if window.listen == "z" or "Z":
# print("Z")
