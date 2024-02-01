def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    name = args[0]
    #Search for an entity in the list with a key equal to name
    for key in contacts:
        if key == name:
            #Change value for entity with key = name
            contacts[name] = phone
            return "Contact is successfully changed."
    #Return error message in case if name is not found
    return ("No such contact")

def show_phone(args, contacts):
    name = args[0]
    #Search for an entity in the list with a key equal to name
    for key in contacts:
        if key == name:
            #Return key value from dictionary
            return (contacts[key])
    #Return error message in case if name is not found
    return ("No such contact")
        
def show_all(contacts):
    #Create an empty list to store the values
    all_list = []
    if contacts:

        for key,value in contacts.items():
            #Add a string to the list
            all_list.append(f"{key} - {value}")
        #Return a list as a string separated by a newline
        return '\n'.join(all_list)
    else:
        #Return error in case if list is empty
        return ("No contacts in the list")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()