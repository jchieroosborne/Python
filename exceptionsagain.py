# Custom exception class
class NotNumericError(Exception):
    """Exception raised for inputs that are not numeric."""
    def __init__(self, message="Input is not numeric. Please enter a number."):
        self.message = message
        super().__init__(self.message)


def main():
    while True:
        try:
            # Prompt for user input
            user_input = input("Please enter a number: ")

            # Validate if the input is numeric
            if not user_input.isnumeric():
                raise NotNumericError

        except NotNumericError as e:
            # Handle invalid input
            print(f"Error: {e}")
        
        else:
            # Confirm valid input
            print(f"Thank you! You entered a valid number: {user_input}")
            break  # Exit loop after valid input
        
        finally:
            # Indicate end of this iteration
            print("End of this iteration.\n")


# Run the program
if __name__ == "__main__":
    main()
