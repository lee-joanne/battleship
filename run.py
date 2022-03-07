import random
import numpy as np

instructions = """There is trouble...The enemies stole our treasure!
They are scattered across the Black Sea.
We must shoot our cannons and try to take their ships down.
They have cannons of their own so they will try to hit one of our ships too!
The sea board contains five by five squares in x,y coordinates.
You must guess the coordinates to take down their ships.
The first to destroy all ships wins the rum and treasure!
Us and the enemies both have a total of 5 ships to take down.

On your grid, your ships are marked as '|O|'. If a ship is
hit, it will be marked as '|X|'. If it's a miss, it will be marked
as '|-|'."""


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
    global user_name
    user_name = input("Ahoy matey! Please enter your pirate name:\n")
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
        confirmation_response = input("aye or nay?\n").lower()

        if confirmation_response == 'aye':
            start_game()
            break
        elif confirmation_response == 'nay':
            end_game()
            break
        else:
            print('')
            print("You must type either 'aye' or 'nay'!")
            print('')


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
        self.user_score = 0
        self.computer_score = 0
        self.column_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

    # Code credit on display_board(self) goes to Damian Jacob
    # https://github.com/Damianjacob/MS3-Battleship-Game
    def display_board(self):
        '''
        Will display the board to the user with respective
        labels on top.
        '''
        if self.name == computer_board.name:
            print("\nEnemy Board\n")
        else:
            print(f"\n {user_name}'s Board:\n")
        for row in self.board_array:
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
                continue
            else:
                self.board_array[row, column] = '|O|'
                count += 1
        self.display_board()

    def validate_y_coordinate(self):
        '''
        Function will validate whether input from user
        is a letter ranging from a to e, or else will
        return ValueError message.
        '''
        while True:
            try:
                print('')
                y_choice = input("Input letter coordinate (A to E):\n").upper()
                y_lst = ['A', 'B', 'C', 'D', 'E']
                if y_choice not in y_lst:
                    raise ValueError(
                        "Value must be a capital letter from A to E!")
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                continue
            else:
                break
        return y_choice

    def validate_x_coordinate(self):
        '''
        Function will validate whether input from user
        is a number ranging from 1 to 5, or else will
        return ValueError message.
        '''
        while True:
            try:
                x_coord = (input("Input number coordinate (1 to 5):\n"))
                x_lst = ["1", "2", "3", "4", "5"]
                if x_coord not in x_lst:
                    raise ValueError(
                        "Value must be a letter between 1 to 5!")
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                continue
            else:
                break
        return x_coord

    def ask_user_start(self):
        '''
        Function will ask user if they wish to place their own ships.
        If n, ship coordinates will be randomized.
        If yes, function will run to ask user to input desired coordinates."
        '''
        print('')
        while True:
            print("Would you like to place the ships yourself?")
            user_answer = input("y or n?:\n").lower()
            if user_answer == 'y':
                user_board.user_choose_ship_placement()
                break
            elif user_answer == 'n':
                user_board.randomize_ship_coordinates()
                computer_board.randomize_ship_coordinates()
                coin_toss(user_board, computer_board)
                break
            else:
                print('')
                print("You must type either 'y' or 'n'!")
                print('')

    def user_choose_ship_placement(self):
        '''
        Function will allow the user to type in their own
        desired coordinates.
        '''
        user_board.display_board()
        ship_count = 0
        while ship_count < 5:
            while True:
                y = self.column_map[input("Choose letter (A to E):\n").upper()]
                x = int(input("Choose number (1 to 5):\n"))
                y_lst = ['A', 'B', 'C', 'D', 'E']
                x_lst = [1, 2, 3, 4, 5]
                if y not in y_lst:
                    print("You must select a letter from A to E!")
                elif x not in x_lst:
                    print("You must select a number from 1 to 5!")
                else:
                    break
            self.board_array[x, y] = '|O|'
            ship_count += 1
            user_board.display_board()
            if ship_count == 5:
                print('')
                print('Great job placing the ships!')
                print('')
                print(f"Are you happy with the ships, Pirate {user_name}?")
                user_answer = input('y or n:\n').lower()
                if user_answer == 'y':
                    print('')
                    user_board.display_board()
                    computer_board.randomize_ship_coordinates()
                    coin_toss(user_board, computer_board)
                    break
                elif user_answer == 'n':
                    continue
                else:
                    print('')
                    print("You must type either 'y' or 'n'!")
                    print('')

    def user_turn_place_hit(self):
        '''
        Function will allow user to type in coordinates
        to place hit.
        Will give message back to user depending on
        hit or miss. Increments miss_count if
        user misses and calls computer's turn.
        Allows user to play again   if hit.
        '''
        while True:
            y_coord = self.column_map[self.validate_y_coordinate()]
            x_coord = int(self.validate_x_coordinate())
            if self.board_array[x_coord, y_coord] == '|O|':
                self.board_array[x_coord, y_coord] = '|X|'
                print('')
                print(f'You hit a battleship! Great job Pirate {user_name}!')
                print('')
                self.user_score += 1
                break
            elif self.board_array[x_coord, y_coord] == '|X|':
                print('')
                print("You already hit here! Try again!")
            elif self.board_array[x_coord, y_coord] == '|-|':
                print('')
                print("You already hit here! Try again!")
            else:
                self.board_array[x_coord, y_coord] = '|-|'
                print('')
                print("You missed!")
                print('')
                break
        self.display_board()
        user_board.computer_turn_place_hit()
        
        
    def computer_turn_place_hit(self):
        '''
        When it is the computer's turn, automatically will
        generate a coordinate and direct a hit at the
        user board.
        '''
        print('')
        print("Enemy's turn...")
        while True:
            y_target = random.randint(1, 5)
            x_target = random.randint(1, 5)
            if self.board_array[x_target, y_target] == '|X|':
                continue
            elif self.board_array[x_target, y_target] == '|-|':
                continue
            elif self.board_array[x_target, y_target] == '|O|':
                self.board_array[x_target, y_target] = '|X|'
                print('')
                print('Oh no! The enemy has hit a ship!')
                self.computer_score += 1
                print("computer score increases")
                print('')
                break
            else:
                self.board_array[x_target, y_target] = '|-|'
                print('')
                print("The enemy missed!")
                print('')
                break
        self.display_board()
        print('')
        print("Take a hit at the enemy's board!")
        print('')
        computer_board.display_board()


    def iterate_user_score(self):
        while True:
            computer_board.user_turn_place_hit()
            if (computer_board.user_score) == 5:
                computer_board.user_wins()
                break
            elif (user_board.computer_score) == 5:
                user_board.computer_wins()
                break
            else:
                pass
    #     '''
    #     Function allow the keep to continuously run until
    #     user scores 5 points. Function will
    #     keep track of incrementing score.
    #     '''

    #     while(self.user_score) < 6:
    #         self.user_turn_place_hit()
    #         if (self.user_score) == 5:
    #             self.user_wins()

    # def iterate_computer_score(self):
    #     '''
    #     Function allow the keep to continuously run until
    #     computer scores 5 points. Function will
    #     keep track of incrementing score.
    #     '''

    #     while(self.computer_score) < 6:
    #         print("computer score less than 5")
    #         self.computer_turn_place_hit()
    #         if (self.computer_score) == 2:
    #           self.computer_wins()

    def user_wins(self):
        '''
        Function will congratulate user for winning when
        user score reaches 5 points.
        '''
        print('')
        print(f"Congratulations Pirate {user_name} You have beat the enemy!")
        print("We have claimed back our beloved treasure! Great job!")
        print("To play again, hit the 'Run Program' button at the top!")

    def computer_wins(self):
        '''
        Function will let user know they have lost the game
        when computer reaches 5 points.
        '''
        print('')
        print(f"Oh no Pirate {user_name}, the enemy has won...")
        print("Our beloved treasure has been claimed back and our ships sunk.")
        print("Better luck next time.")
        print("To play again, click 'Run Program' at the top!")


def coin_toss(user_board, computer_board):
    '''
    Function will do a coin toss to see
    if the user or computer goes first.
    '''
    print('')
    print('A coin toss will be done to see who goes first...')
    print('')
    if random.randint(1, 100) % 2 == 0:
        print("You won the coin toss! You go first.")
        print('')
        print("Take a hit at the enemy's board!")
        print('')
        computer_board.display_board()
        return computer_board.user_turn_place_hit()
    else:
        print("You lost the coin toss, computer goes first!")
        return user_board.computer_turn_place_hit()
    play_game = coin_toss(user_board, computer_board)
    play_game()


def start_game():
    '''
    Function will start the game when user confirms game start.
    '''
    global user_board
    global computer_board
    user_board = GameBoard("name=user")
    computer_board = GameBoard("name=computer")
    user_board.ask_user_start()
    computer_board.iterate_user_score()
    # user_board.iterate_computer_score()


def end_game():
    '''
    When user chooses to end game, will create a goodbye message
    and give instructions to let the user know how to reactive the game.
    '''
    print('')
    print("Goodbye! To play again, please click 'Run Program'!")


def main():
    '''
    Main code to execute the entire Python script
    '''
    introduce_game()
    ask_user_ready()


main()
