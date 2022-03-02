# This is a pin gong game
# In the upgrade, the hoops should be flying up and down, so if the player gets it through, they get extra 50 points
# There should be limits to where the paddles can go
# Create cheat code using my name, so that paddles can move left or right- Done
# Add levels
# Create cheat code to decrease or increase ball speed for either opponent
# Create collision for when paddles' use cheat code
# Create pause button
# Make game one player
# By @ Tioluwanimofe
import turtle as tt
# import win sound
# import Wikipedia as wiki

window = tt.Screen()
window.title("Ping-pong @ Tioluwanimofe")
window.bgcolor("gray")
window.setup(width=800, height=600)
window.tracer(0)

# Creating props

# Paddle A
paddle_a = tt.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = tt.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = tt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09

# Score
score_a = 0
score_b = 0

# Pen
pen = tt.Turtle()
pen.speed()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0 ", align="center", font=("Courier", 24, "normal"))


# Upgrades
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

# Functions of the paddles, hoops, and ball that define their actions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)


def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)


def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)


def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "Up")
window.onkeypress(paddle_a_down, "Down")
window.onkeypress(paddle_b_up, "Left")
window.onkeypress(paddle_b_down, "Right")
window.onkeypress(paddle_a_right, "m")
window.onkeypress(paddle_a_left, "o")
window.onkeypress(paddle_b_right, "f")
window.onkeypress(paddle_b_left, "e")

# Main game loop
while True:
    # Download the file and play the song "Folake for the night oo"
    # win sound.PlaySound("g", win sound.SND_ASYNC)
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
        ball.dy *= -1
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")
                  )
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")
                  )
    #  Paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
