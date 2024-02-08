entries = []
database = []
option = []
temporary = []


# add_entry starts with a wile loop to check the name. The name can not be empty.
# It also has a show_name. which keeps names separated with '-' if multiple names are added.
# Name then sticks the names back together to keep the data in the database easy to work with
# then add_entry has a loop to check for phone number. It has to be a number, start with 06 or 31, and it has to have
# 10 or 11 numbers in it.
# Then there is a nested while loop. The outer loop checks for email. There has to be a @ in the email,
# and after that there has to be a '.' There also can not be double email addresses in entries
# The inner loop checks if you are sure you want to add. And then adds the information.
# The final loop checks if you want to leave email empty.

def add_entry():
    while True:
        show_name = input('Please enter your name: ').lower()
        name = show_name.replace(' ', '').replace('-', '')
        if name and name.isalnum():
            break
        else:
            print("I think you may have made a typo, please enter your name")
    while True:
        phone_number = input('Please enter your phone number: ').replace(' ', '').replace('-', '').replace('+', '')
        if phone_number.isdigit() and (phone_number.startswith('06') or phone_number.startswith('31'))\
                and (len(phone_number) == 10 or len(phone_number) == 11):
            break
        else:
            print('I think you may have made a typo, please enter your number')
    while True:
        email = input('Please enter your email: ').lower()
        sub_string = email.split('@')
        if len(sub_string) == 2 and '@' in email:
            if email in temporary:
                print("This email already exists, please choose another.")
            elif '.' not in sub_string[1] and email:
                print("I think you may have made a typo, please enter your email.")
            else:
                while True:
                    check_adding = input(f"You are adding the following information: "
                                         f"{show_name}, {phone_number}, {email}"
                                         f". Do you want to continue? Type 'yes' or 'no': ")
                    if check_adding == "yes".lower():
                        print("We are now adding your information.")
                        temporary.append(email)
                        entries.append({'Names': show_name, 'mail': email, 'Phone': phone_number})
                        database.append({'Names': name, 'mail': email, 'Phone': phone_number})
                        return
                    elif check_adding == "no".lower():
                        print("You are now returning to the options menu")
                        return
                    else:
                        print("Please choose 'yes' or 'no'")
        else:
            while True:
                no_email = input("Do you want to leave your email empty? Type 'yes' or 'no': ")
                if no_email == 'yes'.lower():
                    print("We are now adding your information")
                    entries.append({'Names': show_name, 'mail': email, 'Phone': phone_number})
                    database.append({'Names': name, 'mail': email, 'Phone': phone_number})
                    return
                elif no_email == "no".lower():
                    print("In that case, please enter your email")
                    break
                else:
                    print("Please choose 'yes' or 'no'")


def all_entries():
    if option == '0':
        if not database:
            print("No data was found")
        for data in database:
            print(data)
    elif option == '1':
        if not entries:
            print('No entries were found')
        for entry in entries:
            print(entry)


# The first while loop checks what option you want.
# Option 3 allows you to remove an entry. You first input the email that belongs to the entry you want removed
# Then you get the values belonging to the keys mail out of the dictionary,
# and compare them with the input you just gave.
# This line rewrites the list 'entries' without the entry belonging to the email you want removed.
# Then it checks if the email to be removed is in the temporary list that checks for double email.
# If it is, it removes it

while True:
    print("These are your options:\n option 1: List all entries\n option 2: Add a new entry"
          "\n Option 3: Remove your entry\n option 4: close the program")
    option = input("Please choose a number to move forward: ")
    if option == '4':
        break
    elif option == '0':
        all_entries()
    elif option == '1':
        all_entries()
    elif option == '2':
        add_entry()
    elif option == '3':
        while True:
            remove_email = input("Please enter your email to remove your information: ").lower()
            name_to_remove = input("Please enter your name as well: ").lower()
            for dictionary in entries:
                if name_to_remove in dictionary.values():
                    if remove_email in temporary:
                        entries = [entry for entry in entries if entry.get('mail') != remove_email]
                        database = [data for data in database if data.get('mail') != remove_email]
                        temporary.remove(remove_email)
                        print(f"Your information is now removed, {name_to_remove}")
                    else:
                        print(f"This email has not been found: {remove_email}")
            break
    else:
        print("That is not a supported number within this program, please choose another number")

