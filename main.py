from turtle import Screen
from paddleClass import Paddle
from ballClass import Ball
from scoreboardClass import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
# Disable both horizontal and vertical resizing
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#Scoreboard placement
scoreboard.update_scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Change direction on side walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle 
    if ball.distance(r_paddle) < 55 and ball.xcor() == 320 or ball.distance(l_paddle) < 55 and ball.xcor() == -320:
        ball.bounce_x()

    #It resets when it goes off boundaries
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.scoreboard_l()
    #When the ball goes off the left side it gives a point to the right player


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.scoreboard_r()
    #When the ball goes off the right side it gives a point to the left player

screen.exitonclick()