import gspread
from google.oauth2.service_account import Credentials

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

def welcome():
    """
    Prints welcome message and gives user 3 options:
    to play the game, to see the rules and to go to the
    high scores area.
    Run a while loop to collect a valid input from user.
    The loop will continue to run until user enters valid
    data.
    """
    print("Welcome to your game of Hangman!\n")
    print("""Select an option (1, 2 or 3) to continue:
    1 - Play Hangman
    2 - Read the rules
    3 - See the high scores\n""")

    while True:
        menu_options = input("Select an option: ").strip()
        if menu_options == "1":
            print("You selected 1")
            break
        elif menu_options == "2":
            print("You selected 2")
            break
        elif menu_options == "3":
            print("You selected 3")
            break
        else:
            print("Please only enter number 1, 2 or 3\n")        

def main():
    """
    Runs all programme functions
    """
    welcome()

main()
