"""List exercises for CP1404"""

NUMBER_OF_NUMBERS = 5


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

    for i in range(NUMBER_OF_NUMBERS):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print(f"The fist number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of numbers is {sum(numbers) / len(numbers)}")


main()
