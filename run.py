"""
Main Hangman game file
"""
import random
import os
import string
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init
from words import words
from hangman_lives import stages, logo

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman _leaderboard')

# Resets colorama colours
init(autoreset=True)

# CONSTANTS
USER_NAME = ""


def welcome():
    """
    Prints welcome message and gives user 3 options:
    to play the game, to see the rules and to go to the
    high scores area.
    Run a while loop to collect a valid input from user.
    The loop will continue to run until user enters valid
    data.
    """
    os.system("clear")
    print(Fore.CYAN + "Welcome to your game of Countries Hangman!")
    print(Fore.LIGHTMAGENTA_EX + logo[0])
    print("""Select an option (1, 2 or 3) to continue:
    1 - Play Hangman
    2 - Read the rules
    3 - See the high scores""")

    while True:
        menu_options = input("Select an option: ").strip()
        if menu_options == "1":
            input_name()
        elif menu_options == "2":
            rules()
        elif menu_options == "3":
            display_scoresheet()
        else:
            print(Fore.RED + "Please only enter number 1, 2 or 3\n")


def input_name():
    """
    Asks user to input their name.
    Throws an error message for an invalid input.
    Run a while loop to collect a valid input from user.
    """
    global USER_NAME
    while True:
        USER_NAME = input("Please enter your name: ").capitalize()
        if len(USER_NAME) == 0:
            print(Fore.RED + "You must enter a name to continue")
        elif not USER_NAME.isalpha():
            print(Fore.RED + "Your name can only include letters")
        else:
            os.system('clear')
            print(f"Let's play Hangman {USER_NAME}!")
            play_game()


def rules():
    """
    Displays rules of the game and requires user input to return
    to welcome page.
    """
    os.system('clear')
    print("""Rules:
    1.	You have 6 lives to guess the country correctly before the man
    is hanged.
    2.	You will be awarded 10 points for each letter you guess
    correctly.
    3.	If you guess a letter or word incorrectly, the man's figure
    will begin appearing in the gallows and you will lose 5 points.
    4.	If you lose all of your lives, unfortunately that is the point
    where we will say 'Hangman'.

    *BONUS POINTS*
    -   If you guess the whole country name correctly, you will be awarded
    a 100 point bonus.
    -   However, if you guess the country incorrectly, you will lose 50
    points.

    Good luck and enjoy!\n""")

    while True:
        return_home = input("Enter 0 to return: ").strip()
        if return_home == "0":
            welcome()
        else:
            print(Fore.RED + "Please only enter 0 to return home")


def get_random_word():
    """
    Generates a random word to guess from the words list
    """
    word = random.choice(words)
    return word.upper()


def play_game():
    """
    Starts the main game.
    User continues guessing letters until the word is guessed
    or the man is hanged.
    Correct letter or word increments the score and incorrect
    guesses decrement the score and number of lives.
    Input validity is checked for each user input.
    """
    lives = 6
    score = 0
    correct = 10
    incorrect = 5
    word = get_random_word()
    letters_in_word = set(word)  # set of the letters in random word
    guessed_letters = set()  # set of the letters guessed by user
    guessed_words = set()  # set of the words guessed by user
    alphabet = set(string.ascii_uppercase)
    print(display_hangman(lives))

    # User's letter guesses
    # Code adapted from https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s
    while len(letters_in_word) > 0 and lives > 0:
        word_list = [
            letter if letter in guessed_letters else "-" for letter in word
        ]
        print(f"You have {score} points and {lives} lives left")
        print("Word: ", " ".join(word_list))
        print(
            "You've guessed the following letters: ", " ".join(guessed_letters)
        )

        # User input to guess a letter.
        # Correct letter is added to guessed_letters set and correct
        # word is added to guessed_words set
        guess = input(f"Guess a letter or a word of {len(word)}"
                      " letters: ").upper().strip()
        # Condition if user guesses a letter in the alphabet.
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_in_word:
                letters_in_word.remove(guess)
                print(
                    Fore.GREEN + f"Good guess {USER_NAME}, {guess} is in the"
                    " word"
                )
                score += correct
            else:
                lives -= 1
                print(Fore.YELLOW + f"{guess} is not in the word")
                score -= incorrect
        # Conditions if user guesses a word with the correct number of letters.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.RED + f"You've already guessed the word {guess}")
            elif guess != word:
                print(Fore.YELLOW + f"{guess} is not the correct word")
                lives -= 1
                score -= 50
                guessed_words.add(guess)
            else:
                score += 100
                break
        # Condition if user guesses a word that is not correct number of
        # letters.
        elif len(guess) > 1 and guess.isalpha():
            print(
                Fore.RED + f"You must enter a letter or a word of {len(word)} "
                "letters - try again"
            )
        # Condition if user guesses a letter they have already guessed.
        elif guess in guessed_letters:
            print(Fore.RED + "You've already guessed that letter - "
                  "try another letter")
        else:
            print(Fore.RED + "Invalid character - try again")
        print(display_hangman(lives))

    # Displays end message to user depending on whethere they guess the word
    # correctly or not, with a 3s delay before displaying the end_choices()
    # function to show the end of game options to the user
    if lives == 0:
        print(Fore.YELLOW + f"\nOh no {USER_NAME}, you're out of lives -"
              " it is time to hang the man!")
        time.sleep(3)
        os.system('clear')
        print(Fore.YELLOW + f"Your final score is: {score} - better luck"
              " next time")
        update_scoresheet(USER_NAME, score)
        end_choices()

    else:
        print(Fore.GREEN + f"\nWell done {USER_NAME} for guessing the word"
              f" {word} correctly!")
        time.sleep(3)
        os.system('clear')
        print(Fore.GREEN + f"Your final score is: {score} - good job")
        update_scoresheet(USER_NAME, score)
        end_choices()


