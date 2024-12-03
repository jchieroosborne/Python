import datetime

def main():
    # Ask for user's birth year, month, and day.
    try:
        year = int(input("What year were you born? "))
        month = int(input("What month were you born (1-12)? "))
        day = int(input("What day were you born? "))

        # Create a date for the user's birthday.
        birthday = datetime(year, month, day)

        # Get today's date.
        today = datetime.now()

        # Calculate difference between today and birthday.
        difference = today - birthday

        # Calculate age in years, months, weeks, days, hours, and minutes.
        years = difference.days // 365
        months = years * 12 + (difference.days % 365) // 30
        weeks = difference.days // 7
        days = difference.days
        hours = difference.days * 24
        minutes = hours * 60

        # Print results.
        print("\nYour Age:")
        print(f"Years: {years}")
        print(f"Months: {months}")
        print(f"Weeks: {weeks}")
        print(f"Days: {days}")
        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")

    except ValueError:
        print("Please enter numbers only.")

if __name__ == "__main__":
    main()
