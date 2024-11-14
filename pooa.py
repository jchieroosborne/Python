class Person:
    # Initialize the Person class with default values
    def __init__(self, name="", address="", age=0, phone=""):
        self._name = name
        self._address = address
        self._age = age
        self._phone = phone

    # Accessor (getter) methods
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    # Mutator (setter) methods
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

    # Method to display Person information
    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Address: {self.get_address()}")
        print(f"Age: {self.get_age()}")
        print(f"Phone: {self.get_phone()}")
        print("-----------------------")


# Creating three instances of Person with different data
person1 = Person("John Doe", "123 Maple St, Springfield", 25, "555-1234")
person2 = Person("Dallas Osborne", "1820 Parklane Ave", 25, "847-975-0481")
person3 = Person("Angela Chiero", "19435 W Hoag CT", 59, "847-341-1190")

# Displaying the information for each instance
print("Person 1:")
person1.display_info()

print("Person 2:")
person2.display_info()

print("Person 3:")
person3.display_info()
