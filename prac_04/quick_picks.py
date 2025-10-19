import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_lines = get_valid_number("How man quick picks?: ", int)
    for i in range(number_of_lines):
        quick_pick_line = []
        while len(quick_pick_line) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick_line:
                quick_pick_line.append(number)
                print(f"{quick_pick_line[-1]:>2}", end=" ")
        print()


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
