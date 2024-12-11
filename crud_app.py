def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def read():
    customer = check()
    lname = input("Please enter the last name to search: ")
    found = [entry for entry in customer if lname in entry.split(", ")[1]]
    if found:
        print("\nMatching entries:")
        for entry in found:
            print(entry.strip())
    else:
        print("No entries found with that last name.")

def update():
    customer = check()
    lname = input("Please enter the last name of the entry to update: ")
    found = [entry for entry in customer if lname in entry.split(", ")[1]]
    if found:
        print("\nMatching entries:")
        for i, entry in enumerate(found):
            print(f"{i + 1}. {entry.strip()}")
        choice = int(input("Select the number of the entry to update: ")) - 1
        if 0 <= choice < len(found):
            index = customer.index(found[choice])
            fname = input("Enter new first name (or press Enter to keep current): ") or found[choice].split(", ")[0]
            phone = input("Enter new phone (or press Enter to keep current): ") or found[choice].split(", ")[2]
            email = input("Enter new email (or press Enter to keep current): ") or found[choice].split(", ")[3].strip()
            customer[index] = f"{fname}, {lname}, {phone}, {email}\n"
            save(customer)
        else:
            print("Invalid selection.")
    else:
        print("No entries found with that last name.")

def delete():
    customer = check()
    lname = input("Please enter the last name of the entry to delete: ")
    found = [entry for entry in customer if lname in entry.split(", ")[1]]
    if found:
        print("\nMatching entries:")
        for i, entry in enumerate(found):
            print(f"{i + 1}. {entry.strip()}")
        choice = int(input("Select the number of the entry to delete: ")) - 1
        if 0 <= choice < len(found):
            customer.remove(found[choice])
            save(customer)
        else:
            print("Invalid selection.")
    else:
        print("No entries found with that last name.")

# Main execution loop
if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Goodbye!")
            break
