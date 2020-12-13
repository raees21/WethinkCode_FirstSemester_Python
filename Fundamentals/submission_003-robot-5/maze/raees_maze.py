from random import shuffle, randrange
import random

random_amount = 0
obstacles = []

def get_obstacles():
    """Creates the maze into an obstacle list"""

    global obstacles

    maze = [
    "  XXXXXXXXXX  XXXXXXXXXXX",
    "                        X",
    "X  XXXXXXX      XXXXXX  X",
    "X                    X  X",
    "X  X XXXXXXXXXXXXXX  X  X",
    "X  X              X  X  X",
    "X  X              X  X  X",
    "X  X  XXXXXXXXXXXXX  X  X",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "   X  X           X  X   ",
    "   X  X           X  X   ",
    "   X              X  X   ",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  X XXXXXXXXX X  X  X",   
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  X           X  X  X",
    "X  X  XXXXXX  XXXXX  X  X",
    "X                       X",
    "XXXXXXXXXXX    XXXXXXXXXX"
    ]
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            character = maze[row][col]
        
            x = -96 + (col * 8)
            y = 196 - (row * 16)

            if character == 'X':
                obstacles.append((x,y))
                obstacles.append((x - 4, y))
                obstacles.append((x, y -4))
                obstacles.append((x - 4, y -4))
                obstacles.append((x, y -8))
                obstacles.append((x -4, y -8))
                obstacles.append((x -4, y -12))
                obstacles.append((x , y -12))

        
    print(obstacles)

    return obstacles


def is_position_blocked(x,y):
    """Determines if the final position falls within the obstacle and returns True
    else it will return false if it doesn't fall within the obstacle"""

    for obs in obstacles:
        if (x >= obs[0] and x <= obs[0]+4) and ( y >= obs[1] and y <= obs[1]+4):
            return True

    return False


def is_path_blocked(x1,y1,x2,y2):
    """Determines if the final position falls after an obstacle and its way is blocked and returns true
    if it doesnt fall after an obstacle it will return False"""

    x_values = []
    y_values = []

    for i in range(len(obstacles)):
        for j in range(5):
            x_values.append(obstacles[i][0]+j)
            y_values.append(obstacles[i][1]+j)

    for i in range(len(x_values)):
        if x1 == x2 and x1 == x_values[i]:
            if y2 < y1 and y2 < y_values[i] and y_values[i] < y1 and is_position_blocked(x2,y2) == False:
                print("path x negative")
                return True

            if y2 > y1 and y2 > y_values[i] and y_values[i] > y1 and is_position_blocked(x2,y2) == False:
                print("path x positive")
                return True

    for i in range(len(x_values)):
        if y1 == y2 and y1 == y_values[i]:
            if x2 < x1 and x2 < x_values[i] and x_values[i] < x1 and is_position_blocked(x2,y2) == False:
                print("path y negative")
                return True
            if x2 > x1 and x2 > x_values[i] and x_values[i] < x1 and is_position_blocked(x2,y2) == False:
                print("path y positive")
                return True

    return False







