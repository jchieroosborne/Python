import calendar
import datetime

def main():
    # Set Sunday as the first day of the week
    calendar.setfirstweekday(calendar.SUNDAY)

    # Get the current year
    now = datetime.datetime.now()
    year = now.year

    # Ask the user for their birth month
    month = input("Enter your birth month (1-12): ")

    # Check if the input is valid
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            # Display the calendar for the month with updated weekday format
            print("Here is the calendar:")
            print(calendar.month(year, month))
        else:
            print("Please enter a number between 1 and 12.")
    else:
        print("That is not a valid number. Please try again.")

    # Example usage of additional calendar methods
    print("\nAdditional Calendar Information:")
    print("Abbreviated weekday names:", calendar.weekheader(3))
    print(f"Is {year} a leap year?:", calendar.isleap(year))

# Run the program
main()
