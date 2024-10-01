def main():
    nato_alphabet = {'A': 'Alpha', 
                     'B': 'Bravo',
                     'C': 'Charlie',
                     'D': 'Delta',
                     'E': 'Echo',
                     'F': 'Foxtrot',
                     'G': 'Gulf',
                     'H': 'Hotel',
                     'I': 'India',
                     'J': 'Juliette',
                     'K': 'Kilo',
                     'L': 'Lima',
                     'M': 'Mike',
                     'N': 'November',
                     'O': 'Oscar',
                     'P': 'Papa',
                     'Q': 'Quebec',
                     'R': 'Romeo',
                     'S': 'Sierra',
                     'T': 'Tango',
                     'U': 'Uniform',
                     'V': 'Victor',
                     'W': 'Whiskey',
                     'X': 'X-Ray',
                     'Y': 'Yankee',
                     'Z': 'Zulu'}
    def spell_word():
        user_word = input("\nPlease enter a word that you would like to convert into NATO Phonetics: ") 
        user_word = user_word.upper()
        for letter in user_word:
            if letter in nato_alphabet:
                print(nato_alphabet[letter])
            else:
                print(f"{letter} is not a valid letter.")
    spell_word()
main()
