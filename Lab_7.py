def lookup_name(employee_id):
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.split()
                if int(data[0]) == employee_id:
                    return data[1], ' '.join(data[2:])
            return "Employee not found"
    except FileNotFoundError:
        return "File not found"


def lookup_id(first_name, last_name):
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.split()
                if data[1].lower() == first_name.lower() and last_name.lower() in ' '.join(data[2:]).lower():
                    return data[0]
            return "ID not found"
    except FileNotFoundError:
        return "File not found"


def main():
    while True:
        print("Options:")
        print("1. Lookup an employee name based on ID number")
        print("2. Lookup an ID number based on an employee name")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            try:
                employee_id = int(input("Enter the ID number: "))
                first_name, last_name = lookup_name(employee_id)
                print(f"Employee Name: {first_name} {last_name}")
            except ValueError:
                print("Please enter a valid integer ID number.")
            except TypeError:
                print("Employee not found.")
        elif choice == '2':
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            result = lookup_id(first_name, last_name)
            print(f"ID number: {result}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
