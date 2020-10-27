#Please use random.randint to get a random word from the list
import random

def read_file(file_name):
    
    #Step 1 - open file and read lines as words.
    
    #open file and read.
    file = open(file_name,'r')

    #save file contents as a list
    list = file.readlines()
    file.close()
    #return the list
    return list
    

def select_random_word(words):

    #Step 2 = select random word from list of file
    
    #find a random word by getting the length and finding a random number, 
    #minus the length by one because arrays/lists start from 0.
    lengthwords = len(words) - 1
    randomword = random.randint(0, lengthwords)

    #make words[0] the random word.
    words[0] = words[randomword].strip()

    #find a random letter in word[0] by getting the length and finding a random rumber,
    #minus length by one because arrays/lists start from 0
    lengthletters= len(words[0]) - 1
    randomletter = random.randint(0, lengthletters)

    #Print all letters just before the randomletter number. 
    #Add an underscore.
    #Print all letters after randomletter 
    print('Guess the word: ' + words[0][:randomletter] + "_" + words[0][randomletter+1:])

    return words[0]

def get_user_input():

    #Get user input for answer

    return input('Guess the missing letter: ')

def run_game(file_name):

    #This is the main game code. You can leave it as is and only implement Steps 1 to 3 indicated above

    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print("The word was: " +word)

if __name__ == "__main__":
    run_game('short_words.txt')