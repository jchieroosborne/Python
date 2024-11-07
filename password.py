def main():
    print("Welcome! Please set up your password.")

    while True:
        password = input("Enter a password: ")

        # Check if password meets the criteria
        if (
            8 <= len(password) <= 20 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%&*" for char in password)
        ):
            # Confirm the password by asking the user to enter it again
            try:
                confirm_password = input("Confirm your password: ")
                if password == confirm_password:
                    print("Password setup successful!")
                    break
                else:
                    print("Passwords do not match. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Password does not meet the required criteria. Please try again.")
main()