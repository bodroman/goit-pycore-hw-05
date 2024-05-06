def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."
    return wrapper

contacts = {}

@input_error
def add_contact(name, number):
    contacts[name] = number
    return f"Contact {name} with number {number} added."

@input_error
def change_contact(name, number):
    contacts[name] = number
    return f"Contact {name} number changed to {number}."

@input_error
def show_phone(name):
    return contacts[name]

def show_contacts():
    return contacts

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    if command == 'exit' or command == 'close':
        return 'exit'
    elif command == 'add':
        return add_contact(parts[1], parts[2])
    elif command == 'change':
        return change_contact(parts[1], parts[2])
    elif command == 'show':
        if len(parts) == 1:
            return show_contacts()
        elif len(parts) == 2:
            return show_phone(parts[1])
    else:
        return 'Invalid command.'

def main():
    print("Welcome to the Contact Assistant CLI!")
    print("Available commands:")
    print("add <name> <number>")
    print("change <name> <number>")
    print("show <name>")
    print("show")
    print("exit or close to quit")

    while True:
        user_input = input("Enter command: ")
        result = parse_input(user_input)
        if result == 'exit':
            print("Exiting program.")
            break
        else:
            print(result)

if __name__ == "__main__":
    main()
