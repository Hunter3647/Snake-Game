import turtle

#create Screen
screen = turtle.Screen()
screen.bgcolor("Light Green")
screen.title("Snake Game")

#Create Snake
snake=turtle.Turtle()
snake.shape("square")
snake.color("Blue")
snake.penup()

#Snake Food
food=turtle.Turtle()
food.shape=("triangle")
food.color=("Red")
food.penup()
food.goto(100,100)

#Score
score=0
text=turtle.Turtle()
turtle.done()