"""Robot moves in a Square"""
def move_square():
    size = 10
    print("Moving in a square of size "+str(size))
    move_forward_right(90, 10, 4)
    
    #for i in range(4):
    #    degrees = 90
    #    print("* Move Forward "+str(size))
    #    print("* Turn Right "+str(degrees)+" degrees")


"""Robot moves in a Rectangle"""
def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


"""Robot moves in a Circle"""
def move_circle():
    print("Moving in a circle")
    degrees = 1
    move_forward_right(1, 1, 360)
    
    #for i in range(360):
    #    length = 1
    #    print("* Move Forward "+str(length))
    #    print("* Turn Right "+str(degrees)+" degrees")


"""Robot moves in a Dancing Square Movement"""
def dance_square():
    size = 20
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        move_forward_right(90, 20, 4)
        
        #for j in range(4):
        #    degrees = 90
        #    print("* Move Forward " + str(size))
        #    print("* Turn Right " + str(degrees) + " degrees")


"""Robot moves in a cropped circle"""
def crop_circle():
    print("Crop circles - 4 circles")
    degrees = 1
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        move_forward_right(1, 1, 360)

        #for k in range(360):
        #    length = 1
        #    print("* Move Forward " + str(length))
        #    print("* Turn Right " + str(degrees) + " degrees")


""" This Function is to move forward and Right using the Parameters of a Shape"""
def move_forward_right(degrees, length, count):
    for i in range(count):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")



# TODO: Decompose into functions
""" The move Function could've been named move_robot to describe what the moving was for"""
def move():
    move_square()
    move_rectangle()
    move_circle()
    dance_square()
    crop_circle()

    """
    #Initial Code
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
    
    
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
    
    
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
    
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 10")
        for j in range(4):
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")
            degrees = 90

    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        for k in range(360):
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")
    """


"""This Function Starts  the Game"""
def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
