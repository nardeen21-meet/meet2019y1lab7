import turtle
import random
turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 10
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    snake_stamp = snake.stamp()
    stamp_list.append(snake_stamp)

    
for number in range(START_LENGTH):
    x_pos=snake.xcor()
    y_pos=snake.ycor()
    x_pos+=SQUARE_SIZE
    

    snake.goto(x_pos,y_pos)
    
    new_stamp()


def remove_tail():
    old_stamp = stamp_list.pop()
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
snake.direction = "Up"

def up():
    snake.direction="Up"
    move_snake()
    print("you pressed the up key!")
    
snake.direction = "Down"

def down():
    snake.direction="Down"
    move_snake()
    print("you pressed the down key!")

snake.direction = "Left"

def left():
    snake.direction="Left"
    move_snake()
    print("you pressed the left key!")

def right():
    snake.direction="right"
    move_snake()
    print("you pressed the right key!")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

if snake.direction == "Up":
    snake.goto(x_pos, y_pos + SQUARE_SIZE)
    print("you moved up!")
elif snake.direction=="Down":
    snake.goto(x_pos, y_pos - SQUARE_SIZE)
elif snake.direction=="Left":
    snake.goto(x_pos, y_pos - SQUARE_SIZE)































    








































    
