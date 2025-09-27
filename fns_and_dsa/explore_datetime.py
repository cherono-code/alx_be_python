import datetime
def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)
    return current_date

def calculate_future_date(current_date, days):
    """Calculate the date after adding a certain number of days to the current date."""
    future_date = current_date + datetime.timedelta(days=days)
    print("Future date:", future_date)
    return future_date

def main():
    current_date = display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, number_of_days)

if __name__ == "__main__":
    main()