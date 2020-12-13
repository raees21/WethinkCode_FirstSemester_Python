obstacles = []
def get_obstacles():
    global obstacles
    maze = [
        "  XXX         XXXXXXXXXXX",
        "                        X",
        "X  XXXXXXX      XXXXXX  X",
        "X                    X  X",
        "X  X XXXXXX  XXXXXX  X  X",
        "X  X       XX     X  X  X",
        "X  X              X  X  X",
        "X  X  XXXXX  XXXXXX  X  X",
        "X  X  X           X  X  X",
        "X  X  X           X  X  X",
        "   X  X           X  X   ",
        "   X  X           X  X   ",
        "X     XXXX        X  X  X",
        "X        X      X  X  X  ",
        "X     X           X  X  X",
        "X  X  X           X  X  X",
        "X  X  X     X      X  X  X",
        "XXXX  X     X     X XXXXX",
        "X  X  X     X     X  X  X",   
        "X  X  X     X      X  X  X",
        "X  X  X     X     X  X XX",
        "X  X  X     X      X  X  ",
        "X  XXXXXXXXXXXXXXX  X  XX",
        "X                       X",
        "XXXXXXXXXXX  XXXXXXXXXXXX"
        ]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char = maze[y][x]
            x_axis = -96 + (x * 8)
            y_axis = 196 - (y * 16)
            if char == 'X':
                obstacles.append((x_axis,y_axis))
                obstacles.append((x_axis - 4, y_axis))
                obstacles.append((x_axis, y_axis -4))
                obstacles.append((x_axis - 4, y_axis -4))
                obstacles.append((x_axis, y_axis -8))
                obstacles.append((x_axis -4, y_axis -8))
                obstacles.append((x_axis -4, y_axis -12))
                obstacles.append((x_axis , y_axis -12))       
    return obstacles