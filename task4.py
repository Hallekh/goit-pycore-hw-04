def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    # Зберігаємо ім'я як ключ в нижньому регістрі, а оригінальне ім'я для відображення
    contacts[name.lower()] = (name, phone)
    return "Contact added."

def change_contact(args, contacts):
    name, new_number = args
    key = name.lower()
    if key in contacts:
        original_name = contacts[key][0]  # зберігаємо оригінальне написання
        contacts[key] = (original_name, new_number)
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    name = args[0]
    key = name.lower()
    if key in contacts:
        return contacts[key][1]  # повертаємо номер телефону
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "Contacts: (none)"
    result_lines = []
    for original_name, phone in contacts.values():
        result_lines.append(f"{original_name}: {phone}")
    return "Contacts:\n" + "\n".join(result_lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ("exit", "close"):
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
