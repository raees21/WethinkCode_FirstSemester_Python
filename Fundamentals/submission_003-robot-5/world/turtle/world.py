import sys
import turtle
from import_helper import dynamic_import as importer

maze_list = ["raees_maze", "violet_maze", "kayden", "nathi", "kimchi"]

if len(sys.argv) == 3 and sys.argv[2] in maze_list:
    obstacle = importer("maze."+sys.argv[2])
elif len(sys.argv) == 3:
    obstacle = importer("maze"+".obstacles")
    print(sys.argv)
else:
    obstacle = importer("maze.obstacles")



# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
robot_name = ""


# turtle initialisation
screen = turtle.getscreen()
board = turtle.Turtle()
turtle.setworldcoordinates(-300, -300, 300, 300)
turtle.setheading(90)
turtle.tracer(n=1, delay=0) 
turtle.delay(0)


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y
    #return True

def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, current_direction_index
    new_x = position_x
    new_y = position_y

    
    if current_direction_index == 0:
        turtle.setheading(90)
    if current_direction_index == 1:
        turtle.setheading(0)
    if current_direction_index == 2:
        turtle.setheading(270)
    if current_direction_index == 3:
        turtle.setheading(180)

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if len(sys.argv) == 2:
        if obstacle.is_position_blocked(new_x,new_y) == True:
            return False

        if obstacle.is_path_blocked(position_x,position_y,new_x,new_y) == True:
            return False

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False




def show_position(robot_name):
    """Shows the final position after the robot has moved"""

    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    turtle.setposition(position_x, position_y)


def print_obstacles(robot_name):
    """Prints an obstacle list for the user"""
    print(sys.argv[0])
    if obstacle.get_obstacles() != []: 
        print(robot_name+": Loaded obstacles.")
        print("There are some obstacles:")
        for i in range(len(obstacle.obstacles)):
            print(f"- At position {obstacle.obstacles[i][0]}, {obstacle.obstacles[i][1]} (to {obstacle.obstacles[i][0]+4},{obstacle.obstacles[i][1]+4})")
            draw_obstacles(obstacle.obstacles[i][0], obstacle.obstacles[i][1])


def reset_obstacles_global():
    """Resets global obstacle after its been used"""
    global position_x, position_y, current_direction_index

    position_x = 0
    position_y = 0
    current_direction_index = 0
    obstacle.obstacles = []
            

def draw_rectangle(board,x,y,width,height,size,color):
    """Draws a rectangle for the outline border"""

    board.pencolor(color)
    board.pensize(size)
    board.setheading(0)
 
    board.up()
    board.goto(x,y)
    board.down()
    # draw top
    board.forward(width)
    # draw right
    board.right(90)
    board.forward(height)
    # draw bottom
    board.right(90)
    board.forward(width)
    # draw left
    board.right(90)
    board.forward(height)
    board.end_fill()



draw_rectangle(board,-100,200,200,400,2,"red")

def draw_obstacles(x, y):
    """Draws a square filled in, used for obstacles"""

    t = turtle.Turtle()
    t.pencolor('black')
    t.penup()
    t.setposition(x, y)
    t.fillcolor('black')
    t.speed(0)
    #t.tracer(n=1, delay=0)

    t.pendown()
    
    t.begin_fill()

    for i in range(4):
        t.forward(4)
        t.right(90)

    t.end_fill()  
    t.penup()
    t.hideturtle()
