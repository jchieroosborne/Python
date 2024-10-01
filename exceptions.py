def square_number():
    while True:
        number = input("Enter a number to square: ")
        try:
            squared_number = int(number) ** 2
            print(f"The square of {number} is {squared_number}.")
            # Exit if conversion and squaring works
            break
        except ValueError:
            #if the conversion fails
            print("That's not a valid number. Please try again.")
square_number()