def display_hangman(lives):
    """
    Shows hangman stages from hangman_lives.py which adjust as
    user loses lives.
    """
    return stages[lives]


def end_choices():
    """
    At the end of the game, presents user with options
    to play again, view the high scores or to return
    to the home page
    """
    print("\nThis game of Hangman is over - "
          "what would you like to do now?")
    print("""Select an option below (1, 2 or 3) to continue:
    1 - Play again
    2 - View the high scores
    3 - Return home\n""")
    while True:
        end_choice = input("Select an option: ").strip()
        if end_choice == "1":
            os.system('clear')
            play_game()
        elif end_choice == "2":
            os.system('clear')
            display_scoresheet()
        elif end_choice == "3":
            welcome()
        else:
            print(Fore.RED + "Please only enter number 1, 2 or 3\n")


def update_scoresheet(USER_NAME, score):
    """
    Updates scoresheet by adding a new row with the user's name and score
    """
    scores_worksheet = SHEET.worksheet('scoresheet')
    scores_worksheet.append_row([str(USER_NAME), score])


def display_scoresheet():
    """
    Displays the top 10 scores.
    Converts the score from a string into an integer.
    Sorts the code in numerically descending order.
    """
    scores = SHEET.worksheet('scoresheet').get_all_values()[1:]
    for data in scores:
        data[1] = int(data[1])

    # Code from Stack Overflow
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    os.system('clear')
    print("High Scores:")
    print("Position\t Name\t\t Score")

    # Creates the maximum range for the scoreboard
    if len(sorted_scores) < 10:
        max_range = len(sorted_scores)
    else:
        max_range = 10

    # Aligns the Names and Scores into evenly spaced columns depending on
    # the length of the user's name
    for i in range(0, max_range):
        if len(sorted_scores[i][0]) < 7:
            print(f"{i+1}\t\t {sorted_scores[i][0]}\t\t {sorted_scores[i][1]}")
        else:
            print(f"{i+1}\t\t {sorted_scores[i][0]}\t {sorted_scores[i][1]}")
    scoresheet_options()


def scoresheet_options():
    """
    Provides the user with options to play again or return home.
    Includes a while loop that checks whether the player has
    played already or is a new player.
    """
    while True:
        if not USER_NAME:
            while True:
                return_home = input("\nEnter 0 to return: ").strip()
                if return_home == "0":
                    welcome()
                else:
                    print(Fore.RED + "\nPlease only enter 0 to return home")
        else:
            print("""\nSelect an option below (1 or 2) to continue:
                1 - Play again
                2 - Return home\n""")
            while True:
                scoresheet_choice = input("Select an option: ").strip()
                if scoresheet_choice == "1":
                    os.system('clear')
                    play_game()
                elif scoresheet_choice == "2":
                    os.system('clear')
                    welcome()
                else:
                    print(Fore.RED + "Please only enter number 1 or 2\n")


def main():
    """
    Runs all programme functions.
    """
    welcome()


main()
