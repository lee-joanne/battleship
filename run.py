import random
from boardclass import GameBoard

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
    While loop will ensure that user does not leave
    the name input empty.
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
    while True:
        user_name = input("Ahoy matey! Please enter your pirate name:\n")
        print('')
        if user_name == '':
            print("Please enter a name!")
            print('')
        else:
            break
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

