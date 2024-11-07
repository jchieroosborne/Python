# Main function to run the flower list program
def main():
    flower_list = []

    # Collect flower names until the user types "done"
    print("Enter the names of flowers (type 'done' to finish):")
    while True:
        flower = input("Flower name: ").strip()
        if flower.lower() == "done":
            break
        if flower:
            flower_list.append(flower)
        else:
            print("Flower name cannot be empty.")

    # Sort and display the flowers with numbers
    flower_list.sort()
    print("\nSorted Flower List:")
    for i, flower in enumerate(flower_list, start=1):
        print(f"{i}. {flower}")

    # Search for a flower
    search_flower = input("\nEnter a flower name to search: ").strip()
    if search_flower in flower_list:
        print(f"{search_flower} is in the list.")
    else:
        print(f"{search_flower} is not in the list.")

    # Access a flower by number with error handling
    try:
        flower_number = int(input("\nEnter a number to access the corresponding flower: "))
        print(f"You selected: {flower_list[flower_number - 1]}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except IndexError:
        print(f"Number out of range! Choose between 1 and {len(flower_list)}.")

# Call the main function directly
main()
