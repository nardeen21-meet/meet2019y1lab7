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
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
snake.direction = "Up",

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up"
    
    print("you pressed the up key!")
    

def down():
    snake.direction="Down"
    print("you pressed the down key!")
    

def left():
    snake.direction="Left"
    print("you pressed the left key!")


def right():
    snake.direction="Right"
    print("you pressed the right key!")


turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100),(-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    
    food.goto(this_food_pos)
    foodid = food.stamp()
    food_stamps.append(foodid)
    food.hideturtle()





def move_snake():
    x_pos = snake.xcor()
    y_pos = snake.ycor()
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")

    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    elif snake.direction=="Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        
    elif snake.direction=="Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)

  #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_index])
        food_pos.pop(food_index)
        print("you have eaten the food!")
        
    remove_tail()
    
    
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if my_pos[0] >= RIGHT_EDGE:
        
         print("You hit the right edge! Game over!")
         quit()

    elif my_pos[0] <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
         
    elif my_pos[1] >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif my_pos[1] <= DOWN_EDGE:
        print("you hit the down edge! Game over!")
        quit()
        
    turtle.ontimer(move_snake,TIME_STEP)
    
move_snake()

    
turtle.mainloop()


     






























    




















    
