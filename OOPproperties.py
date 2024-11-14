class Pet:
    # Class variable for vet's office name
    vet_name = "Happy Paws Veterinary Clinic"
    
    # Initialize
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Private attributes
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, first_name):
        self.__owner_first_name = first_name

    # Getter and Setter for owner_last_name
    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, last_name):
        self.__owner_last_name = last_name

    # Getter and Setter for pet_id
    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    # Getter and Setter for pet_name
    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    # Getter and Setter for pet_type
    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # Method to display pet info
    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Vet: {Pet.vet_name}")
    

# Function to check if a property exists in the pet object
def check_property(pet, property_name):
    if hasattr(pet, property_name):
        print(f"The property '{property_name}' exists in the pet object.")
    else:
        print(f"The property '{property_name}' does not exist in the pet object.")

# Creating pet objects
pet1 = Pet("John", "Doe", 101, "Buddy")
pet2 = Pet("Jane", "Smith", 102, "Mittens", "Cat")
pet3 = Pet("Emily", "Jones", 103, "Goldie", "Fish")

# Using setter method to change pet type for pet1
pet1.set_pet_type("Husky")

# Display information for each pet
print("Displaying Pet Information:")
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# Check property existence
print("Checking Property Existence:")
check_property(pet1, "_Pet__pet_name")  # Checking private property by name
check_property(pet2, "_Pet__owner_first_name")
check_property(pet3, "vet_name")
check_property(pet3, "non_existent_property")
