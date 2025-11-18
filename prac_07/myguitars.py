"""Program to read guitar details from a csv"""

import csv
from guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    my_guitars = []
    read_guitar_csv(my_guitars)

    get_new_guitars(my_guitars)  # Get new guitars from user input, until a blank name is entered
    display_guitars(my_guitars)

    write_guitar_csv(my_guitars)


def read_guitar_csv(my_guitars):
    with open(FILE_NAME, "r", encoding="utf-8") as in_file:
        reader = csv.reader(in_file)

        for row in reader:
            # Convert year and cost into number types
            row[1] = int(row[1])  # type warning is not a problem
            row[2] = float(row[2])
            my_guitars.append(Guitar(*row))


def write_guitar_csv(my_guitars):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        for guitar in my_guitars:
            writer.writerow([guitar.name, guitar.date_of_manufacture.year, guitar.cost])


def display_guitars(my_guitars):
    """Displays the guitars that are inside guitar list"""
    maximum_name_length = max(len(guitar.name) for guitar in my_guitars)
    maximum_cost_length = max(len(str(guitar.cost)) for guitar in my_guitars)
    my_guitars.sort(reverse=True)
    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}{":":<2} {guitar.name:>{maximum_name_length}} ({guitar.date_of_manufacture.year}), worth $ "
              f"{guitar.cost:>{maximum_cost_length+1},.2f} {vintage_string}")


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
