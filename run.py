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
    while True:
        print('Please enter spendings for each group member for today in order Matt, Loreen-Nicole, Luka, Lejla, Emma')
        print('Data should be 5 numbers, separated by comas')
        print('Example: 10,20,30,40,50,60\n')

        spendings_str = input('Enter your spendings here:\n')

        spendings_data = spendings_str.split(',')

        if validate_data(spendings_data):
            print('Data is correct')
            break
        
    return spendings_data


def validate_data(values):
    """
    Convert all input string values from 'spendings_str' into integers
    and raises ValueError if strings can not be converted into integers and/or
    if it is not exactly 5 values.
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(f'It is exactly 5 values required, you provided {len(values)}')
    except ValueError as e:
        print(f'You provided invalid data: {e}, please try again.\n')
        return False

    return True


individual_spendings_values = get_individual_spendings()

