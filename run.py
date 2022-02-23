def start_game():
    print('-' * 80)
    print('')
    print("Welcome to Pirate Ship!")
    print('')
    print('-' * 80)
    user_name = input("Ahoy matey! Please enter your pirate name: ")
    print('')
    print(f"Welcome aboard Pirate {user_name}! There is trouble...The enemies have stolen our beloved rum and treasure! \nThey are scattered across the Black Sea. We must shoot our cannons and try to take their ships down. \nThey have cannons of their own so they will try to hit one of our ships too! \nWe are lucky to have you Pirate {user_name}. \nThe sea board contains five by five squares in x,y coordinates. \nYou must guess the coordinates to take down their ships. The first to destroy all ships wins the rum and treasure! \nUs and the enemies both have a total of 5 ships to take down. Are you ready?")
    print('')
    input("Yes or No?")

def main():
    start_game()

main()