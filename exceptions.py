def modify_artist_list(top_artists):
    try:
        # Ask user for the index of the artist to replace
        index = int(input("Enter the index of the artist you want to replace (0-9): "))
        # Ask user for the new artist name
        new_artist = input("Enter the new artist's name: ")
        
        # Replace the artist at the specified index
        top_artists[index] = new_artist
        print(f"Artist at index {index} has been replaced with {new_artist}.")
        
    except (ValueError, IndexError):
        print("An input error occurred. Please enter a valid index and artist name.")

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", 
                   "Mariah Carey", "Stevie Wonder", "Janet Jackson", 
                   "Michael Jackson", "Whitney Houston", "Rihanna"]
    print("Top artists:", top_artists)
    
    while True:
        # Call the modify_artist_list function
        modify_artist_list(top_artists)
        
        # Display the updated list after each modification
        print("Updated Top artists:", top_artists)
        
        # Ask the user if they want to make another change
        another_change = input("Would you like to make another change? (yes/no): ").strip().lower()
        if another_change != "yes":
            print("No further changes will be made.")
        else:
                print("Invalid input. Please type 'yes' or 'no'.")
        if another_change == "no":
            print("No further changes will be made.")
            break
main()
