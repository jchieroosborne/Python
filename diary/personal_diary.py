# diary_entry.py

def main():
    """
    Main function to collect and save diary entries.
    Prompts the user for the current date, time, and a diary entry,
    then appends the input to a file named 'diary.txt'.
    """
    # Prompt the user to input the current date and time
    date_time = input("Enter the current date and time (e.g., 2024-11-26 14:30): ")

    # Prompt the user to input their diary entry
    diary_entry = input("Enter your diary entry: ")

    # Open or create the diary.txt file in append mode
    diary_file = open("diary.txt", "a")

    # Write the date, time, and diary entry to the file
    diary_file.write(f"Date and Time: {date_time}\n")
    diary_file.write(f"Entry: {diary_entry}\n")
    diary_file.write("\n")  # Add a blank line to separate entries

    # Close the file
    diary_file.close()

    # Notify the user
    print("Your diary entry has been saved.")

# Run the main function
if __name__ == "__main__":
    main()
