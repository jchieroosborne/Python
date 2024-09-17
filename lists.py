#List of the days of the week

day_of_week = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#empty list that the user will input their information into
steps = []

#Will now begin to ask the user to inputs the amount of steps on each day of the week

for day in day_of_week:
    while True:
        try:
            # Ask the user to enter the number of steps for the current day
            steps_taken = int(input(f"How many steps did you take on {day}? "))
            # Append the number of steps to the steps list
            steps.append(steps_taken)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Display the steps recorded for each day
print("\nSteps recorded for each day:")
for day, step in zip(day, steps):
    print(f"{day}: {step} steps")

#calculate the total number of steps
total_steps = sum(steps)
print (f"\n The total number of steps taken with week are {total_steps}")

# Calculate the average number of steps and round it
average_steps = round(total_steps / len(steps))
print(f"Average steps per day: {average_steps}")

