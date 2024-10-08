import random

def main():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            
            # Calculate the absolute difference
            difference = abs(guess - target_number)
            
            # Check how close the guess is and give feedback
            if difference == 0:
                print("Congratulations! You've guessed the correct number!")
                break  # Exit the loop if the guess is correct
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

main()