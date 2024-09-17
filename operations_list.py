def main():
    # Initialize the list of seats (1-20)
    seats = list(range(1, 21))
    
    while True:
        # Display available seats
        print("\nAvailable seats:", seats)
        
        # Prompt the customer to select a seat
        selected_seat = input("Enter the seat number you want to purchase (or '0' to finish): ")
        
        # Convert input to integer
        try:
            selected_seat = int(selected_seat)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if selected_seat == 0:
            # Customer chose to finish their purchase
            print("Thank you for your purchase!")
            break
        
        if selected_seat in seats:
            # If the seat is available, remove it from the list
            seats.remove(selected_seat)
            print(f"Seat {selected_seat} has been booked.")
        else:
            # If the seat is not available or invalid
            print("Seat number not available or already taken. Please choose a different seat.")
    
    # Final list of available seats
    print("\nFinal list of available seats:")
    print(seats)

# Run the main function
if __name__ == "__main__":
    main()
