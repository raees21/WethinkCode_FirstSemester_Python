import random
​
print("{} Loaded crazy_maze.".format(robot_name))
​
'''Initialises empty lists to hold coords of obstacles'''
obstacl_ = []
obstacl = []
block_axis = [(-100,-5),(95,-5)]
​
count = 40
while count > 0 :
    obstacl_.append([])
    count -= 1
​
def get_columns(obstacl):
    '''Generates a list of obstacles in the Y-direction'''
    for i in range(25):
        x = random.randrange(-100, 95, 5)
        y = random.randrange(-200, 195, 5)
        obstacl.append((x,y))
​
    return obstacl    
​
def get_obstacles():
    global obstacl, obstacl_
    '''Generates a list of obstacles by rows'''
    y = 200
    for i in obstacl_:
        x = -100
        y -= 10
        for a in range(40):
            i.append((x,y))
            x += 5
​
        #Removes obstacles at random
        for b in range(5):
            pop_ob = random.randint(1,len(i) - 1)
            i.remove(i[pop_ob])
        
    for i in obstacl_:
        for a in i:
            obstacl.append(a)
​
    get_columns(obstacl)
    obstacl = obstacl + block_axis 
    return list(obstacl)
​
​
def is_position_blocked(x, y):
    global obstacl
    
    for o in obstacl:
        if ((x <= o[0] + 4) and (x >= o[0])) and ((y <= o[1] + 4) and (y >= o[1])):
            return True
    return False        
​
​
def is_path_blocked(x1, y1, x2, y2):
​
    '''sx = step x , xx = x multiplier, sy = step y , yy = y multiplier
       added them to account for when the values are in the negative range'''
​
    sx, xx = 1, 1
​
    if x2 < x1 :
        sx *= -1
        xx *= -1
​
    sy, yy = 1, 1
​
    if y2 < y1:
        sy *= -1
        yy *= -1    
    
    for a in range(x1, x2 + xx, sx):
        for b in range(y1, y2 + yy, sy):
            if is_position_blocked(a,b):
                return True
    return False   