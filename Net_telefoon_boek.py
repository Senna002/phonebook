entries = []
temporary_numbers = []
error_message_number = "I think you may have made a typo, please enter your number"


def menu():
    menu_list = [{"option": "option 1: List all entries", "key_input": "1", "program": all_entries},
                 {"option": "option 2: Add a new entry", "key_input": "2", "program": add_entry},
                 {"option": "option 3: Remove entry", "key_input": "3", "program": remove_entry},
                 {"option": "option 4: Close program", "key_input": "4", "program": exit},
                 ]

    while True:
        print("You have the following options: ")
        for options in menu_list:
            print(options["option"])
        command = input("please choose an option: 1, 2, 3, 4: ")
        for options in menu_list:
            if command == options["key_input"]:
                options["program"]()


def validate_name(name):
    while True:
        check_name = name.replace(' ', '').replace('-', '')
        if check_name and check_name.isalnum():
            return True
        else:
            print("I think you may have made a typo, please enter your name")
            return False


def validate_phone(phone_number):
    while True:
        if phone_number.isdigit():
            if phone_number.startswith('06') or phone_number.startswith('0031'):
                if len(phone_number) in range(10, 13):
                    return True
                print(error_message_number)
                return False
            print(error_message_number)
            return False
        else:
            print(error_message_number)
            return False


def double_number(phone_number):
    while True:
        for entry in entries:
            if entry['Phone'] == phone_number:
                print("This phone number already exists, please choose another")
                return False
        return True


def validate_mail(email):
    if email:
        while True:
            sub_strings = email.split('@')
            if len(sub_strings) == 2:
                if '.' not in sub_strings[1]:
                    print("I think you may have made a typo, please enter your email.")
                    return False
            if '@' in email:
                return True
            print("I think you may have made a typo, please enter your email.")
            return False


def double_mail(email):
    if email:
        while True:
            for entry in entries:
                if entry['mail'] == email:
                    print("This email already exists, please choose another.")
                    return False
            return True


def no_email_entered(email):
    if not email:
        while True:
            no_email = input("Do you want to leave your email empty? Type 'yes' or 'no': ").lower()
            if no_email == 'yes':
                print("We are now adding your information")
                return True
            elif no_email == "no":
                print("In that case, please enter your email")
                return False
            print("Please choose 'yes' or 'no'")


def check_adding(name, email, phone_number):
    while True:
        check_entry = input(f"You are adding the following information: "
                            f"{name.title()}, {phone_number}, {email}"
                            f". Do you want to continue? Type 'yes' or 'no': ").lower()
        if check_entry == "yes":
            print("We are now adding your information.")
            temporary_numbers.append(phone_number)
            entries.append({'Names': name.title(), 'mail': email, 'Phone': phone_number})
            return True
        elif check_entry == "no":
            print("You are now returning to the options menu")
            return True
        print("Please choose 'yes' or 'no'")


def all_entries():
    if not entries:
        print('No entries were found')
    for entry in entries:
        print(entry)


def add_entry():
    while True:
        name = input('Please enter your name: ').upper()
        if validate_name(name=name):
            break
    while True:
        phone_number = input('Please enter your phone number: ').replace(' ', '').replace('-', '').replace('+', '00')
        if validate_phone(phone_number=phone_number):
            if double_number(phone_number=phone_number):
                break
    while True:
        email = input('Please enter your email: ').lower()
        if no_email_entered(email=email):
            break
        if email and double_mail(email=email):
            if validate_mail(email=email):
                break
    while True:
        if check_adding(name=name, phone_number=phone_number, email=email):
            return


def remove_entry():
    number_to_remove = input("Please enter your phone number to remove your information: ") \
        .replace(' ', '').replace('-', '').replace('+', '00')
    if number_to_remove not in temporary_numbers:
        print("Entry not found")
    for entry in entries:
        if entry["Phone"] == number_to_remove:
            entries.remove(entry)
            temporary_numbers.remove(number_to_remove)
            print("Your information is now removed")
            break


if __name__ == "__main__":
    menu()
