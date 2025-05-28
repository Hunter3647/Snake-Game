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

#Movement
def Move_up():
    Snake.sety(snake.ycor()+10)

def Move_down():
    Snake.sety(snake.ycor()-10)

def Move_left():
    Snake.setx(snake.xcor()-10)

def Move_right():
    Snake.setx(snake.xcor()+10)

screen.listen()
screen.onkey(Move_up,"w")
screen.onkey(Move_left,"a")
screen.onkey(Move_right,"s")
screen.onkey(Move_down,"d")

while True:
    screen.update()
    
    if snake.distance(food) < 10:
        score = score+1
turtle.done()