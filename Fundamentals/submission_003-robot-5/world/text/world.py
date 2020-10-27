import maze.obstacles as obstacle

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

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


def print_obstacles():
    """Prints an obstacle list for the user"""

    if obstacle.get_obstacles() != []:
        print("There are some obstacles:")
        for i in range(len(obstacle.obstacles)):
            print(f"- At position {obstacle.obstacles[i][0]},{obstacle.obstacles[i][1]} (to {obstacle.obstacles[i][0]+4},{obstacle.obstacles[i][1]+4})")


def reset_obstacles_global():
    """Resets global obstacle after its been used"""
    global position_x, position_y, current_direction_index

    position_x = 0
    position_y = 0
    current_direction_index = 0
    obstacle.obstacles = []

def setup_world():
    pass

