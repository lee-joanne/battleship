import random

def introduce_game():
    '''
    Initial message to introduce title of the game.
    Input will appear for user to type in their name.
    Paragraph will appear to explain rules of the game and ask user if they wish to continue.
    '''
    print('-' * 80)
    print('')
    print("Welcome to Pirate Ship!")
    print('')
    print('-' * 80)
    user_name = input("Ahoy matey! Please enter your pirate name: ")
    print('')
    print(f"Welcome aboard Pirate {user_name}! There is trouble...The enemies have stolen our beloved rum and treasure! \nThey are scattered across the Black Sea. We must shoot our cannons and try to take their ships down. \nThey have cannons of their own so they will try to hit one of our ships too! \nWe are lucky to have you Pirate {user_name}. \nThe sea board contains five by five squares in x,y coordinates. \nYou must guess the coordinates to take down their ships. The first to destroy all ships wins the rum and treasure! \nUs and the enemies both have a total of 5 ships to take down. \nAre you ready?")
    print('')

def ask_user_ready():
    '''
    Asks the user if they are ready to play the game or not. Loops the response if invalid response is given.
    '''
    while True:
        confirmation_response = input("aye or nay? ")

        if (confirmation_response == 'aye'):
            print("You chose aye!")
            break
        elif (confirmation_response == 'nay'):
            print('you chose nay!')
            break
        else:
            print("You must type either 'aye' or 'nay'!")

class GameBoard:
    '''
    Creates the game boards class used in the Pirate Ship game.
    '''
    def __init__(self, name):
        self.name = name
        self.num_ships = 5
        self.guesses = []
        self.ships = []
    
    def convert_letters_to_numbers():
        letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        return letters_to_numbers
    
def build_board():
    print("      A    B    C    D    E    F")
    print("      -----------------------------")
    row_board = [0, "| |, | |, | |, | |, | |, | |"]
    for i in range(5):
        row_board[0] += 1
        print(row_board)

def main():
    introduce_game()
    ask_user_ready()

#main()
build_board()