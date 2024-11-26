# Define a generator function to produce all possible two-letter combinations
def two_letter_combinations(char_list):
    """
    A generator function that yields all possible two-letter combinations
    from the given list of characters.

    Parameters:
        char_list (list): A list of characters to create combinations from.
    """
    # Use nested loops to iterate over the list of characters
    for char1 in char_list:
        for char2 in char_list:
            # Yield the concatenated two-letter combination
            yield char1 + char2

# Main method
if __name__ == "__main__":
    # Define a list of 5 characters
    characters = ['x', 'y', 'z', 'p', 'q']

    # Call the generator function with the character list
    combinations = two_letter_combinations(characters)

    # Iterate over the generator and print each combination
    for combination in combinations:
        print(combination)
