def main():
    # Define time slots
    time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
    
    # Create an empty list to store heart rate data
    heart_rates = []
    
    # Loop over each time slot to get heart rate input from the user
    for slot in time_slots:
        while True:
            try:
                # Ask the user to enter their heart rate
                heart_rate = int(input(f"Enter your heart rate for {slot} (in beats per minute): "))
                # Append the time slot and heart rate to the heart_rates list
                heart_rates.append([slot, heart_rate])
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    # Display the collected heart rate data
    print("\nHeart Rate Data:")
    for entry in heart_rates:
        print(f"Time Slot: {entry[0]}, Heart Rate: {entry[1]} bpm")
    
    # Calculate the average heart rate
    total_heart_rate = 0
    for entry in heart_rates:
        total_heart_rate += entry[1]
    
    # Avoid division by zero
    if len(heart_rates) > 0:
        average_heart_rate = total_heart_rate / len(heart_rates)
    else:
        average_heart_rate = 0
    
    # Print the average heart rate
    print(f"\nAverage Heart Rate: {average_heart_rate:.2f} bpm")

# Run the main function
if __name__ == "__main__":
    main()
