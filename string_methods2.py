import time

# TODO: Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
print("Capitalized string:", string1.capitalize())
time.sleep (.5)

# TODO: Use the center() method to center the string in a string of specified width
string2 = "python"
print("Centered string:", string2.center(10)) 
time.sleep (.5)

# TODO: Use the endswith() method to check if the string ends with a specified substring
string3 = "python"
print("Does it end with 'on'?:", string3.endswith("on"))
time.sleep (.5)

# TODO: Use the find() method to find the first occurrence of a substring in the string
string4 = "python"
print("Position of 'th':", string4.find("th"))
time.sleep (.5)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
string5 = "python3"
print("Is alphanumeric?:", string5.isalnum())
time.sleep (.5)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
string6 = "python"
print("Is alphabetic?:", string6.isalpha())
time.sleep (.5)

# TODO: Use the islower() method to check if all characters in the string are lowercase
string7 = "python"
print("Is lowercase?:", string7.islower())
time.sleep (.5)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
string8 = " "
print("Is whitespace?:", string8.isspace())
time.sleep (.5)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
string9 = "PYTHON"
print("Is uppercase?:", string9.isupper())
time.sleep (.5)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
print("Joined string:", separator.join(iterable1))
