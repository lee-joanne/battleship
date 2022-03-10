# Pirate Ship

Ahoy matey! Welcome to Pirate Ship, a game that is pretty much Battleships but with a different name! Pirate Ship is a Python terminal game
to test wits, skills, and luck. The user must try to hit all of the computer's five ships before the computer hits all of the user's ships.
The five ships are placed on a 5 by 5 board (letters ranging from A to E, and numbers from 1 to 5), with each ship occupying a single (x, y) coordinate. The users must type in an (x, y) coordinate to try to guess where the computer's ships are placed. But watch out! The computer will also generate a random coordinate to try to attack back. Whoever takes down all five ships first wins!

[View live project here](https://pirate-ship54.herokuapp.com/)

## User Experience (UX)

* ### User Stories

    - First Time Visitor Goals

        1. As a First Time User, I want to fully understand what this game is called. I can see at the very beginning, the game is called Pirate Ship and seems to
        talk back to me with a pirate tone of voice to make it more fun.

        2. As a First Time User, I want to understand how to play the game. After typing in my name to the game, the game responds with my name which is nice to personalize the game, and gives me a very thorough explanation on how to play the game. I know exactly what is expected of me, what I need to achieve in this game, and how I can achieve it. The game also explains the different labels I will expect to see on the board, what |X|, |O|, and |-| are. 

        3. As a First Time User, I want the choice to be able to either place my own ships or have my ships randomized. After seeing the description of the game, the game allows me to choose. If I choose to place my own ships, the game shows me the updated board each time I put in a new ship. Each time I accidentally put in a ship where I have already put one, the game lets me know and allows me to try again. If I choose to have the board randomized, my boards will be randomized and the game will start. I can clearly see where all of my ships are placed on the randomized board.

        4. As a First Time User, I want feedback on whether I have hit the computer ships or if the computer ship has hit mine. The game is very thorough in communicating with me whether my ship or the computer's ship has been hit and always shows me an updated view of the board after every turn. The game is
        very communicative with me when I accidentally put in incorrect or invalid coordinates and allows me to try again until I put in a correct value.

        5. As a First Time User, I want to know the outcome at the end of the game and to be communicated with if I have lost or won the game. At the end of the game, the game tells me if I have lost or won and gives me an appropriate message for each occassion.

    - Returning / Frequent Visitor Goals

        1. As a Returning / Frequent Visitor, I want to be able to play the game again and have the board reshuffled. When I finish playing the game or each time I run the program, the board is reshuffled which makes the game start again from scratch.

* ### Flowchart

    - Flowchart has been created using the program Whimsical.

    -  Flowchart - [View](assets/documentation/whimsical_map.png)

## How To Play

- Pirate Ship is the exact same game as Battleships. The user and the computer will compete against each other to try to guess where each other's five ships are placed. The board is a 5 by 5 grid and the five ships occupy one single cell each in (x,y) coordinates. The game will allow the user to choose whether they would like they place their own ships or would like to have their board randomized. There is a coin toss at the beginning of the game to decide whether the user or the computer gets to guess first. When it is the user's turn, the user will type out their coordinates, letters ranging from A to E and a number from 1 to 5 (for example, A1) to place a hit and see if their guess hits the computer's ship or not. When it is the computer's turn, the computer will generate a random coordinate to try to direct a hit at the user's ships too. Each turn allows for one guess as the game will go back and forth until there is one winner. Whoever hits all of the opponent's five ships first will win the game.

[For further information on Battleships, please read here](https://en.wikipedia.org/wiki/Battleship_(game))

## Features

* ### Existing Features:

- Introduction:

    - The game will introduce the title of the game (Pirate Ship), and will let the user input their name. If the user types in nothing, the game will prompt the user to type in their name again.

    <details>
    <summary>Screenshot of Game Introduction</summary>
    <img src='assets/documentation/game-introduction.png' alt='introduction'>
    </details>

    <details>
    <summary>Screenshot of User Typing in Blank Name</summary>
    <img src='assets/documentation/type-blank-name.png' alt='blank name type'>
    </details>

- Instructions:

    - After the user types in their name, the game will give the story line and instructions on how to play the game. The game will ask the user if they are ready to start the game, the user must type either 'aye' or 'nay'. The game will convert all letters to lowercase so if the user types 'Aye' or 'Nay' it will still be registered. If the user does not type either 'aye' or 'nay', the game will prompt again for the user to type the correct response. If the user chooses 'nay', the game will close. If the user chooses 'aye', the game will ask the user if they wish to place their own ships, which takes us to the next feature...

    <details>
    <summary>Screenshot of Game Instructions</summary>
    <img src='assets/documentation/game-instructions.png' alt='game instructions'>
    </details>

    <details>
    <summary>Screenshot of User Typing Invalid Response</summary>
    <img src='assets/documentation/aye-nay-invalid.png' alt='invalid response'>
    </details>

    <details>
    <summary>Screenshot of User Selecting 'Nay'</summary>
    <img src='assets/documentation/user-nay.png' alt='user selects nay'>
    </details>

    <details>
    <summary>Screenshot of User Selecting 'Aye'</summary>
    <img src='assets/documentation/user-aye.png' alt='user selecting aye'>
    </details>

- User Choosing Coordinates:

    - After the user chooses 'aye' to start the game, the game will ask if the user wishes to add their own coordinates or not. Here, the user must either type 'y' or 'n' for the game to register the response. The game will convert the user's response to lowercase so 'Y' or 'N' are also registered as valid responses. If the user selects 'y', the game will prompt the user to type in their first coordinate. The user can choose a letter from A to E first. If the user types in an invalid response, the game will prompt the user to retry. 
    - After typing in the letter coordinate, the game will prompt the user to type in their number coordinate from 1 to 5. After typing in the correct number, the ship placement on the board will be shown to the user. If the user types in an invalid response, the game will again prompt the user to retry. 
    Each time the user places a new ship, the updated board will always be shown back to the user. If the user accidentally types in a coordinate twice, the game will let the user know and tell the user to try again. When the user places all five ships, the final board will be revealed again, telling the user good job on placing the board and tells the user that the game will start. The user's ships are marked as |O|.

    <details>
    <summary>Screenshot of 'Y' or 'N' Invalid Response</summary>
    <img src='assets/documentation/y-n-invalid.png' alt='y or n invalid'>
    </details>

    <details>
    <summary>Screenshot of User Choosing First Coordinate</summary>
    <img src='assets/documentation/user-place-ships-y.png' alt='user choosing first coordinate'>
    </details>

    <details>
    <summary>Screenshot of Invalid Letter Coordinate</summary>
    <img src='assets/documentation/invalid-letter-coord.png' alt='invalid letter coordinate'>
    </details>

    <details>
    <summary>Screenshot of A 1 First Coordinate Placed</summary>
    <img src='assets/documentation/user-place-ships.png' alt='user places first ship'>
    </details>

    <details>
    <summary>Screenshot of Invalid Number Coordinate</summary>
    <img src='assets/documentation/invalid-number-coord.png' alt='invalid number coordinate'>
    </details>

    <details>
    <summary>Screenshot of Redundant Coordinate</summary>
    <img src='assets/documentation/user-redundant-coordinate-place-ships.png' alt='redundant coordinate placed'>
    </details>

    <details>
    <summary>Screenshot of Completed Board</summary>
    <img src='assets/documentation/user-place-ships-complete.png' alt='completed board'>
    </details>

- User Selecting Randomize Coordinates:

    - If the user selects 'n' for placing their own ships, the game will randomize the user's coordinates and show the user's board to the user.

    <details>
    <summary>Screenshot of User's Randomized Board</summary>
    <img src='assets/documentation/user-randomize-coord.png' alt='randomized user board'>
    </details>

- Coin Toss

    - After the user has seen their board (either after choosing their own ship placement or randomized ship placement), a coin toss will be done to see whether the user or computer goes first. If the user wins, the user can take their first shot at the computer board. If the computer wins, the computer will take their first shot at the user board.

    <details>
    <summary>Screenshot of Coin Toss: User Wins</summary>
    <img src='assets/documentation/coin-toss-user.png' alt='user wins coin toss'>
    </details>

    <details>
    <summary>Screenshot of Coin Toss: Computer Wins</summary>
    <img src='assets/documentation/coin-toss-computer.png' alt='computer wins coin toss'>
    </details>

- Computer's Turn

    - When it is the computer's turn, the computer will generate a random coordinate. The game will let the user know if the computer has hit the user's ship or not. When a ship is hit, the board will be marked as |X|. If a ship is missed, it will be marked as |-|. The updated user board will be shown back to the user.

    <details>
    <summary>Screenshot of User Getting Hit</summary>
    <img src='assets/documentation/user-gets-hit.png' alt='user gets hit'>
    </details>

    <details>
    <summary>Screenshot of Computer Missing Shot</summary>
    <img src='assets/documentation/enemy-misses.png' alt='computer misses'>
    </details>

- User's Turn

    - When it is the user's turn, the user can type in their coordinate. Each time it is the user's turn, it will show the computer's board to the user. The first round, the computer's board will be shown blank (of course since it is the first round!). The user can then type in their coordinates, first the letter (A to E) and then the number (1 to 5). If the user types in an invalid response for the letter or the number coordinate, it will prompt the user to try again. If the user accidentally tries to hit where they have already placed a hit previously, the game will let the user know and let the user try again. If the user hits the computer's ship, the game will let the user know and show |X| on the computer's board. If the user misses, the game will let the user know and show up as |-| on the computer's board. The updated computer board will be shown back to the user.

    <details>
    <summary>Screenshot of First Round User Turn</summary>
    <img src='assets/documentation/user-first-try.png' alt='first round user turn'>
    </details>

    <details>
    <summary>Screenshot of User Inputting Coordinates</summary>
    <img src='assets/documentation/user-types-coordinates.png' alt='user inputting coordinates'>
    </details>

    <details>
    <summary>Screenshot of User Hitting Redundant Spot</summary>
    <img src='assets/documentation/user-hits-same-spot.png' alt='user hits redundant spot'>
    </details>

    <details>
    <summary>Screenshot of User Hitting Computer's Ship</summary>
    <img src='assets/documentation/computer-gets-hit.png' alt='user hits ship'>
    </details>

    <details>
    <summary>Screenshot of User Missing Hit</summary>
    <img src='assets/documentation/user-misses.png' alt='user misses hit'>
    </details>

- Game End

    - The game is over when either the user or the computer have hit all of the opponent's five ships. When the user wins, the game will congratulate the user and gives instructions on how to play again. If the computer wins, the game feels bad for the user and gives instructions on how to play again.

    <details>
    <summary>Screenshot of Game End: User Wins</summary>
    <img src='assets/documentation/user-wins.png' alt='user winning'>
    </details>

    <details>
    <summary>Screenshot of Game End: Computer Wins</summary>
    <img src='assets/documentation/computer-wins.png' alt='computer winning'>
    </details>

* ### Future Features:

- In the future, I would like the game to be able to keep track of score history. I can do this by the use of Google Drive and creating a spreadsheet to keep track of the score history.

- In the future, I would like to be able to have the boards side by side rather than having the user scroll up and down to see the user board and computer board. This feature would be a great user experience to not have to scroll constantly and be able to compare their board to the computer's board easily. 

- In the future, I want there to be different sizes of ships, ranging from 2 by 1, 3 by 1, etc. This way, there will be more diversity in the game and it will allow the game to be much harder. With this, the board size will need to be bigger as well to accomodate the different ship sizes. 

## Data Model

- For the model of the game, I have created the GameBoard class. The game will create two instances, one for the user_board and one for the computer_board. The GameBoard class will create the boards for the user and computer, the randomize ship coordinates (depending on the user's choice of placing their own ships or randomizing coordinates), placing the ships on the board, labelling the boards, and displaying the boards back to the user. The user and computer are also able to generate hits at each other's boards. The class methods are extremely important for the game to function as majority of the functionality relies on this class.

## Technologies Used

*  ### Languages and Python Packages/Libraries Used: 

- [Python](https://www.python.org/) 
- [Numpy](https://numpy.org/)
- [Random](https://www.w3schools.com/python/module_random.asp)

* ### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub](https://github.com/)
    - GitHub was used to store the project code after being pushed in by Git. Project repository linked with Heroku for deployment process. 
3. [Heroku](https://dashboard.heroku.com/login)
    - Heroku was used to deploy the Python project as a terminal based game after signing in with GitHub. 
4. [Whimsical](https://whimsical.com)
    - Whimsical was used to create the flowchart for the game. 
5. [PEP8 Online Check](http://pep8online.com/)
    - PEP8 Online Check was used to validate the Python code used and check for warnings/errors. 
6.  [Ecotrust-Canada Markdown-toc](https://ecotrust-canada.github.io/markdown-toc/)
    - Ecotrust-Canada Markdown was used to create the table of contents for this README. 

## Testing

- When copying and pasting my run.py code into the PEP8 validator, it comes back as 'all right' with no errors or warnings to show.

![Screenshot of pep8 validator](assets/documentation/pep8-validator.png)

- Lots of other testing has been done. I have played this game so many times that I wish to take a long break from playing Battleships to test each possible outcome possible of the game to ensure that all is working properly. I have bugged my work colleagues to play the game for me and they most likely are also sick of the game. I ensured that validation checks are done when typing in input responses to ensure that the game is registering that my input is invalid and will prompt me to try again. I have played the game numerous times here on Gitpod, IDLE, Spyder, and the deployed Heroku live site. All is working fine and no errors are shown. I used Numpy to help me get better control of the two-dimensional array of the game. With Numpy, it was a lot easier to target and create my boards and manipulate the boards when needed. 

* ### Bugs:

    - There have been many bugs while creating this game, a list of the main bugs encountered:

        - First bug was being unable to hide the computer's ships from the user. There was one function to display the board by inputting both the user and computer names into the GameBoard class. The randomize_ship_coordinates function would also produce randomized coordinates and previewed both ships to the user. After getting help from Tutor Support, I was able to create two separate functions to display the ships, one for the computer's ships (empty board) and one for the user's ships. In the user_turn_place_hit function, I was able to target the computer's ships based on the real computer board ship placement and the empty displayed computer board will preview whether the user has missed or not. 

        - I was facing many problems of having my Python lines too long, whether it be from long print statements, long variable names, or long docstrings. The longest string I had was the introduction of the game. I managed to fix the issue of having the introduction of the game too long by creating the variable, 'introduction', and having the string assigned to it. I, then, printed this variable in the introduce_game function. For the docstrings, I managed to make multiple lines for my docstrings to ensure they do not exceed Python's limit. As well, I have tried to shorten variable names to make them short, but still comprehensive.

        - The user_choose_ship_placement was difficult because there were many validation checks that were required, such as ensuring the user types in a letter coordinate from A to E, a number coordinate from 1 to 5, and ensuring that the user does not put in a redundant ship. It was difficult to ensure that for each invalid value, the game will correctly allow the user to repeat where required (if invalid letter coordinate, will allow the user to put in another letter coordinate. For number, it needs to allow the user to re-enter the number but also still keep the previously accepted letter coordinate. For redundant coordinate, the game needed to allow the user to try again from the start of inputting a letter coordinate). I managed to fix this with nested while loops, and strategically placed the while loops where necessary to ensure that the game will appropriately give the correct prompts and messages to the user. 

        - In the computer_turn_place_hit function, I was facing an issue where when the computer generates a new coordinate and the new coordinate turns out to be where the computer has already placed a hit, it would skip the computer's turn altogether. It turns out that previously, I had 'pass' written in my if statements. The 'pass' statements made the computer skip the turn completely if it was a coordinate where the computer has already placed a hit. I have managed to fix this by using 'continue' instead so that if the computer generates a redundant coordinate, it will redo the loop until a unique coordinate is produced.

        - I was having an issue with the coin_toss function. The function would not register the winner of the coin toss to let that person go first. I managed to get this fixed thanks to Tutor Support who suggested to add:
        play_game = coin_toss(user_board, computer_board)
        play_game()

    - There are no unresolved bugs in the game.  

## Deployment

- The game was deployed using Heroku and the Code Institute Python template. 
[The Python Code Institute template can be found here](https://github.com/Code-Institute-Org/python-essentials-template)

- The following steps were taken for the deployment process:

    1. Ensure that the template used for the project is made with the Code Institute Python template linked above. 
    2. Second, in all Python scripts, ensure that input methods have a new line character at the end of the text inside.
    3. If any packages or installments were made, type in the following command in the terminal: **'pip3 freeze > requirements.txt'** so these installments / dependencies can work on Heroku. After typing this in, the requirements.txt file in the Code Institute Python template will automataically be updated. 
    4. Commit and push these changes onto GitHub.
    5. [Create an account for Heroku](https://id.heroku.com/login)
    6. On the Heroku dashboard, go to **Create new app**. 
    7. Name your app (must be a unique name) and select your region, and go to **Create app**.
    8. On the next page after selecting **Create app**, go to the **Settings** tab. Scroll down to **Config Vars** and select **Reveal Config Vars**.
    9. Since no APIs or Creds were used for Pirate Ship, the only Config Vars added was:
    Key: PORT
    Value: 8000
    10. Next, scroll down to **Buildpacks**. Click **Add Buildpack** and select **Python** and **Save Changes**. Next, add **nodejs** and **Save changes**. Ensure Python is on top and nodejs is below. 
    11. Next, scroll up and go to the **Deploy** tab.
    12. Under **Deployment method**, select **GitHub** and confirm **Connect to GitHub**. 
    13. Search for your repository name and click **Connect**.
    14. Scroll down and select **Deploy Branch** next to **Manual Deploy**. Ensure the branch to deploy is master/main. 
    15. Deployment gets created and live link is then previewed. 

[View live project here](https://pirate-ship54.herokuapp.com/)

## Credits

* ### Code

* ### Content

* ### Acknowledgements















