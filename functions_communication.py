def custom_song(star_name, adjective1, adjective2, place, action_verb, noun1, noun2, emotion):
    lyrics = f"""
    Twinkle, twinkle, little {star_name},
    How I wonder what you are!
    Up above the world so {adjective1},
    Like a diamond in the {place}!

    Twinkle, twinkle, little {star_name},
    How I wonder what you are!

    When the blazing sun is {action_verb},
    And you shine throughout the {noun1},
    Twinkle, twinkle, little {star_name},
    How I wonder what you are!

    Then the traveler in the {noun2},
    Thanks you for your {emotion} light,
    Twinkle, twinkle, little {star_name},
    How I wonder what you are!
    """
    print(lyrics)

# Collect user input
star_name = input("Enter a name for the star: ")
adjective1 = input("Enter an adjective (1): ")
adjective2 = input("Enter an adjective (2): ")
place = input("Enter a place: ")
action_verb = input("Enter a verb (ending in -ing): ")
noun1 = input("Enter a noun (1): ")
noun2 = input("Enter a noun (2): ")
emotion = input("Enter an emotion: ")

# Call the function with user inputs
custom_song(star_name, adjective1, adjective2, place, action_verb, noun1, noun2, emotion)
