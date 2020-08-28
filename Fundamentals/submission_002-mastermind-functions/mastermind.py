import random


"""Get a random/secret code"""
def get_random_code():
    global code 
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value


"""Get user input"""
def get_user_input():
    global user_input
    user_input = input("Input 4 digit code: ")


"""Evaluate if guess is correct """
def is_code_correct():
    global iscorrect
    if correct_digits_and_position == 4:
        iscorrect = True
        print('Congratulations! You are a codebreaker!')
    else:
        iscorrect = False
        print('Turns left: '+str(12 - turns))


"""Evaluate the input agaisnt the secret code"""
def checking_result_and_print():

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    correct = False
    global turns
    turns = 0
    while not correct and turns < 12:
        get_user_input()
        answer = user_input
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        global  correct_digits_and_position
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        is_code_correct()
        correct = iscorrect
    print('The code was: '+str(code))    


# TODO: Decompose into functions
"""Run the game"""
def run_game():
    get_random_code()
    checking_result_and_print()

    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))
    """

if __name__ == "__main__":
    run_game()
