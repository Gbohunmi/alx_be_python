from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time :",current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

display_current_datetime()    

days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.now() + timedelta(days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))    

calculate_future_date()