import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    problem = ["1", "2", "3", "4", "5", "6", "7", "8"]
    code = []
    i = 0
    strproblem = "".join(problem)

    while i <= 3:
        random_num = random.randint(1, len(problem))
        random_num_index = random_num - 1
        if problem[random_num_index] not in code:
            code.append(problem[random_num_index])
            i = i + 1

    strcode = "".join(code)
    #print(strcode)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    turns = 12
    while turns > 0:
        guess = input("Input 4 digit code: ")
        guess = guess.lower()

        correct_digits_place = 0
        correct_digits = 0

        if len(guess) != 4:
            print("Please enter exactly 4 digits.")

        elif guess.find("0") != -1 or guess.find("9") != -1:
            print("Please enter exactly 4 digits.")

        elif guess.islower() == True:
            print("Please enter exactly 4 digits.")
            
        elif guess == strcode:
            print("Number of correct digits in correct place:",  " " * 3, (correct_digits_place) + len(guess))
            print("Number of correct digits not in correct place:", correct_digits)
            print("Congratulations! You are a codebreaker!")
            print("The code was: "+strcode)
            break
        
        else:
            for i in range(0, len(guess)):
                if guess[i] == strcode[i]:
                    correct_digits_place = correct_digits_place + 1
            print("Number of correct digits in correct place:",  " " * 3, correct_digits_place)

            for j in range(0, len(guess)):
                if guess[j] in strcode and guess[j] != strcode[j]:
                    correct_digits = correct_digits + 1
            print("Number of correct digits not in correct place:", correct_digits)
            turns = turns - 1
            print("Turns left: "+str(turns))

    pass

if __name__ == "__main__":
    run_game()
