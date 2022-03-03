import random
import numpy as np

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
    user_name = input("Ahoy matey! Please enter your pirate name: ")
    print('')
    print(f"Welcome aboard Pirate {user_name}! There is trouble...The enemies have stolen our beloved rum and treasure! \nThey are scattered across the Black Sea. We must shoot our cannons and try to take their ships down. \nThey have cannons of their own so they will try to hit one of our ships too! \nThe sea board contains five by five squares in x,y coordinates. \nYou must guess the coordinates to take down their ships. The first to destroy all ships wins the rum and treasure! \nUs and the enemies both have a total of 5 ships to take down. \nAre you ready?")
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
        x = 0
        while x < 5:
            column = random.randint(1, 5)
            row = random.randint(1, 5)
            random_coordinates = [row, column]
            if random_coordinates == self.board_array:
                pass
            else:
                self.board_array[row, column] = '|O|'
                x += 1
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
        y_choice = input("Input letter coordinate (A to E): ")
        x_coord = int(input("Input number coordinate (1 to 5): "))
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
    #user_board.display_board()
    user_board.randomize_ship_coordinates()
    user_board.user_turn_place_hit()

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
