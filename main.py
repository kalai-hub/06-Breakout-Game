# main.py
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from bricks import Bricks
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")

screen.delay(0)
paddle = Paddle((0,-250))

ball = Ball()
bricks = Bricks()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with paddle
    if paddle.distance(ball) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    # Detect collision with left and right wall
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 290:
        ball.bounce_y()

    # Detect when paddle misses the ball
    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.point_reduce()

    # Detect collision with bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
                ball.bounce_y()
                scoreboard.point()

screen.exitonclick()