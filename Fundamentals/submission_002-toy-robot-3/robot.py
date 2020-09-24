# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent']
valid_second_command = ['silent', 'reversed', 'reversed silent']
valid_third_command = ["silent"]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """

    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''

def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    silent_steps = []
    (command_name, arg1) = split_command_input(command)
    silent_steps = arg1.split()
    silent_step = split("- ", arg1)
    #print(silent_step)

    if len(silent_steps) >= 0 and len(silent_steps) < 2 and len(silent_step) != 2:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or arg1.lower() in valid_second_command)

    elif len(silent_step) == 2 and is_int(silent_step[0]) == True and is_int(silent_step[1]) == True:
        return command_name.lower() in valid_commands and (is_int(silent_step[0]) == True and is_int(silent_step[1]) == True)

    elif len(silent_steps) == 2 and is_int(silent_steps[1]):
        return command_name.lower() in valid_commands and (is_int(silent_steps[1]) and silent_steps[0].lower() in valid_second_command)

    elif len(silent_steps) == 2 and is_int(silent_steps[0]):
        return command_name.lower() in valid_commands and (is_int(silent_steps[0]) and silent_steps[1].lower() in valid_second_command)
    
    elif len(silent_steps) == 2:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or arg1.lower() in valid_second_command)

    elif len(silent_step) == 3 and is_int(silent_step[1]) == True and is_int(silent_step[2]) == True: 
        return command_name.lower() in valid_commands and (silent_step[0].lower in valid_second_command and is_int(silent_step[1]) == True and is_int(silent_step[2]) == True)  

    elif len(silent_steps) == 3 and is_int(silent_steps[0]):
        return command_name.lower() in valid_commands and (is_int(silent_steps[0]) and silent_steps[1].lower() in valid_second_command and silent_steps[2].lower() in valid_third_command)

    elif len(silent_steps) == 3 and is_int(silent_steps[2]):
        return command_name.lower() in valid_commands and (is_int(silent_steps[2]) and silent_steps[0].lower() in valid_second_command and silent_steps[1].lower() in valid_third_command)

def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays commands previously done
REPLAY SILENT - replays commands done silently
REPLAY REVERSED - replays commands in reverse order
REPLAY REVERSED SILENT - replays commands in reverse order silently
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command, command_list, silent):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)
    user_list = command.split()
    #print(user_list)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    
    if len(user_list) == 1 and command_name == "replay":
        if command_name == 'replay':
            (do_next, command_output) = do_replay(robot_name, command_list, silent, user_list)
    if len(user_list) == 2 and command_name == "replay":
        if command_name == 'replay' and is_int(user_list[1]):
            (do_next, command_output) = do_replay(robot_name, command_list, silent, user_list)
        elif command_name == 'replay' and "-" in user_list[1]:
            (do_next, command_output) = do_replay(robot_name, command_list, silent, user_list)
        elif command_name == "replay" and arg == "silent":
            (do_next, command_output, silent) = do_replay_silent(robot_name, command_list, silent, user_list)
        elif command_name == "replay" and arg == "reversed":
            (do_next, command_output) = do_replay_reversed(robot_name, command_list, silent, user_list)
    if len(user_list) == 3 and command_name == "replay":
        if user_list[0] == "replay" and user_list[1] == "silent" and is_int(user_list[2]):
            (do_next, command_output, silent) = do_replay_silent(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[2] == "silent" and is_int(user_list[1]):
            (do_next, command_output, silent) = do_replay_silent(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[1] == "reversed" and is_int(user_list[2]):
            (do_next, command_output) = do_replay_reversed(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[2] == "reversed" and is_int(user_list[1]):
            (do_next, command_output) = do_replay_reversed(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[1] == "reversed" and user_list[2] == "silent":
            (do_next, command_output, silent) = do_replay_reversed_silent(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[1] == "reversed" and user_list[2] == "silent" and is_int(user_list[3]):
            (do_next, command_output, silent) = do_replay_reversed_silent(robot_name, command_list, silent, user_list)
        elif user_list[0] == "replay" and user_list[2] == "reversed" and user_list[3] == "silent" and is_int(user_list[1]):
            (do_next, command_output, silent) = do_replay_reversed_silent(robot_name, command_list, silent, user_list)

    if silent == False:
        print(command_output)
        show_position(robot_name)

    return do_next


def store_commands(command_list, command):
    """stores commands"""

    command_list.append(command)
    filtered_list = list(filter(lambda x: x != "help" and x != "replay" and x != "replay silent" 
                        and x != "replay reversed" and x != "replay reversed silent", command_list))
    final_list = [x for x in filtered_list if 'replay' not in x]


    return final_list


def do_replay(robot_name, command_list, silent, user_list):
    """replays commands"""



    if len(user_list) == 1:
        [handle_command(robot_name, command, command_list, silent) for command in command_list]
        return True, ' > '+robot_name+' replayed '+str(len(command_list))+' commands.'

    if len(user_list) == 2 and '-' not in user_list[1]:
        position = len(command_list) - int(user_list[1])
        [handle_command(robot_name, command_list[i], command_list, silent) for i in range(position, len(command_list))]
        return True, ' > '+robot_name+' replayed '+str(user_list[1])+' commands.'

    if len(user_list) == 2 and '-' in user_list[1]:
        range_number = split("-", user_list[1])
        [handle_command(robot_name, command_list[i], command_list, silent) for i in range(int(range_number[1])-1, int(range_number[0])-1)]
        return True, ' > '+robot_name+' replayed '+str(len(range_number))+' commands.'
    


def do_replay_silent(robot_name, command_list, silent, user_list):
    """replays commands silently"""

    if len(user_list) == 2:
        [handle_command(robot_name, command, command_list, True) for command in command_list]
        return True, ' > '+robot_name+' replayed '+str(len(command_list))+' commands silently.', False

    if len(user_list) == 3 and is_int(user_list[1]):
        position = len(command_list) - int(user_list[1])
        [handle_command(robot_name, command_list[i], command_list, True) for i in range(position, len(command_list))]
        return True, ' > '+robot_name+' replayed '+str(user_list[1])+' commands silently.', False

    if len(user_list) == 3 and is_int(user_list[2]):
        position = len(command_list) - int(user_list[2])
        [handle_command(robot_name, command_list[i], command_list, True) for i in range(position, len(command_list))]
        return True, ' > '+robot_name+' replayed '+str(user_list[2])+' commands silently.', False

    if len(user_list) == 3 and '-' in user_list[2]:
        range_number = split("-", user_list[1])
        [handle_command(robot_name, command_list[i], command_list, True) for i in range(int(range_number[1])-1, int(range_number[0])-1)]
        return True, ' > '+robot_name+' replayed '+str(len(range_number))+' commands.'


def do_replay_reversed(robot_name, command_list, silent, user_list):
    """replays commands reversed"""
    
    if len(user_list) == 2:
        [handle_command(robot_name, command, command_list, silent) for command in reversed(command_list)]
        return True, ' > '+robot_name+' replayed '+str(len(command_list))+' commands in reverse.'

    if len(user_list) == 3 and is_int(user_list[1]):
        position = len(command_list) - int(user_list[1])
        [handle_command(robot_name, command_list[i], command_list, silent) for i in range(position, 0-1, -1)]
        return True, ' > '+robot_name+' replayed '+str(user_list[1])+' commands in reverse.'

    if len(user_list) == 3 and is_int(user_list[2]):
        position = len(command_list) - int(user_list[2])
        [handle_command(robot_name, command_list[i], command_list, silent) for i in range((len(command_list)-1), (position-1), -1)]
        return True, ' > '+robot_name+' replayed '+str(user_list[2])+' commands in reverse.'


def do_replay_reversed_silent(robot_name, command_list, silent, user_list):
    """replays commands reversed silently"""
    
    if len(user_list) == 3:
        [handle_command(robot_name, command, command_list, True) for command in reversed(command_list)]
        return True, ' > '+robot_name+' replayed '+str(len(command_list))+' commands in reverse silently.', False

    if len(user_list) == 4 and is_int(user_list[1]):
        position = len(command_list) - int(user_list[1])
        [handle_command(robot_name, command_list[i], command_list, True) for i in range(position, 0-1, -1)]
        return True, ' > '+robot_name+' replayed '+str(user_list[1])+' commands in reverse silently.', False

    if len(user_list) == 4 and is_int(user_list[3]):
        position = len(command_list) - int(user_list[3])
        [handle_command(robot_name, command_list[i], command_list, True) for i in range((len(command_list)-1), (position-1), -1)]
        return True, ' > '+robot_name+' replayed '+str(user_list[3])+' commands in reverse silently.', False


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index
    command_list = []
    silent = False

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    command_list = []

    command = get_command(robot_name)

    while handle_command(robot_name, command, command_list, silent):
        command_list = store_commands(command_list, command)
        command = get_command(robot_name)



    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
