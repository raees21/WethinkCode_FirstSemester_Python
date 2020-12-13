import turtle
import random
# empty list to which obstacles positions are appended to.
x = 0
y = 0
obstacles = []
def get_obstacles():
    global obstacles
    obstacles = [(-100,170), (100,200), (100,-200), (-100,-200),(-100,200),(100,100),(100,70),   #first wall
    (-80,170),(80,170),(80,-170),(-60,-170),                        #second wall
    (-60,140),(60,141),(60,-140),(-60,-140),                        #third wall
    (-40,110),(40,110),(40,-110),(-40,-110),                        #forth wall
    (-24,80),(24,80),(24,-80),(-24,-80)]                            #inner most wall
    outer_most_wall(obstacles)
    second_wall(obstacles)
    third_wall(obstacles)
    forth_wall(obstacles)
    inner_most_wall(obstacles)
    return obstacles
def outer_most_wall(obstacles):
    for i in range(obstacles[3][1],obstacles[0][1],4):
        left = (obstacles[0][0],i)
        obstacles.append(left)
    for i in range(-75,obstacles[2][0],4):
        bottom_x = (i,obstacles[3][1])
        obstacles.append(bottom_x)
    # for i in range(obstacles[2][1], obstacles[1][1],4):
    #     right_y = (obstacles[1][0],i)
    #     obstacles.append(right_y)
    for i in range(obstacles[4][0], obstacles[0][0],4):
        left_wall= (i, obstacles[1][0])
        obstacles.append(left_wall)
    for i in range(-80, obstacles[1][0],4):
        very_top = (i,obstacles[4][1])
        obstacles.append(very_top)
    # for i in range(obstacles[3][0],obstacles[4][0]):
    #     blocked = (i,0)
    #     obstacles.append(blocked)
    # print(obstacles)
# obstacles[2][1]
    for i in range(-170,obstacles[6][1], 4):
        bottom_right = (obstacles[6][0],i)
        obstacles.append(bottom_right)
    for i in range(obstacles[5][0],obstacles[1][1],4):
        top_right =(obstacles[5][1],i)
        obstacles.append(top_right)
def second_wall(obstacles):
    for i in range(obstacles[7][0], obstacles[8][0],4):
        i = i -20
        top = (i, obstacles[7][1])
        obstacles.append(top)
    for i in range(obstacles[9][1], obstacles[8][1],4):
        right = (obstacles[8][0],i)
        obstacles.append(right)
    for i in range(obstacles[10][0],obstacles[8][0],4):
        bottom = (i,obstacles[10][1])
        obstacles.append(bottom)
    for i in range(obstacles[10][1],obstacles[7][1],4):
        left = (obstacles[7][0],i)
        obstacles.append(left)
    for i in range(80,100):
        short = (i,30)
        obstacles.append(short)
def third_wall(obstacles):
    for i in range(-40, obstacles[12][0],4):
        top = (i, obstacles[11][1])
        obstacles.append(top)
    for i in range(obstacles[14][1],obstacles[11][1],4):
        left = (obstacles[11][0],i)
        obstacles.append(left)
    for i in range(obstacles[14][0],obstacles[10][0],4):
        bottom_x = (i,obstacles[14][1])
        obstacles.append(bottom_x)
    for i in range (obstacles[14][0], obstacles[13][0],4):
        bottom = (i, obstacles[14][1])
        obstacles.append(bottom)
    for i in range(obstacles[13][1], 171,2):
        right = (obstacles[12][0],i)
        obstacles.append(right)
    for i in range(-60,-40):
        blocked = (i,30)
        obstacles.append(blocked)
def forth_wall(obstacles):
    for i in range(obstacles[15][0], obstacles[16][0],4):
        top = (i, obstacles[15][1])
        obstacles.append(top)
    for i in range(obstacles[18][1],obstacles[15][1],4):
        left = (obstacles[15][0],i)
        obstacles.append(left)
    for i in range(obstacles[17][1], obstacles[16][1],4):
        right = (obstacles[16][0],i)
        obstacles.append(right)
    for i in range(-20, obstacles[17][0],4):
        bottom = (i,obstacles[18][1])
        obstacles.append(bottom)
def inner_most_wall(obstacles):
    for i in range(obstacles[22][1],obstacles[19][1],4):
        left = (obstacles[19][0],i)
        obstacles.append(left)
    for i in range(-6,obstacles[20][0],4):
        bottom = (i,obstacles[22][1])
        obstacles.append(bottom)
    for i in range(obstacles[21][1], obstacles[20][1],4):
        right = (obstacles[20][0],i)
        obstacles.append(right)
    for i in range(-6, obstacles[20][0],4):
        top = (i,obstacles[19][1])
        obstacles.append(top)
# for i in obstacles:
#     draw_obstacles(i)
def is_position_blocked(x, y):
    '''
    This function checks if there is an obsticle in a certain position. 
    If position is blocked return True else return False.
    '''
    global obstacles
    for i in obstacles:
        if x >= i[0] and x <= i[0] + 4 and y >= i[1] and y <= i[1] + 4:
            return True
    return False
def is_path_blocked(x1, y1, x2, y2):
    '''
    This function checks if the robot can move on a certain path.
    If path is blocked return True else return False.
    '''
    global obstacles
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if y1 == y2:
        for x in range(x1, x2 + 1):
            if is_position_blocked(x, y1):
                return True
    if x1 == x2:
        for y in range(y1, y2 + 1):
            if is_position_blocked(x1, y):
                return True
    return False