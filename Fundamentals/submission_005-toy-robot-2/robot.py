
def user_input_name():
    """Takes user input for robot name"""

    robot_name = input("What do you want to name your robot? ")

    if robot_name != "":
        return robot_name
    else:
        return user_input_name()


def greet_user(robot_name):
    """Greets User with specified name"""

    print(robot_name+":", "Hello kiddo!")


def user_input_command(robot_name):
    """Takes user input for command issued to robot"""

    user_command = input(robot_name+": What must I do next? ")

    return user_command


def commands_list(user_command, robot_name, position, coordinate):
    """List of commands for moving forward or back or sprinting
       These Commands then return a postion value"""

    user_list = user_command.split()

    try:
        if len(user_list) > 0 and len(user_list) < 3:

            if user_list[0].lower() == "forward" and len(user_list) == 2:
                return move_forward(user_list, robot_name, position, coordinate)

            elif user_list[0].lower() == "back" and len(user_list) == 2:
                return move_back(user_list, robot_name, position, coordinate)

            elif user_list[0].lower() == "sprint" and len(user_list) == 2:
                return sprint_range_check(user_list[0].lower(), int(user_list[1]), robot_name, position, coordinate)
                
            else:
                return robot_position(user_list, robot_name, position, coordinate)

    except ValueError:
        return robot_position(user_list, robot_name, position, coordinate)
    

def turn_robot_off(user_command, robot_name):
    """Function to turn robot off
       If True Robot breaks out of main while loop"""
    
    if user_command.lower() == "off":
        print(robot_name+":", "Shutting down..")
        return True
    else:
        return False


def move_forward(user_list, robot_name, position, coordinate):
    """Command to move forward Saves old position in case the new position
       is out of range then it will return the old position"""

    old_position = position.copy()
 
    new_position = robot_position(user_list, robot_name, position, coordinate)

    if int(new_position[0]) <= 100 and int(new_position[0]) >= -100 and int(new_position[1]) >= -200 and int(new_position[1]) <= 200:
        print(" > "+robot_name+" moved forward by "+str(user_list[1])+" steps.")
        return new_position

    else:
        print(robot_name+": Sorry, I cannot go outside my safe zone.")
        return old_position


def move_back(user_list, robot_name, position, coordinate):
    """Command to move back Saves old position in case the new position
       is out of range then it will return the old position"""

    old_position = position.copy()

    new_position = robot_position(user_list, robot_name, position, coordinate)

    if int(new_position[0]) <= 100 and int(new_position[0]) >= -100 and int(new_position[1]) >= -200 and int(new_position[1]) <= 200:
        print(" > "+robot_name+" moved back by "+user_list[1]+" steps.")
        return new_position
    else:
        print(robot_name+": Sorry, I cannot go outside my safe zone.")
        return old_position


def robot_coordinate(user_list, robot_name, coordinate):
    """List of robot coordinates:  
                0
                |
                |
          3-----|-----1
                |
                |
                2   """

    if coordinate == 0:
        if user_list.lower() == "right":
            print(" > "+robot_name+" turned right.")
            return 1
        elif user_list.lower() == "left":
            print(" > "+robot_name+" turned left.")
            return 3
        else:
            return 0

    elif coordinate == 1:
        if user_list.lower() == "right":
            print(" > "+robot_name+" turned right.")
            return 2
        elif user_list.lower() == "left":
            print(" > "+robot_name+" turned left.")
            return 0
        else:
            return 1 

    elif coordinate == 2:
        if user_list.lower() == "right":
            print(" > "+robot_name+" turned right.")
            return 3
        elif user_list.lower() == "left":
            print(" > "+robot_name+" turned left.")
            return 1
        else:
            return 2   

    elif coordinate == 3:
        if user_list.lower() == "right":
            print(" > "+robot_name+" turned right.")
            return 0
        elif user_list.lower() == "left":
            print(" > "+robot_name+" turned left.")
            return 2
        else:
            return 3       


def robot_position(user_list, robot_name, position,coordinate):
    """Determines the current robot position depending on the given coordinate and returns the position"""

    try:
        if len(user_list) > 0 and len(user_list) < 3:
            
            if coordinate == 0:

                if user_list[0].lower() == "forward" or user_list[0].lower() == "sprint":
                    position[1] = position[1] + int(user_list[1])

                elif user_list[0].lower() == "back":
                    position[1] = position[1] - int(user_list[1])
            
            if coordinate == 1:

                if user_list[0].lower() == "forward" or user_list[0].lower() == "sprint":
                    position[0] = position[0] + int(user_list[1])

                elif user_list[0].lower() == "back":
                    position[0] = position[0] - int(user_list[1])

            if coordinate == 2:

                if user_list[0].lower() == "forward" or user_list[0].lower() == "sprint":
                    position[1] = position[1] - int(user_list[1])

                elif user_list[0].lower() == "back":
                    position[1] = position[1] + int(user_list[1])
            

            if coordinate == 3:

                if user_list[0].lower() == "forward" or user_list[0].lower() == "sprint":
                    position[0] = position[0] - int(user_list[1])

                elif user_list[0].lower() == "back":
                    position[0] = position[0] + int(user_list[1])

            return position

    except ValueError:
        return None
        

def sprint_range_check(command, distance, robot_name, position, coordinate):
    """See if the sprint is in range if its in range it returns the new psosition
       otherwise it returns the old position"""

    old_position = position.copy()

    new_position = sprint_forward(command, distance, robot_name, position, coordinate)

    if int(new_position[0]) <= 100 and int(new_position[0]) >= -100 and int(new_position[1]) >= -200 and int(new_position[1]) <= 200:
        return new_position
    
    else:
        return old_position


def sprint_forward(command, distance, robot_name, position, coordinate):
    """Sprint recursive function to make the sprint command work decreasing from the specified number"""

    old_position = position.copy()

    user_list = [command, distance]

    new_position = move_forward(user_list, robot_name, position, coordinate)

    if distance == 1:
        return new_position

    else:
        return sprint_forward(command, distance-1, robot_name, position, coordinate)


def get_help(user_command):
    """Function to list help instructions"""

    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("FORWARD x - Moves robot forward a specified amount of steps, change x to steps")
    print("BACK x - Moves robot back a specified amount of steps, change x to steps")
    print("SPRINT x - Sprints robot forward a specified amount of steps, change x to steps")
    print("RIGHT - Moves robot right")
    print("LEFT - Moves robot left")
    print("")
        

def robot_start():
    """This is the entry function, do not change"""

    off_robot = False
    position = [0, 0]
    commands = ["forward", "back", "right", "left", "sprint"]

    coordinate = 0
    new_coordinate = 0

    robot_name = user_input_name()
    greet_user(robot_name)

    while off_robot != True:
        user_command = user_input_command(robot_name)
        user_list = user_command.split()

        try:
            if user_list[0].lower() in commands:

                if user_list[0].lower() == "right" or user_list[0].lower() == "left":

                    coordinate = robot_coordinate(user_command, robot_name, new_coordinate)
                    new_coordinate = coordinate

                position = commands_list(user_command, robot_name, position, new_coordinate)
                
                print(" > "+robot_name+" now at position "+"("+str(position[0])+","+str(position[1])+").")

            elif user_command.lower() == "help":
                get_help(user_command)

            elif user_command.lower() == "off":
                off_robot = turn_robot_off(user_command, robot_name)

            else:
                print(robot_name+": Sorry, I did not understand " +"'"+user_command+"'"+".")

        except IndexError and ValueError:
            print(robot_name+": Sorry, I did not understand " +"'"+user_command+"'"+".")


if __name__ == "__main__":
    robot_start()
