from random import shuffle, randrange
import random

random_amount = 0
obstacles = []

def get_obstacles():
    """Gets a list of obstacles and return it"""

    global obstacles
    x_width= 200
    y_height= 400
    size_obstacle = 5
    maze = make_maze((x_width // size_obstacle) // 2, (y_height // size_obstacle) // 2)

    maze[0]  = '00111111111111111111111111111111111111100'
    #maze[38] = '10000000000000000000000000000000000000001'
    maze[39] = '00000000000000000000000000000000000000001'
    maze[40] = '00000000000000000000000000000000000000001'
    maze[41] = '00000000000000000000000000000000000000001'
    #maze[42] = '10000000000000000000000000000000000000001'
    maze[80] = '00111111111111111111111111111111111111100'

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '1':
                x = -100 + (col * 5)
                y = 200 - (row * 5)
                obstacles.append((x,y))


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
                print("neg")
                return True

            if y2 > y1 and y2 > y_values[i] and y_values[i] > y1 and is_position_blocked(x2,y2) == False:
                print("pos")
                return True

    for i in range(len(x_values)):
        if y1 == y2 and y1 == y_values[i]:
            if x2 < x1 and x2 < x_values[i] and is_position_blocked(x2,y2) == False:
                return True
            if x2 > x1 and x2 > x_values[i] and is_position_blocked(x2,y2) == False:
                return True

    return False



def create_random_obstacles():
    pass


def make_maze(w = 20, h = 40):
    
    #Make a list with inner lists amounting to h that contain 0's * width and the last element being 1 and the last list has 1's only
    vis = [[0] * w + [1] for element in range(h)] + [[1] * (w + 1)]
    print(vis)
    
    #Make a list with inner lists that have the the string "10" * width and the last element "1" and the final list being empty
    ver = [['10'] * w + ['1'] for element in range(h)] + [[]]
    print(ver)
    
    #Make a list with inner lists that have the the string "11" * width and the last element "1" for all the lists and an extra list
    hor = [['11'] * w + ['1'] for element in range(h + 1)]
    print(hor)
    

    def walk(x, y):

        vis[y][x] = 1
        #Directions
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '10'
            if yy == y: ver[y][max(x, xx)] = '00'
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    maze = []
    for (a, b) in zip(hor, ver):
        maze.append(''.join(a))
        maze.append(''.join(b))

    return maze