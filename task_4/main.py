def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        print(f"Contact added.")
    except ValueError:
        print("Command ADD should have this structure: 'Add <name> <phone_number>'")

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            print(f"Contact updated.")
        else: 
            print(f"Name '{name}' wasn't found in the contact list.")
    except ValueError:
        print("Command CHANGE should have this structure: 'Change <name> <phone_number>'")

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            print(f"{contacts[name]}")
        else: 
            print(f"Name '{name}' wasn't found in the contact list.")
    except IndexError:
        print("Command PHONE should have this structure: 'Phone <name>'")

def show_all(contacts):
    if contacts:
        print("Contacts list:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Contact list is empty.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
