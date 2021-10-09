                                    # Password generator #
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
numbers = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', "@", '#', '$', '^', '*', "&", '(', ")"]

total_letters = int(input("no.of letters in your password\n"))
no_of_alphabets = int(input(f"choose alphabet number bellow {total_letters}\n"))
if no_of_alphabets > total_letters:
    print("Error")
no_of_numbers = int(input(f"choose numbers number bellow {total_letters - no_of_alphabets}\n"))
if no_of_numbers > total_letters - no_of_alphabets:
    print("Error")
no_of_symbols = total_letters - no_of_numbers - no_of_alphabets

create = True
while create:

    password_alphabet = random.choices(population=alphabets, k=no_of_alphabets)
    password_number = random.choices(population=numbers, k=no_of_numbers)
    password_symbols = random.choices(population=symbols, k=no_of_symbols)
    password_letters = password_symbols + password_alphabet + password_number

    easy_hard = input("Select Easy password or hard password type 'E' for easy or 'H' for hard\n").lower()

    password = ''
    if easy_hard == "e":
        password = password.join(password_letters)
        print(password)

    if easy_hard == "h":
        random.shuffle(password_letters)
        password = password.join(password_letters)
        print(password)

    create = input('type "T" to change password\n').lower()
    if create == "t":
        create = True
    else:
        break
