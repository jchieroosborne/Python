# Creating and using an Employee Superclass 🧑‍💼
# and a ProductionWorker subclass 🛠️
# along with instantiating (creating objects)

class Employee:
    # Employee is a Superclass of the ProductionWorker class
    def __init__(self, name, number):
        self.name = name  # Public attribute for name
        self.number = number  # Public attribute for number

    def __str__(self):
        return f"Employee: Name: {self.name}, Number: {self.number}"


class ProductionWorker(Employee):
    # ProductionWorker is a subclass of Employee
    def __init__(self, name, number, shift_number, hourly_rate):
        super().__init__(name, number)  # Inherit attributes from Employee
        self.shift_number = shift_number  # Public attribute for shift number
        self.hourly_rate = hourly_rate  # Public attribute for hourly rate

    def __str__(self):
        # Add additional details specific to ProductionWorker
        shift = "Day" if self.shift_number == 1 else "Night"
        return super().__str__() + f", Shift: {shift}, Hourly Rate: ${self.hourly_rate:.2f}"


# Main function to create and display objects
def main():
    print("\n\n")

    # Create an instance of Employee
    emp = Employee("Alice Smith", "12345")
    print("Employee:")
    print(emp)

    print("\n\n")

    # Create an instance of ProductionWorker
    worker = ProductionWorker("Bob Johnson", "67890", 2, 25.50)
    print("Production Worker:")
    print(worker)

    print("\n\n")


main()
