import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
        print('Please enter spendings for each group member for today in order \nMatt, Loreen-Nicole, Luka, Lejla, Emma')
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


def update_individual_spendings_worksheet(data):
    """
    Update 'individual_spendings' worksheet, add a new row with the list data provided.
    """
    print('Updating "individual spendings" worksheet...\n')
    individual_spendings_worksheet = SHEET.worksheet('individual spendings')
    individual_spendings_worksheet.append_row(data)

    print('"individual spendings" worksheet successfully updated!\n')


def update_total_individual_spendings_worksheet(data):
    """
    Update s worksheet, add new row with list data provided
    """
    print('Updating "Total individual spendings" worksheet...\n ')
    total_individual_spendings_worksheet = SHEET.worksheet('Total individual spendings')
    total_individual_spendings_worksheet.append_row(data)
    print('Total individual spendings worksheet updated successfully.\n')


def calculate_total_individual_spendings(individual_spendings_row):
    total_spendings = SHEET.worksheet('Total individual spendings').get_all_values()
    total_spendings_row = total_spendings[-1]

    total_data = []
    for total_spendings, individual_spendings_worksheet in zip(total_spendings_row, individual_spendings_row):
        total = int(total_spendings) + individual_spendings_worksheet
        total_data.append(total)
    return total_data


def get_average_spendings():
    total_spendings = SHEET.worksheet('Total individual spendings').get_all_values()
    last_row = total_spendings[-1]
    int_last_row = [int(num) for num in last_row]
    average_sum = sum(int_last_row) / 5
    int_last_row = [x - average_sum for x in int_last_row ]
    
    return int_last_row
    #print(spendings_difference_row)


def update_spendings_difference(data):
    spendings_difference_worksheet = SHEET.worksheet('spendings difference')
    spendings_difference_worksheet.append_row(data)
    spendings_difference_row = spendings_difference_worksheet[-1]

    
def main():
    """
    Run all program functions
    """
    individual_spendings_values = get_individual_spendings()
    spendings_data = [int(num) for num in individual_spendings_values]
    update_individual_spendings_worksheet(spendings_data)
    new_total_data = calculate_total_individual_spendings(spendings_data)
    update_total_individual_spendings_worksheet(new_total_data)
    print(new_total_data)
    average_number = get_average_spendings()
    print(average_number)
    update_spendings_difference(average_number)
 
print('Welcome to Vacation Spendings Group')
main()
#update_spendings_difference()