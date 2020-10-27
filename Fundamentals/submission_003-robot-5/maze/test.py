import time
import math
from random import shuffle, randrange
import turtle
import functools


PLAYGROUND_WIDTH= 200
PLAYGROUND_HEIGHT= 400
STRIDE = 10

def draw_square(pen, x, y, side, color):
    pen.pencolor(color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(side)
        pen.right(90)
    pen.end_fill()


def draw_maze(maze):
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-PLAYGROUND_WIDTH // 2, PLAYGROUND_HEIGHT // 2)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = 'black' if maze[row][col] == '1' else 'white'
            draw_square(
                pen,
                col * STRIDE - PLAYGROUND_WIDTH // 2,
                -row * STRIDE + PLAYGROUND_HEIGHT // 2,
                STRIDE,
                color
            )
    pen.hideturtle()


def make_maze(w = 20, h = 40):
    
    #Make a list with inner lists amounting to h that contain 0's * width and the last element being 1 and the last list has 1's only
    vis = [[0] * w + [1] for element in range(h)] + [[1] * (w + 1)]
    
    #Make a list with inner lists that have the the string "10" * width and the last element "1" and the final list being empty
    #"10" = "|  "
    ver = [['10'] * w + ['1'] for element in range(h)] + [[]]
    
    #Make a list with inner lists that have the the string "11" * width and the last element "1" for all the lists and an extra list
    #"11" = "+--"
    hor = [['11'] * w + ['1'] for element in range(h + 1)]
    

    def walk(x, y):

        vis[y][x] = 1

        #Directions
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '10' # "+  "
            if yy == y: ver[y][max(x, xx)] = '00' # "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    maze = []
    for (a, b) in zip(hor, ver):
        maze.append(''.join(a))
        maze.append(''.join(b))
    
    print(maze)
    return maze

maze = make_maze((PLAYGROUND_WIDTH // STRIDE) // 2, (PLAYGROUND_HEIGHT // STRIDE) // 2)


def is_free(x, y):
    result = 0 < x < len(maze) and 0 < y < len(maze[0]) and maze[y][x] == '0'
    return result


# Set up screen
window = turtle.Screen()
window.bgcolor('black')
window.tracer(0)


draw_maze(maze)
window.update()

window.mainloop()