obst_check = False
level_maze = []
obs = []
level = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXX",
    "XX              XXXX    XXXXXX      XXXX",
    "XX              XXXX    XXXXXX      XXXX",
    "XX              XXXX    XXXXXX      XXXX",
    "XX              XXXX    XXXXXX      XXXX",
    "XX        XXXXXXXXXX    XXXXXX      XXXX",
    "XX        XXXXXXXXXX    XXXXXX      XXXX",
    "XX        XXXXXXXXXX    XXXXXX      XXXX",
    "XX        XXXXXXXXXX    XXXXXX      XXXX",
    "XX                                  XXXX",
    "XX                                  XXXX",
    "XX                                  XXXX",
    "XX                                  XXXX",
    "XX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XX        XXXXXX                        ",
    "XX        XXXXXX                        ",
    "XX        XXXXXX                        ",
    "XX        XXXXXX                        ",
    "XX            XX      XXXXXXXXXXXXXXXXXX",
    "XX            XX      XXXXXXXXXXXXXXXXXX",
    "XX            XX      XXXXXXXXXXXXXXXXXX",
    "XX            XX      XXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXX    XX      XXXXXX            ",
    "XXXXXXXXXX    XX      XXXXXX            ",
    "XXXXXXXXXX    XX      XXXXXX            ",
    "XXXXXXXXXX    XX      XXXXXX    XXXXXXXX",
    "XX      XX    XX      XXXXXX    XXXXXXXX",
    "XX      XX    XX      XXXXXX    XXXXXXXX",
    "XX      XX    XX      XXXXXX    XXXXXXXX",
    "XX      XX    XX      XXXXXX    XXXXXXXX",
    "XX      XX                XX    XXXXXXXX",
    "XX      XX                XX    XXXXXXXX",
    "        XX                XX    XXXXXXXX",
    "        XX                XX    XXXXXXXX",
    "        XX      XX        XX        XXXX",
    "        XX      XX        XX        XXXX",
    "        XX      XX                  XXXX",
    "XX      XX      XX                  XXXX",
    "XX      XX      XX              XXXXXXXX",
    "XX      XX      XX        XX    XXXXXXXX",
    "XX      XX      XX        XX    XXXXXXXX",
    "XX      XX      XX        XX    XXXXXXXX",
    "XX      XX      XX      XXXX    XXXXXXXX",
    "XX      XX      XX      XXXX    XXXXXXXX",
    "XX      XX      XX      XXXX    XXXXXXXX",
    "XX      XX    XXXX      XXXXXXXXXXXXXXXX",
    "XX      XX    XXXX      XXXXXXXXXXXXXXXX",
    "XX      XX    XXXX      XXXXXXXXXXXXXXXX",
    "XX      XX    XXXX      XXXXXXXXXXXXXXXX",
    "XX            XXXX                XXXXXX",
    "XX            XXXX                XXXXXX",
    "XX            XXXX                XXXXXX",
    "XX            XXXX                XXXXXX",
    "XX      XX      XXXXXXXX    XX    XXXXXX",
    "XX      XX      XXXXXXXX    XX    XXXXXX",
    "XX      XX      XXXXXXXX    XX    XXXXXX",
    "XX      XX      XXXXXXXX    XX    XXXXXX",
    "XXXXXXXXXX      XXXXXXXX    XX    XXXXXX",
    "XXXXXXXXXX      XXXXXXXX    XX    XXXXXX",
    "XXXXXXXXXX      XXXXXXXX    XX    XXXXXX",
    "XXXXXXXXXX      XXXXXXXX    XX    XXXXXX",
    "XX              XX                XXXXXX",
    "XX              XX                XXXXXX",
    "XX              XX                XXXXXX",
    "XX              XX                XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXX     XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXX     XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXXX    XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXXX    XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXXX    XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXXX    XXXXXX",
    "XX      XXXXXXXXXXXXXXXXXXXXXX          ",
    "XX      XXXXXXXXXXXXXXXXXXXXXX          ",]
​
global obstacle_lst
​
obstacle_lst = []
cord_list = []
def maze_level(level):
    global obstacle_lst
    for y in range(len(level)):
        for x in range(len(level[y])):
            #find character
            charX = level[y][x]
            #calc cords
            pos_x = -90 + (x * 5)
            pos_y = 205 - (y * 5)
            cords = pos_x-10,pos_y-10
            cord_list.append(cords)
            if charX == "X":
                obs = pos_x-10,pos_y-10
                obstacle_lst.append(obs)
    return obstacle_lst
​
def get_obstacles():
    global obstacles
    maze_level(level)
    return obstacles
​
def is_position_blocked(x, y):
    """
    Makes sure robot cannot occupy the same space as the robot
    """
    global obst_check
    for i in range(len(obstacle_lst)):
        x_check = obstacle_lst[i][0]
        y_check = obstacle_lst[i][1]
        if y_check <= y <= (y_check + 4) and x_check <= x <= (x_check + 4):
            obst_check = True
            return True
    obst_check = False
    return False
​
​
def is_path_blocked(x1, y1, x2, y2):
    """
    -Blocks the robot from skipping the obstacles
    -Returns true if there is an obstacles
    """
    global obstacle_lst
    global obst_check
    obst_check = True
    for i in obstacle_lst:
        obs_x = i[0]
        obs_y = i[1]
        if x1 == x2 and (obs_x <= x1 and x1 <= obs_x + 4):
            if y2 < obs_y:
                return y1 >= obs_y
            elif y2 > obs_y + 4:
                return y1 <= obs_y + 4
        elif y1 == y2 and (obs_y <= y1 and y1 <= obs_y + 4):
            if x2 < obs_x:
                return x1 >= obs_x
            elif x2 > obs_x + 4:
                return x1 <= obs_x + 4
    obst_check = False
    return False