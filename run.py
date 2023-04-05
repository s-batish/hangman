"""
Main Hangman game file
"""
import random
import os
import string
import gspread
from google.oauth2.service_account import Credentials
from words import words
from hangman_lives import stages

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman _leaderboard')

scores = SHEET.worksheet('Sheet1').get_all_values()

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
    print("Welcome to your game of Hangman!\n")
    print("""Select an option (1, 2 or 3) to continue:
    1 - Play Hangman
    2 - Read the rules
    3 - See the high scores\n""")

    while True:
        menu_options = input("Select an option: ").strip()
        if menu_options == "1":
            input_name()
            break
        elif menu_options == "2":
            rules()
            break
        elif menu_options == "3":
            print("You selected 3")
            break
        else:
            print("Please only enter number 1, 2 or 3\n")


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
            print("You must enter a name to continue")
            continue
        elif not USER_NAME.isalpha():
            print("Your name can only include letters")
            continue
        else:
            os.system('clear')
            print(f"Let's play Hangman {USER_NAME}!\n")
            play_game()
            break


def rules():
    """
    Displays rules of the game and requires user input to return
    to welcome page.
    """
    print("""Rules:
    1.	You have 6 lives to guess the word correctly before
    the man is hanged.
    2.	You will be awarded 10 points for each letter you
    guess correctly.
    3.	If you guess a letter incorrectly, the man's figure
    will begin appearing in the gallows and you will lose 5 points.
    4.	If you lose all of your lives, unfortunately that is
    the point where we will say 'Hangman'.
    Good luck and enjoy!\n""")

    while True:
        return_home = input("Enter 0 to return: ").strip()
        if return_home == "0":
            welcome()
            break
        else:
            print("Please only enter 0 to return home")


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
    Input validity is checked for each user input.
    """
    lives = 6
    word = get_random_word()
    letters_in_word = set(word)  # set of the letters in random word
    guessed_letters = set()  # set of the letters guessed by user
    guessed_words = set()  # set of the words guessed by user
    alphabet = set(string.ascii_uppercase)

    # User's letter guesses
    # Code adapted from https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s
    print(f"This word has {len(word)} letters in it")
    while len(letters_in_word) > 0 and lives > 0:
        word_list = [
            letter if letter in guessed_letters else "-" for letter in word
        ]
        print("Word: ", " ".join(word_list))
        print(f"You have {lives} lives left")
        print(
            "You've guessed the following letters: ", " ".join(guessed_letters)
        )

        guess = input("Guess a letter: ").upper().strip()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_in_word:
                letters_in_word.remove(guess)
                print(f"Good guess {USER_NAME}, {guess} is in the word\n")
            else:
                lives -= 1
                print(f"{guess} is not in the word\n")
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You've already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the correct word")
                lives -= 1
                guessed_words.add(guess)
            else:
                break
        elif len(guess) > 1 and guess.isalpha():
            print(
                f"You must enter a letter or a word of {len(word)} "
                "letters - try again\n"
            )
        elif guess in guessed_letters:
            print("You have already guessed that letter - "
                  "try another letter\n")
        else:
            print("Invalid character - try again\n")
        print(display_hangman(lives))

    if lives == 0:
        print("Oh no, you're out of lives - it is time to hang the man!")
    else:
        print(f"Well done {USER_NAME} for guessing the word {word} correctly!")


def display_hangman(lives):
    """
    Show hangman stages which adjust as user loses lives.
    """
    return stages[lives]


def main():
    """
    Runs all programme functions
    """
    welcome()


main()
