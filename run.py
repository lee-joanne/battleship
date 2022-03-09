import random
import numpy as np

user_instructions = """There is trouble...The enemy stole our treasure!
The enemy has five ships scattered across the Black Sea.
We must shoot our cannons and try to take their ships down.
They have cannons of their own so they will try to hit one of our ships too!
The sea board contains five by five squares in x,y coordinates.
You must guess the coordinates to take down their ships.
The first to destroy all 5 ships wins the treasure!

On your grid, your ships are marked as '|O|'. If a ship is
hit, it will be marked as '|X|'. If it's a miss, it will be marked
as '|-|'. A coin toss will be done to see who gets to shoot first."""


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
    print(user_instructions)
    print('')
    print(f"Are you ready, Pirate {user_name}?")
    print('')


def ask_user_ready():
    '''
    Asks the user if they are ready to play the game or not.
    Loops the response until valid response is given, either
    'aye' or 'nay' must be written.
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
        Will display the user board and computer board
        to the user. Labels will be shown above to 
        distinguish whose board belongs to who.
        '''
        if self.name == computer_board.name:
            print("\nEnemy's Board\n")
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
        ship_count = 0
        while ship_count < 5:
            column = random.randint(1, 5)
            row = random.randint(1, 5)
            if self.board_array[row, column] == '|O|':
                continue
            else:
                self.board_array[row, column] = '|O|'
                ship_count += 1
        self.display_board()

    def validate_y_coordinate(self):
        '''
        Function will validate whether input from user
        is a letter ranging from A to E, or else will
        return ValueError message.
        '''
        while True:
            try:
                print('')
                y_choice = input("Input letter coordinate (A to E):\n").upper()
                y_list = ['A', 'B', 'C', 'D', 'E']
                if y_choice not in y_list:
                    raise ValueError(
                        "Value must be a letter from A to E!")
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
                x_choice = (input("Input number coordinate (1 to 5):\n"))
                x_list = ["1", "2", "3", "4", "5"]
                if x_choice not in x_list:
                    raise ValueError(
                        "Value must be a number between 1 to 5!")
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                continue
            else:
                break
        return x_choice

    def ask_user_start(self):
        '''
        Function will ask user if they wish to place their own ships.
        If n, ship coordinates will be randomized.
        If yes, function will run to ask user to input desired coordinates.
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
        Function will allow user to input their own desired
        coordinates. Validations will run first to see if user
        types in a letter coordinate from A to E. Next, validation
        will run to see if user types in a number from 1 to 5.
        Each time a new ship is made, the user board will be displayed.
        Next, another validation will check to see if user is typing
        in a unique coordinate and if user types in a redundant
        coordinate, message will show to user to try again.
        When all five ships are placed, board will be displayed
        and coin toss will run to see who goes first.
        '''
        user_board.display_board()
        added_ship_count = 0
        while added_ship_count < 5:
            while True:
                while True:
                    try:
                        y_input = input("Choose letter (A to E):\n").upper()
                        print('')
                        y_list = ['A', 'B', 'C', 'D', 'E']
                        if y_input not in y_list:
                            raise ValueError(
                                "You must select a letter from A to E!")
                    except ValueError as e:
                        print(f"Invalid data: {e}, please try again.\n")
                        continue
                    else:
                        break
                while True:
                    try:
                        x_input = input("Choose number (1 to 5):\n")
                        print('')
                        x_list = ['1', '2', '3', '4', '5']
                        if x_input not in x_list:
                            raise ValueError(
                                "You must select a number from 1 to 5!")
                    except ValueError as e:
                        print(f"Invalid data: {e}, please try again.\n")
                        continue
                    else:
                        break
                y_input = self.column_map[y_input]
                x_input = int(x_input)
                if self.board_array[x_input, y_input] == '|O|':
                    print("You already have a ship here! Try again!")
                    print('')
                else:
                    break
            self.board_array[x_input, y_input] = '|O|'
            added_ship_count += 1
            user_board.display_board()
            if added_ship_count == 5:
                print('')
                print('Great job placing the ships!')
                print('')
                user_board.display_board()
                computer_board.randomize_ship_coordinates()
                coin_toss(user_board, computer_board)

    def user_turn_place_hit(self):
        '''
        Function will allow user to type in coordinates
        to place hit.
        Will give message back to user depending on
        if the user misses or hits the computer ships.
        Will run validation checks whether user types in a unique
        coordinate or redundant coordinate. Will display the board
        to the user when coordinates are accepted. If user score
        is below 5, will allow the computer to go next. 
        '''
        while True:
            print('')
            print("Take a hit at the enemy's board!")
            print('')
            computer_board.display_board()
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
        if self.user_score < 5:
            user_board.computer_turn_place_hit()

    def computer_turn_place_hit(self):
        '''
        When it is the computer's turn, automatically will
        generate a coordinate and direct a hit at the
        user board. Message will show whether the
        enemy has correctly hit the user's ship or
        missed. Will display the user's board back to 
        the user. 
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
                print('')
                break
            else:
                self.board_array[x_target, y_target] = '|-|'
                print('')
                print("The enemy missed!")
                print('')
                break
        self.display_board()

    def progress_game(self):
        '''
        Function will run in a while loop to continously
        play game back and forth until user or
        computer reaches a score of 5.
        '''
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
        print("We will never be able to take back our treasure.")
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
        return computer_board.user_turn_place_hit()
    else:
        print("You lost the coin toss, computer goes first!")
        return user_board.computer_turn_place_hit()
    play_game = coin_toss(user_board, computer_board)
    play_game()


def start_game():
    '''
    Function will start the game when user confirms game start.
    User board and computer board names are defined to the
    GameBoard class.
    '''
    global user_board
    global computer_board
    user_board = GameBoard("name=user")
    computer_board = GameBoard("name=computer")
    user_board.ask_user_start()
    computer_board.progress_game()


def end_game():
    '''
    When user chooses to end game after saying 'nay', will 
    create a goodbye message and give instructions to let the 
    user know how to reactive the game.
    '''
    print('')
    print("Goodbye! To play again, please click 'Run Program'!")


def main():
    '''
    Main code to execute the entire game. Will introduce the game and
    ask the user if they are ready to play.
    '''
    introduce_game()
    ask_user_ready()


main()
