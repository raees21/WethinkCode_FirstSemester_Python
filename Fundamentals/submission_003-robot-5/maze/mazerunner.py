from collections import deque
import time
# from robot import robot.handle_command
# from robot import mazerunner
import robot
import sys
from random import randint
from import_helper import dynamic_import as importer

maze_list = ["raees_maze", "violet_maze", "kayden", "nathi", "kimchi"]

if len(sys.argv) == 3 and sys.argv[2] in maze_list:
    obstacle = importer("maze."+sys.argv[2])
elif len(sys.argv) == 3:
    obstacle = importer("maze"+".obstacles")
    print(sys.argv)
else:
    obstacle = importer("maze.obstacles")


pos_blocked = False
pos_allowed = True

full_obs = []
valid_path_list = []
solution = {} 
x_robot,y_robot = 0,0
robot_pos = 0
frontier = deque()
visited = set()
robot_movement_list = []

def list_each_point_of_each_obstacle():
    """Create grid with each point listed"""

    global full_obs
    obs = obstacle.obstacles

    for i in range(len(obs)):
        for j in range(5):
            for k in range(5):
                full_obs.append((obs[i][0]+j,obs[i][1]+k))


def every_cell_obstacle_list():
    """Take an obstacle coordinate and get every sing coordinate"""

    maze = []

    for i in range(-200,200, 5):
        for j in range(-100, 100, 5):
            maze.append((j,i))

    return maze


def get_valid_path_list():
    """Get a valid path for the robot the walk """
    global full_obs,valid_path_list

    list_each_point_of_each_obstacle()

    obst_list = full_obs
    full_maze = every_cell_obstacle_list()
    
    for i in full_maze:
        if i not in obst_list:
            valid_path_list.append(i)

def backRoute(x, y):
    """Start from end point and make way to start point"""

    global robot_movement_list
    robot_movement_list = []
    while (x, y) != (x_robot, y_robot):    # stop loop when current cells == start cell

        robot_movement_list.append((x,y))
        print(x,y)
        x, y = solution[x, y]

def create_path_to_follow():
    """BFS algo"""

    global full_obs,valid_path_list,x_robot,y_robot,frontier,solution
    
    (x, y) = (x_robot,y_robot)
    path = valid_path_list

    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 5, y) in path and (x - 5, y) not in visited:  # check the cell on the left
            cell = (x - 5, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-5, y))  # add cell to visited list

        if (x, y - 5) in path and (x, y - 5) not in visited:  # check the cell down
            cell = (x, y - 5)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 5))
            # print(solution)

        if(x + 5, y) in path and (x + 5, y) not in visited:   # check the cell on the  right
            cell = (x + 5, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x +5, y))

        if(x, y + 5) in path and (x, y + 5) not in visited:  # check the cell up
            cell = (x, y + 5)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 5))


def robot_solve(p,robot_name):
    """Solve BFS in turtle"""
    global robot_movement_list,x_robot,y_robot

    if (x_robot+5,y_robot) == (p[0],p[1]):
        robot.handle_command(robot_name,'right')
        robot.handle_command(robot_name,'forward 5')
        robot.handle_command(robot_name,'left')
        x_robot = x_robot+5
    elif (x_robot-5,y_robot) == (p[0],p[1]):
        robot.handle_command(robot_name,'left')
        robot.handle_command(robot_name,'forward 5')
        robot.handle_command(robot_name,'right')
        x_robot=x_robot-5
    elif (x_robot,y_robot+5) == (p[0],p[1]):
        robot.handle_command(robot_name,'forward 5')
        y_robot=y_robot+5
    elif (x_robot,y_robot-5) == (p[0],p[1]):
        robot.handle_command(robot_name,'back 5')
        y_robot=y_robot-5


def maze_run(robot_name,command_arg):
    """Mazerun function that handles all the other functions to edge"""

    global x_robot,y_robot,full_obs

    clear_globals()

    list_each_point_of_each_obstacle()

    get_valid_path_list()

    create_path_to_follow()

    command_args = command_arg.split()
    
    backRoute(-95,195)
    
    reversed_robot_list = list(reversed(robot_movement_list))
    for p in reversed_robot_list:
        robot_solve(p,robot_name)


def maze_run_top(robot_name,command_arg):
    """Mazerun function that handles all the other functions to top"""
    global x_robot,y_robot,full_obs

    clear_globals()

    list_each_point_of_each_obstacle()

    get_valid_path_list()

    create_path_to_follow()
    
    backRoute(0,195)
    
    reversed_robot_list = list(reversed(robot_movement_list))
    for p in reversed_robot_list:
        robot_solve(p,robot_name)


def maze_run_bottom(robot_name,command_arg):
    """Mazerun function that handles all the other functions to bottom"""
    global x_robot,y_robot,full_obs

    clear_globals()

    list_each_point_of_each_obstacle()

    get_valid_path_list()

    create_path_to_follow()
    
    backRoute(0,-195)
    
    reversed_robot_list = list(reversed(robot_movement_list))
    for p in reversed_robot_list:
        robot_solve(p,robot_name)


def maze_run_left(robot_name,command_arg):
    """Mazerun function that handles all the other functions to left"""
    global x_robot,y_robot,full_obs

    clear_globals()

    list_each_point_of_each_obstacle()

    get_valid_path_list()

    create_path_to_follow()
    
    backRoute(-95, 0)
    
    reversed_robot_list = list(reversed(robot_movement_list))
    for p in reversed_robot_list:
        robot_solve(p,robot_name)


def maze_run_right(robot_name,command_arg):
    """Mazerun function that handles all the other functions to right"""
    global x_robot,y_robot,full_obs

    clear_globals()

    list_each_point_of_each_obstacle()

    get_valid_path_list()

    create_path_to_follow()
    
    backRoute(95, 0)
    
    reversed_robot_list = list(reversed(robot_movement_list))
    for p in reversed_robot_list:
        robot_solve(p,robot_name)


def clear_globals():
    """Clear global variables for next run"""

    global full_obs, valid_path_list, solution, x_robot, y_robot, robot_pos, frontier, visited, robot_movement_list

    full_obs = []
    valid_path_list = []
    solution = {} 
    x_robot,y_robot = 0,0
    robot_pos = 0
    frontier = deque()
    visited = set()
    robot_movement_list = []
