"""Create an output text file with results for a user defined number of random scores"""
import random


def main():
    number_of_scores = get_valid_number("Enter number of random scores to generate: ", int)
    with open("results.txt", "w") as file:
        for i in range(number_of_scores):
            score = random.randint(0, 100)
            result = calculate_result(score)
            file.write(f"{score} is {result}\n")


def calculate_result(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def get_valid_number(print_message, number_type):
    """Get a valid number from the user"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = number_type(input(print_message))
            is_valid_input = True
        except ValueError:
            print("Invalid input")
    return number # no problem with reference before assignment


main()
