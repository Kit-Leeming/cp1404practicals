"""List exercises for CP1404"""


def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

    number = get_valid_number("Enter number 1: ", int)
    while number >= 0:
        numbers.append(number)
        number = get_valid_number(f"Enter number {len(numbers) + 1}: ", int)

    print(f"The fist number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of numbers is {sum(numbers) / len(numbers)}")


def get_valid_number(print_message, number_type):
    """Get a valid number from the user"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = number_type(input(print_message))
            is_valid_input = True
        except ValueError:
            print("Invalid input")
    return number  # no problem with reference before assignment


main()
