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
    by comas. The loop will repeatedly ask for data, until it is valid.
    """
    while True:
        print('Enter spendings for each group member for today in order')
        print('Matt, Lauren-Nicole, Luka, Lejla, Emma')
        print('Data should be 5 whole numbers, separated by comas')
        print('Example: 10,20,30,40,50,60\n')

        spendings_str = input('Enter your spendings here:\n')

        spendings_data = spendings_str.split(',')

        if validate_data(spendings_data):
            print('Data is correct\n')
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
            raise ValueError(
                f'It is exactly 5 values required, you provided {len(values)}')
    except ValueError as e:
        print(f'You provided invalid data: {e}, please try again.\n')
        return False

    return True


def update_individual_spendings_worksheet(data):
    """
    Update 'Individual_spendings' worksheet,
    add a new row with the list data provided.
    """
    individual_spendings_worksheet = SHEET.worksheet('individual spendings')
    individual_spendings_worksheet.append_row(data)


def update_total_individual_spendings_worksheet(data):
    """
    Update 'Total individual spendings' worksheet,
    add new row with list data provided
    """
    tot_individ_spendings_worksheet = SHEET.worksheet(
        'Total individual spendings')
    tot_individ_spendings_worksheet.append_row(data)


def calculate_total_individual_spendings(individual_spendings_row):
    """
    Calculate and get total individual spendings for each group member
    """
    total_spendings = SHEET.worksheet(
        'Total individual spendings').get_all_values()

    total_spendings_row = total_spendings[-1]

    total_data = []
    for total_spendings, individual_spendings_worksheet \
            in zip(total_spendings_row, individual_spendings_row):
        total = int(total_spendings) + individual_spendings_worksheet
        total_data.append(total)
    return total_data


def get_average_spendings():
    """
    Get average spendings per group member using accurate groups total spending
    """
    total_spendings = SHEET.worksheet(
        'Total individual spendings').get_all_values()

    last_row = total_spendings[-1]
    int_last_row = [int(num) for num in last_row]
    average_sum = sum(int_last_row) / 5
    int_last_row = [round(x - average_sum) for x in int_last_row]

    return int_last_row


def update_spendings_difference(data):
    """
    Update difference in members total spending to groups average spending
    """
    spendings_difference_worksheet = SHEET.worksheet('spendings difference')
    spendings_difference_worksheet.append_row(data)


def main():
    """
    Run all program functions
    """
    individual_spendings_values = get_individual_spendings()
    spendings_data = [int(num) for num in individual_spendings_values]
    update_individual_spendings_worksheet(spendings_data)
    new_total_data = calculate_total_individual_spendings(spendings_data)
    update_total_individual_spendings_worksheet(new_total_data)
    average_number = get_average_spendings()
    update_spendings_difference(average_number)
    headings = SHEET.worksheet('Total individual spendings').row_values(1)
    print('Total members spendings!\n')
    print(headings)
    print(new_total_data)
    print("""
    Difference saldo shows difference in members spendings,
compared to groups average spendings:
- MINUS saldo represent that member has spend LESS than average
- PLUS saldo represent that member has spend MORE than average \n""")
    print(headings)
    print(average_number)

    
print('Welcome to Vacation Spendings Group\n')
main()
