import collections


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


@input_error
def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    return "All contacts shown."


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = collections.defaultdict(str)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
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
                raise
        except:
            print("Invalid command.")


if __name__ == "__main__":
    main()