import os
print(f"Current working directory: {os.getcwd()}")


def main():
    try:
        # Example file handling
        file_name = "sales_totals.txt"
        
        # Open the text file for reading
        with open(file_name, "r") as file:
            total = 0.0  # Running total
            count = 0    # Line count

            print("Sales Totals:")

            # Read lines from the file one by one
            for line in file:
                try:
                    # Strip newline symbol and convert to float
                    number = float(line.strip())
                    total += number
                    count += 1
                    # Format and display the number
                    print(f"{number:,.2f}")
                except ValueError:
                    print("Invalid number encountered. Skipping...")

            # Calculate average
            average = total / count if count > 0 else 0

            # Display total, count, and average
            print(f"\nTotal: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")

    except IOError:
        print(f"Error: Unable to access or read the file '{file_name}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
