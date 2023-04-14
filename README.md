# Countries Hangman
'Countries Hangman' is a terminal based Python game in which players have to guess letters or words to find out the name of a country before they are out of lives and the man is hanged.
![Countries Hangman gif](docs/hangman.gif)

View the live site [here](https://hangman-countries.herokuapp.com/)
## User Experience
### Site Owner's goals
- To create an entertaining and interactive game of Hangman for users to enjoy
- To make it easy for users to interact with the game
- To have a scores system and to enable users to save their high scores
### User's goals
- To easily interact with the game
- To play a fun and entertaining game of Hangman
- To have clear instructions explaining the rules of the game
- To be clearly informed of what any errors are from any invalid inputs
- To view my score after each game
- To save my high scores to a high scores leaderboard
- To have the option to play the game again or quit
## Design
### Flowchart
I made the following flowchart to show the logic of the game from the start to the end, making sure to include any points where validity checks would be needed.
![Flowchart](docs/hangman_flowchart.png)
### Colours
I used colorama to input the following colours:
- Any input error messages from the user are in red as red is a colour often associated with warnings.
- The text is green when the user guesses a letter or word correctly as green is often associated with doing something correctly.
- The text is yellow when the user guesses a letter or word incorrectly or when they are out of lives as I wanted to use a bright colour to stand out, and as I had used red already, I chose yellow as a suitable colour here.
- The initial welcome message is light yellow and bold to make it stand out as the welcoming title of the game.
- The hangman logo is light magenta, again to add a bit of colour to the welcome screen and because this colour is close to red so represents the danger.
## Features
### Welcome page
- This is what the player will be greeted with upon opening the game.
- There are 3 options for the user to choose from:
    - Playing the game
    - Reading the rules
    - Viewing the high scores
- Error messages will appear for any invalid inputs.
<details><summary>Welcome page</summary>

![Welcome page](docs/features/welcome_page.png)
</details>

### Rules
- This page explains the rules of the game and how scoring will be calculated, along with an explanation of the bonus points.
- The user has to enter 0 to return to the home page.
- Error messages will appear for any invalid inputs.
<details><summary>Rules page</summary>

![Rules page](docs/features/rules.png)
</details>

### High scores
- This page displays the top 10 highest scores.
- If there are not 10 scores that have been saved yet, this page will display as many scores as there are in the correct descending order.
- The user has to choose either to play again or return home if they have already played the game (so they would have already inputted a username to allow them to play again).
- Or, if the user views the high scores page after opening the game (and so would not have inputted a username yet), they have to enter 0 to return home, since, if they have not played yet, they would be unable to select an option to play again.
- Error messages will appear for any invalid inputs.
<details><summary>High scores page after playing a game</summary>

![High scores page after playing a game](docs/features/high_scores.png)
</details>
<details><summary>High scores page without playing a game yet</summary>

![High scores page without playing a game yet](docs/features/high_scores_start_of_game.png)
</details>

### Play game
- This is where the main Hangman game is played.
- The user is greeted with their inputted name and presented with the empty gallows, 0 points and 6 lives.
- They are shown the blank word as well as what letters they have guessed (which will be updated as they play).
- They are prompted to input a letter or a word of the number of letters in the randomly selected word.
<details><summary>Game page</summary>

![Game page](docs/features/start_of_game.png)
</details>

- The user will receive different messages depending on whether they have guessed the word or letter correctly or not.
- Their score, lives and the hangman figure will also change during the game depending on whether they have guessed correctly or not.
<details><summary>Game page - correctly guessed letter</summary>

![Game page - correctly guessed letter](docs/features/correct_letter_guess.png)
</details>

<details><summary>Game page - correctly guessed word</summary>

![Game page - correctly guessed word](docs/features/correct_word_guess.png)
</details>

<details><summary>Game page - incorrectly guessed letter</summary>

![Game page - incorrectly guessed letter](docs/features/incorrect_letter_guess.png)
</details>

<details><summary>Game page - incorrectly guessed word</summary>

![Game page - incorrectly guessed word](docs/features/incorrect_word_guess.png)
</details>

### End of game section
- This is what the user will see once they have finished their game.
- There is a 3 second delay before this page appears so that the user can see the end message before their final score and the end of game options are presented to them.
- There are 3 options for the user to choose from:
    - Playing again
    - Viewing the high scores
    - Returning to the home page
- Error messages will appear for any invalid inputs.

<details><summary>End of game page</summary>

![End of game page](docs/features/end_options.png)
</details>

### Google Sheet
- This is the Google Sheet that I connected to the game in order to store the high scores

<details><summary>Google Sheet</summary>

![Google Sheet](docs/features/google_sheet.png)
</details>

### Future Features
- I think it would be a nice addition to create different levels of the game, for example based on the different lengths of the words, or different regions of countries, and there could be varying points awarded for the different levels.
## Technologies
- Python
    - Used to build the functionality of the game
        - Python Packages:
            - random: used to generate a random word
            - os: used to clear the screen
            - string: used to create a string of only uppercase letters to be used in the game
            - time: used to create a delay on the screen before showing the next function
            - gspread: used to connect the game to the Google Sheet
            - google.oauth2.service_account: used to enable confidential access to the Google Sheet
            - colorama: used to add colour to the text of the game
- Gitpod
    - Used to develop and edit the code
- Git
    - Used to add, commit and push the code
- Heroku
    - Used to deploy the live site
- [Diagrams.net](https://app.diagrams.net/)
    - Used to create the flowchart that was used to plan the game
## Testing
### Validator Testing
No errors were found when all 3 python pages were passed through the [CI Python Linter](https://pep8ci.herokuapp.com/):
<details><summary>run.py Validator Testing</summary>

![run.py Validator Testing](docs/testing/run.py_testing.png)
</details>
<details><summary>words.py Validator Testing</summary>

![words.py Validator Testing](docs/testing/words.py_testing.png)
</details>
<details><summary>hangman_lives.py Validator Testing</summary>

![hangman_lives.py Validator Testing](docs/testing/hangman_lives.py_testing.png)
</details>

### Testing User Stories
- Expectation: To easily interact with the game
    - Result: The menu on the welcome page explains what to do and any invalid inputs are met with error messages explaining the problem or what to do
- Expectation: To play a fun and entertaining game of Hangman
    - Result: The large list of countries available to guess means that if a player plays the game repeatedly it is not likely that the word will be repeated, making the game more engaging and entertaining
- Expectation: To have clear instructions explaining the rules of the game
    - Result: The Rules page, found through the Welcome page, clearly explains how to play the game, how points are awarded or deducted, how lives are lost, and how to gain or lose bonus points
- Expectation: To be clearly informed of what any errors are from any invalid inputs
    - Result: All error messages will appear in red to make them stand out and they contain information stating what the error is and how to fix it
- Expectation: To view my score after each game
    - Result: The scores will be calculated and displayed during the game, and once the game is over the player will be shown their final score
- Expectation: To save my high scores to a high scores leaderboard
    - Result: Scores will automatically be updated to the high scores Google Sheet and the top 10 high scores will be displayed on the High Scores page
- Expectation: To have the option to play the game again or quit
    - Result: At the end of the game the player has the option to play again, to see the high scores or to return to the Home page
### Manual Testing
Thorough testing of this game has been undertaken to ensure that the game functions as expected and that any invalid user inputs or errors have been handled correctly.
####  Welcome page - Correct inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Select 1 | Instructed to enter name. | Entered 1. | Instructed to enter my name. [Enter name input](docs/testing/enter_name.png) |
| Select 1 and then enter a name with only alphabetical characters | Taken to the main game. | Entered 1 and entered the name 'bob'. | Taken to the main game and greeted with a personalised message including the name 'Bob' (the name has been automatically capitalised). [Personalised welcome message](docs/testing/name_message.png) |
| Select 2 | Taken to the Rules page. | Entered 2. | Taken to the Rules page.
| Select 3 | Taken to the High Scores page. | Entered 3. | Taken to the High Scores page. |

####  Welcome page - Inorrect inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter an invalid number | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered 4. | Presented with the following error message and instructed to select an option: [Invalid number](docs/testing/welcome_number_error.png) |
| Enter a word | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered the word 'yes'. | Presented with the following error message and instructed to select an option: [Invalid word](docs/testing/welcome_word_error.png) |
| Enter without typing anything | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered without typing anything. | Presented with the following error message and instructed to select an option: [Enter error](docs/testing/welcome_enter_error.png) |
| Name input with numbers and symbols | Presented with a red error message to enter a name with just letters and instructed to enter your name again. |Entered the name 'bob123!' | Presented with the following error message and instructed to enter my name again: [Invalid name](docs/testing/welcome_invalid_name.png) |
| Blank name input | Presented with a red error message stating that you must enter a name to continue and instructed to enter your name again. | Entered without typing anthing. | Presented with the following error message and instructed to enter my name again: [Blank name](docs/testing/welcome_blank_name.png) |

####  Rules page

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter 0 | Taken back to the Welcome page. | Entered 0. | Taken back to the Welcome page. |
| Enter an invalid number | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered 10. | Presented with the following error message and instructed to enter 0: [Invalid number](docs/testing/rules_number_error.png) |
| Enter a word | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered the word 'return'. | Presented with the following error message and instructed to enter 0: [Invalid word](docs/testing/rules_word_error.png) |
| Enter without typing anything | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered without typing anything. | Presented with the following error message and instructed to enter 0: [Enter error](docs/testing/rules_enter_error.png) |

#### High scores page (start of game - with no username inputted)

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter 0 | Taken back to the Welcome page. | Entered 0. | Taken back to the Welcome page. |
| Enter an invalid number | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered 10. | Presented with the following error message and instructed to enter 0: [Invalid number](docs/testing/high_scores_number_error.png) |
| Enter a word | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered the word 'return'. | Presented with the following error message and instructed to enter 0: [Invalid word](docs/testing/high_scores_word_error.png) |
| Enter without typing anything | Presented with a red error message to only enter 0 and instructed to enter 0. | Entered without typing anything. | Presented with the following error message and instructed to enter 0: [Enter error](docs/testing/high_scores_enter_error.png) |

#### Main game page - correct inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter a correct letter | Will receive a personalised green message stating that the letter (which will automatically be written in uppercase) is in the word. Points will increase by 10. Lives and hangman figure will remain unchanged. The guessed letter will be filled into the missing word and added to the guessed letters set. | Entered the letter 'a'. | Received a personalised green message stating that the letter 'A' is in the word. Points increased by 10. Lives and hangman figure are unchanged. The guessed letter has been filled into the missing word and added to the guessed letters set. [Correct letter guess](docs/testing/play_correct_letter.png) |
| Enter an incorrect letter | Will receive a yellow message stating that the letter (which will automatically be written in uppercase) is in the word. Points will decrease by 5. Lives decrease by 1 and hangman figure will start to appear. The guessed letter will be added to the guessed letters set. | Entered the letter 'q'. | Received a yellow message stating that the letter 'Q' is not in the word. Points decreased by 5 (from 10 points to 5 points). Lives decreased by 1 (from 6 to 5) and the hangman figure has started to appear. [Incorrect letter guess](docs/testing/play_incorrect_letter.png) |
| Enter an incorrect word of the correct number of letters | Will receive a yellow message stating that the word guessed is not the correct word. Points will decrease by 50. Lives decrease by 1 and hangman figure grows a limb. |Entered the word 'france'. | Received a yellow message stating that the word 'France' was incorrect. Points decreased by 50 (from 5 to -45). Lives decreased by 1 (from 5 to 4) and the hangman figure has grown. [Incorrect word guess](docs/testing/play_incorrect_word.png) |
| Enter the correct word | Will receive a personalised green message stating the word is correct. There will be a 3s delay before being taken to the end page where it will say the final score, which will have increased by 100 points. | Entered the correct word 'slovakia'. | Received a personalised green message stating the word is correct. There was a 3s delay before being taken to the end page where it stated the final score, which will have increased by 100 points (from -45 to 55). [Correct word message](docs/testing/play_correct_word.png) and [Correct word score](docs/testing/play_correct_word_score.png) |
| Hangman figure growth as lives decrease | For each incorrect guess the hangman figure will grow a new limb and the lives will decrease. | Enter incorrect guesses until the hangman figure is complete and there are no lives left. There will be a 3s delay before being taken to the end page where it will say the final score. | [6 lives left](docs/testing/play_6_lives.png), [5 lives left](docs/testing/play_5_lives.png), [4 lives left](docs/testing/play_4_lives.png), [3 lives left](docs/testing/play_3_lives.png), [2 lives left](docs/testing/play_2_lives.png), [1 life left](docs/testing/play_1_life.png), [0 lives left](docs/testing/play_0_lives.png). There was then a 3s delay before being taken to the end page where it stated the final score. [Incorrect final score](docs/testing/play_incorrect_word_score.png) |

#### Main game page - incorrect inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter a number | Will receive a red error message stating that this is an invalid character and instructed to try again. Points, lives and hangman figure remain unchanged. | Entered the number 1. | Received the following red error message. Points, lives and hangman figure were unchanged. [Number error](docs/testing/play_number_error.png) |
| Enter a symbol | Will receive a red error message stating that this is an invalid character and instructed to try again. Points, lives and hangman figure remain unchanged. | Entered an exclamation mark. | Received the following red error message. Points, lives and hangman figure were unchanged. [Symbol error](docs/testing/play_symbol_error.png) |
| Enter without typing anything | Will receive a red error message stating that this is an invalid character and instructed to try again. Points, lives and hangman figure remain unchanged. | Entered without typing anything. | Received the following red error message. Points, lives and hangman figure were unchanged. [Enter error](docs/testing/play_enter_error.png) |
| Enter a word of the incorrect amount of letters | Will receive a red error message instructing the user to enter a letter or word of the correct number of letters and told to try again. Points, lives and hangman figure remain unchanged. | Entered the word 'spain' (the word to guess has 8 letters). | Received the following red error message. Points, lives and hangman figure were unchanged. [Incorrect word length](docs/testing/play_wrong_word_length.png) |
| Enter an already guessed letter | Will receive a red error message that the letter has already been guessed and instructed to try again. Points, lives and hangman figure remain unchanged. | Entered the letter 'a' which had already been guessed. | Received the following red error message. Points, lives and hangman figure were unchanged. [Guessed letter error](docs/testing/play_same_letter.png) |
| Enter an already guessed word | Will receive a red error message that the word has already been guessed and instructed to try again. Points, lives and hangman figure remain unchanged. | Entered 'germany' which had already been guessed. | Received the following red error message. Points, lives and hangman figure were unchanged. [Guessed word error](docs/testing/play_same_word.png) |

#### End of game page - correct inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Select 1 | Taken to the start of the main game page to play again. Different word will be generated to guess. | Entered 1. | Taken to the start of the main game page to play again. Different word generated to guess (previously had a 8 letter word to guess, now have a 5 letter word). |
| Select 2 | Taken to end of game high scores page (has a different selection of options to when accessing high scores page at start of game when no username has been inputted yet). | Entered 2. | Taken to end of game high scores page. |
| Select 3 | Taken back to the Welcome page. | Entered 3. | Taken back to the Welcome page. |

#### End of game page - incorrect inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter an invalid number | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered 4. | Presented with the following error message and instructed to select an option: [Invalid number](docs/testing/end_page_number_error.png) |
| Enter a word | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered the word 'yes'. | Presented with the following error message and instructed to select an option: [Invalid word](docs/testing/end_page_word_error.png) |
| Enter without typing anything | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered without typing anything. | Presented with the following error message and instructed to select an option: [Enter error](docs/testing/end_page_enter_error.png) |

#### High scores page (after a username has been inputted) - correct inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter 1 | Taken to the start of the main game page to play again. Different word will be generated to guess. | Entered 1. | Taken to the start of the main game page to play again. Different word generated to guess (previously had a 5 letter word to guess, now have an 8 letter word). |
| Enter 2 | Taken back to the Welcome page. | Entered 2. | Taken back to the Welcome page. |

#### High scores page (after a username has been inputted) - incorrect inputs

| Feature | Expectation | Action | Result |
| ---| ---| ---| ---|
| Enter an invalid number | Presented with a red error message to only enter the number 1 or 2 and instructed to select an option again. | Entered 3. | Presented with the following error message and instructed to select an option: [Invalid number](docs/testing/high_scores_2_enter_error.png) |
| Enter a word | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered the word 'yes'. | Presented with the following error message and instructed to select an option: [Invalid word](docs/testing/high_scores_2_word_error.png) |
| Enter without typing anything | Presented with a red error message to only enter the number 1, 2 or 3 and instructed to select an option again. | Entered without typing anything. | Presented with the following error message and instructed to select an option: [Enter error](docs/testing/high_scores_2_enter_error.png) |

## Solved Bugs
- I initally drew the hangman figure incorrectly resulting in it displaying off centre as I realised that you cannot use two ' \ ' as only one ' \ ' displays, leading to the figure being displayed off centre:

![Initial Hangman figure](docs/bugs/initial_figure_image.png) Initial drawing
![Initial figure output](docs/bugs/figure_output.png) Initial figure output
- I decided to draw the final figure without as many ' \ ' because of this issue and because I though the final result looked better.

    ![Final Hangman drawing](docs/bugs/final_figure.png) Final drawing
    ![Final Hangman figure](docs/bugs/final_output.png) Final output

- The Scoresheet was initally not updating correctly but this was solved by adding USER_NAME and score as parameters of the update_scoresheet function.
- The screen was not clearing when selecting to play again at the end of the game. This was fixed by moving the clear operation before play_game() instead of after it:

![Code before](docs/bugs/clear_before.png) Code before

![Code after](docs/bugs/clear_after.png) Code after

- The high scores were printing in reverse alphabetical order instead of a decreasing numerical order and the scores were printing as strings instead of integers:

    ![Scores before](docs/bugs/scores_before.png)
    - This was solved by converting the scores to integers and implementing the following code, found on Stack Overflow, to print the scores in numerically decreasing order:

![Scores code](docs/bugs/scores_code.png)

![Scores after](docs/bugs/scores_after.png) Scores after

- There was an error on the scoresheet when there were not at least 10 scores saved on the Google Sheet. This is because the range for the scores had been set to 10:
![Scores error](docs/bugs/scores_error.png)
    - This was solved by adding an if/else statement to create a maximum range if there are less than 10 scores saved:

    ![Solution to the scores error](docs/bugs/scores_error_solution.png) 
- The names and scores were initially not aligning the same amount with longer names displaying their scores further to the right:

    ![Misaligned scores](docs/bugs/unaligned_scores.png)
    - This was solved by adding an if/else statement to the for loop which adds 2 tabs if the player's name is less than 7 characters, but only 1 tab if the player's name is more than 7 characters:
    ![Misaligned scores solution code](docs/bugs/misaligned_scores_solution.png)
- The coloured pieces of text were not displaying when deployed to Heroku, resulting in this error message:

    ![Colours error](docs/bugs/colours_error.png)
    - This was solved by updating the requirements.txt file so that the colours would deploy correctly.
## Deployment
### Deploying the Project
- This game was deployed to Heroku. The steps to do this are as follows:
    - Create an account with [Heroku](https://id.heroku.com/login).
    - On the Heroku dashboard, click the button that says "New", then click "Create new app".
    - Choose a unique name for the app.
    - Select your region, then click "Create app".
    -  Click on the "Settings" button on the menu.
    - Scroll down to the section "Config Vars" and click "Reveal Config Vars".
    - Enter CREDS in the field for key and copy and paste the creds.json file into the field for value and then click "Add".
    - Add another Config Var with the key Port and the value 8000.
    - Scroll down to the "Buildpacks" section and click "Add buildpack".
    - Select "python" and then "Save changes".
    - Then click "Add buildpack" again and select "node.js" and "Save changes".
    - Go to the "Deploy" button on the menu at the top.
    - Select GitHub as the deployment method and click the "Connect to GitHub" button.
    - Search for the repository "hangman" and then click "Connect".
    - Scroll to the bottom of the page and either click "Enable Automatic Deploys" in the Automatic deploys section or "Deploy branch" in the Manual deploy section.
### Forking the Project
- Follow the steps below to fork this project,:
    - Locate the hangman repository: https://github.com/s-batish/hangman
    - Click the 'Fork' button at the top right of the page.
### Cloning the Project
- Follow the steps below to clone this project:
    - Locate the hangman repository: https://github.com/s-batish/hangman
    - Click the green 'Code' button.
    - Copy the URL for the repository.
    - Open the repository and open a new terminal.
    - Change the current directory to the location that you want the cloned directory to be.
    - Type 'git clone' and paste the copied URL.
    - Press 'enter' to create the clone.
## Credits
### Content
- The list of countries was from [GitHub Gist](https://gist.github.com/kalinchernev/486393efcca01623b18d)
### Code
- [Free Code Camp](https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s) and [Kite](https://www.youtube.com/watch?v=HRJRq2r7eL8) were used to help create the play_game() function.
-  [Stack Overflow](https://stackoverflow.com/questions/53570558/python-sorting-a-leaderboard-from-highest-to-lowest-scores-and-top-5-external-f) was used to explain how to sort the leaderboard.
- [Stack Overflow](https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string) was also used to show how to remove white spaces from inputs.
- [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/) was used to explain how to clear the screen.
- [Stack Abuse](https://stackabuse.com/how-to-print-colored-text-in-python/) was used to show how to add colour to Python text.
- [Stack Overflow](https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python) was used once more to explain how to make text bold in Python.
- [Real Python](https://realpython.com/python-sleep/) was used to explain how to add time delays.