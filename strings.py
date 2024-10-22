import time

def main():
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)
    
    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    time.sleep(.5)
    print(min(example_string))

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    time.sleep(.5)
    print(max(example_string))
    
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    time.sleep(.5)
    print(example_string.index('o'))

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    time.sleep(.5)
    print(list(example_string))

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    time.sleep(.5)
    print(example_string.count('o'))

main()
