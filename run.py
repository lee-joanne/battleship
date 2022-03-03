import random
import numpy as np

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
            start_game()
            break
        elif (confirmation_response == 'nay'):
            end_game()
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
        self.user_board = []
        self.coordinates = []
        self.computer_board = [
            [" ",  " A", "  B", "  C", "  D", "  E"],
            ["1", "| |", "| |", "| |", "| |", "| |"],
            ["2", "| |", "| |", "| |", "| |", "| |"],
            ["3", "| |", "| |", "| |", "| |", "| |"],
            ["4", "| |", "| |", "| |", "| |", "| |"],
            ["5", "| |", "| |", "| |", "| |", "| |"],
        ]

    def display_board(self):
        '''
        Will display the board to the user.
        '''
        print("The board")
        for row in board:
            joint_row = "  ".join(row)
            print(f"{joint_row}\n")

    def convert_row_to_number(self):
        '''
        Converts the string rows into integers.
        '''
        converted_row = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return converted_row

    def create_random_user_board(self):
        """
        needs to be done
        """
        self.user_board = [
            [" ",  " A", "  B", "  C", "  D", "  E"],
            ["1", "| |", "| |", "| |", "| |", "| |"],
            ["2", "| |", "| |", "| |", "| |", "| |"],
            ["3", "| |", "| |", "| |", "| |", "| |"],
            ["4", "| |", "| |", "| |", "| |", "| |"],
            ["5", "| |", "| |", "| |", "| |", "| |"],
        ]
        return self.randomize_ship_coordinates()

    def randomize_ship_coordinates(self):
        '''
        Function will randomly create coordinates on where to place the ships.
        '''
        board_rows = ["A", "B", "C", "D", "E"]
        board_columns = [1, 2, 3, 4, 5]

        current_ships_deployed: int = 0
        while current_ships_deployed < 5:
            rows = random.choice(board_rows)
            columns = random.choice(board_columns)
            converted_row = self.convert_row_to_number(rows)
            random_coordinates = [columns, converted_row]
            if random_coordinates not in self.coordinates:
                self.coordinates.append(random_coordinates)
                self.user_board[converted_row][columns] = "|X|"
                current_ships_deployed += 1

def start_game():
    game_board = GameBoard(name="user")
    game_board.create_random_user_board()

def end_game():
    '''
    When user chooses to end game, will create a goodbye message and give instructions to let the user know how to reactive the game.
    '''
    print("Goodbye! To play again, please click 'Run Program'!")

def main():
    '''
    Main code to execute the entire Python script
    '''
    introduce_game()
    ask_user_ready()

main()