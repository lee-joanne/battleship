import random
import numpy as np

instructions = """There is trouble...The enemies stole our treasure!
They are scattered across the Black Sea. 
We must shoot our cannons and try to take their ships down. 
They have cannons of their own so they will try to hit one of our ships too!
The sea board contains five by five squares in x,y coordinates. 
You must guess the coordinates to take down their ships. 
The first to destroy all ships wins the rum and treasure! 
Us and the enemies both have a total of 5 ships to take down."""

def introduce_game():
    '''
    Initial message to introduce title of the game.
    Input will appear for user to type in their name.
    Paragraph will appear to explain rules of the game
    and ask user if they wish to continue.
    '''
    print('-' * 80)
    print('')
    print("Welcome to Pirate Ship!")
    print('')
    print('-' * 80)
    print('')
    user_name = input("Ahoy matey! Please enter your pirate name: ")
    print('')
    print(f"Welcome aboard Pirate {user_name}!")
    print(instructions)
    print('')
    print(f"Are you ready, Pirate {user_name}?")
    print('')

def ask_user_ready():
    '''
    Asks the user if they are ready to play the game or not.
    Loops the response if invalid response is given.
    '''
    while True:
        confirmation_response = input("aye or nay? ")

        if confirmation_response == 'aye':
            start_game()
            break
        elif confirmation_response == 'nay':
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
        self.board = [
            [" ",  " A", "  B", "  C", "  D", "  E"],
            ["1", "| |", "| |", "| |", "| |", "| |"],
            ["2", "| |", "| |", "| |", "| |", "| |"],
            ["3", "| |", "| |", "| |", "| |", "| |"],
            ["4", "| |", "| |", "| |", "| |", "| |"],
            ["5", "| |", "| |", "| |", "| |", "| |"],
        ]
        self.board_array = np.array(self.board)

    def display_board(self):
        '''
        Will display the board to the user.
        '''
        print("The board")
        for row in self.board:
            joint_row = "  ".join(row)
            print(f"{joint_row}\n")

    def randomize_ship_coordinates(self):
        '''
        Function will randomly create coordinates on where to place the ships.
        Function will place the ships, marked as |O|.
        '''
        count = 0
        while count < 5:
            column = random.randint(1, 5)
            row = random.randint(1, 5)
            if self.board_array[row, column] == '|O|':
                pass
            else:
                self.board_array[row, column] = '|O|'
                count += 1
        print(self.board_array)

    def user_turn_place_hit(self):
        '''
        Function will allow user to type in coordinates
        to place hit.
        Will give message back to user depending on
        hit or miss. Increments miss_count if
        user misses and calls computer's turn.
        Allows user to play again if hit.
        '''
        list_of_ship_coord = list(zip(*np.where(self.board_array == '|O|')))
        try:
            y_choice = input("Input letter coordinate in capitals (A to E): ")
            y_lst = ['A', 'B', 'C', 'D', 'E']
            if y_choice not in y_lst:
                raise ValueError(
                    f"Value must be a capital letter from A to E! You typed {y_choice}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

        try:
            x_coord = int(input("Input number coordinate (1 to 5):: "))
            x_lst = [1, 2, 3, 4, 5]
            if x_coord not in x_lst:
                raise ValueError(
                    f"Value must be a letter between 1 to 5! You typed {x_coord}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            
        column_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
        y_coord = column_map[y_choice]
        shot = (x_coord, y_coord)
        miss_count = 0
        for item in list_of_ship_coord:
            if item == shot:
                self.board_array[x_coord, y_coord] = '|X|'
                print('You hit a battleship! Take another turn.')
                break
            else:
                self.board_array[x_coord, y_coord] = '|-|'
                miss_count += 1
                if miss_count == len(list_of_ship_coord):
                    print("You missed!")
                else:
                    pass
        print(self.board_array)

def start_game():
    '''
    Function will start the game when user confirms game start.
    '''
    user_board = GameBoard("name=user")
    computer_board = GameBoard("name=computer")
    #user_board.display_board()
    user_board.randomize_ship_coordinates()
    computer_board.randomize_ship_coordinates()
    computer_board.user_turn_place_hit()


def end_game():
    '''
    When user chooses to end game, will create a goodbye message
    and give instructions to let the user know how to reactive the game.
    '''
    print("Goodbye! To play again, please click 'Run Program'!")

def main():
    '''
    Main code to execute the entire Python script
    '''
    introduce_game()
    ask_user_ready()

main()
