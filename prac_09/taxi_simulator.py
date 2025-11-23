"""CP1404/CP5632 Practical - taxi simulator program."""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    """Taxi simulator program"""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_taxi = None

    print("Let's drive!")
    display_main_menu()
    user_input = input(">>> ").upper()

    while user_input != "Q":
        if user_input == "C":
            print("Taxis available: ")
            display_taxi_list(taxis)
            choice = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(choice)]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif user_input == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()  # Start a new fare for the next drive
                distance = get_valid_positive_number("Drive how far? ", int)
                current_taxi.drive(distance)
                bill_to_date += current_taxi.get_fare()  # Add fare to bill to date
                print(f"Your {current_taxi.name} trip cost you {current_taxi.get_fare()}")

        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        display_main_menu()
        user_input = input(">>> ").upper()

    print(f"Total trip cost: ${bill_to_date:.2f}\nTaxis are now:")
    display_taxi_list(taxis)


def display_taxi_list(taxis: list[Taxi | SilverServiceTaxi]):
    """Display a list of taxis with indexes"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def display_main_menu():
    """Display the menu text"""
    print("q)uit, c)hoose taxi, d)rive")


def get_valid_positive_number(print_message, number_type):
    """Get a valid number of a type from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = input(print_message)
            number = number_type(user_input)
            if number > 0:
                is_valid_input = True
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # no problem with reference before assignment


main()
