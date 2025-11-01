"""
CP1404/CP5632 Practical - guitar catalog program
Started: 1:15
Estimated: 45 mins
Actual: 55 mins
"""

from prac_06.guitar import Guitar


def main():
    """Program to ask user to input guitar details, before displaying those details"""
    print("my guitars!")
    my_guitars = []
    get_new_guitars(my_guitars)
    display_guitars(my_guitars)


def display_guitars(my_guitars):
    """Displays the guitars that are inside guitar list"""
    maximum_name_length = max(len(guitar.name) for guitar in my_guitars)
    maximum_cost_length = max(len(str(guitar.cost)) for guitar in my_guitars)
    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars, 1):
        vintage_string = "(vintage)" if guitar.get_age() >= 50 else ""
        print(f"Guitar {i}{":":<2} {guitar.name:>{maximum_name_length}} ({guitar.year}), worth $ "
              f"{guitar.cost:,>{maximum_cost_length}} {vintage_string}")


def get_new_guitars(my_guitars):
    """Will keep getting new guitar details from user until a blank name is input"""
    name = input("Name: ")
    while name != "":
        year = get_valid_positive_number("Year: ", int)
        cost = get_valid_positive_number("Cost: ", float)
        my_guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")
        name = input("Name: ")
    print(f"... snip ...\n")


def get_valid_positive_number(print_message, number_type):
    """Get a valid number from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = number_type(input(print_message))
            if number > 0:
                is_valid_input = True
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # no problem with reference before assignment


main()
