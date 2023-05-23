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
SHEET = GSPREAD_CLIENT.open('group_vacation_spendings')


def get_individual_spendings():
    """
    Get todays spendings from each group member.
    Run a while loop to collect a valid string of data from the user
    via the terminal, wich must be a string of 5 numbers separated
    by comas. The loop will repeatedly request data, until it is valid.
    """
    
    print('Please enter spendings for each group member for today')
    print('Data should be 5 numbers, separated by comas')
    print('Example: 10,20,30,40,50,60\n')

    spendings_str = input('Enter your spendings here:\n')

    print(f'The spendings provided are {spendings_str}')


get_individual_spendings()




