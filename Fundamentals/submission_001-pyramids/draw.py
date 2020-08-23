

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    str = input("Shape?: ")
    str = str.lower()
    if str == 'pyramid':
        return str
    elif str == "triangle":
        return str
    elif str == "square":
        return str
    elif str == "rhombus":
        return str
    elif str == "rectangle":
        return str
    elif str == "trapezium":
        return str
    else:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    try:
        height = int(input("Height?: "))

        if height > 80 or height < 0 :
            return get_height()
        else:
            return height

    except ValueError:
        return get_height()

# TODO: Step 2
def draw_pyramid(height, outline):
    
    if outline == False:
        for rows in range(0, height):
            print(" " * (height-rows-1) + "*" * (rows*2+1))

    elif outline == True:
        for rows in range(1, height+1):
            if rows == 1:
                print(" " * (height-1) + "*")
            elif rows == height:
                print("*" * (height*2-1))
            else:
                print(" " * (height-rows) + "*" + " " * (rows*2-3) + "*")


# TODO: Step 3
def draw_square(height, outline):
    
    if outline == False:
        for rows in range(0, height):
            print("*" * (height))

    if outline == True:
        for rows in range(1, height+1):
            if rows==height or rows==1:
                print("*" * (height))
            else:
                print("*"  + " " * (height-2) + "*")
        
    
    
# TODO: Step 4
def draw_triangle(height, outline):
    
    if outline == False:
        for rows in range(0, height):
            print("*" * (rows+1))

    if outline == True:
        for rows in range(1, height+1):
            if rows==height:
                print("*" * (height))
            elif rows==1:
                print("*")
            else:
                print("*"  + " " * (rows-2) + "*")


def draw_rhombus(height, outline):
    if outline == False:
        for rows in range(0, height):
            print(" " * (height-rows-1) + "*" * (height))

    if outline == True:
        for row in range(1, height):
            if row == 1:
                print(" " * (height-1) + "*" * height)
            if row == height-1:
                print("*" * (height))
            else:
                print(" " * (height-row-1) + "*" + " " * (height-2) + "*")


def draw_rectangle(height, outline):
    if outline == False:
        for i in range(0, height):
            print("*" * (height*4))
    
    if outline == True:
        for i in range(0, height):
            if i == 0:
                print("*" * (height*4))
            if i == height-1:
                print("*" * (height*4))
            else:
                print("*" + " " * ((height*4)-2) + "*")

def draw_trapezium(height, outline):
    if outline == False:
        for row in range(0, height):
            print("*" * (height) + "*" * (row+1))

    if outline == True:

        for row in range(0, height-1):
            if row == 0:
                print("*" * (height) + "*" * (row+1))
            if row == height-2:
                print("*" * (height) + "*" * (row+1))
            else:
                print("*" + " " * (height) + " " * (row)
                + "*")


    


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "rhombus": 
        draw_rhombus(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "trapezium":
        draw_trapezium(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline = input("Outline only? (y/N): ")
    
    if outline == "y" or outline == "Y":
        return True
    elif outline == "n" or outline == "N":
        return False
    


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

