# Define the Pet class
class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind  # private attribute
        self.__breed = breed  # private attribute
        self.__name = name  # private attribute

    # Getter and Setter for kind
    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    # Getter and Setter for breed
    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Method to print details
    def print_details(self):
        print(f"Kind: {self.__kind}, Breed: {self.__breed}, Name: {self.__name}")

# Create instances of the Pet class
pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Polly")

# Call the print_details method for each object
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrate special methods and functions
print("\nDemonstrating Special Methods and Functions:")

# __name__: Display the name of the class
print(f"Class Name: {Pet.__name__}")

# type(): Show the class used to instantiate a pet object
print(f"Type of pet1: {type(pet1)}")

# __module__: Return the module name in which the Pet class is defined
print(f"Module Name: {Pet.__module__}")

# __bases__: Display the base classes of the Pet class
print(f"Base Classes of Pet: {Pet.__bases__}")

# getattr(): Use it to access an attribute of a Pet instance
print(f"Pet1's Kind (using getattr): {getattr(pet1, 'get_kind')()}")

# isinstance(): Check if an instance is of the Pet class
print(f"Is pet1 an instance of Pet? {isinstance(pet1, Pet)}")
