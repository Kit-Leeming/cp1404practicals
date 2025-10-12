""" Main menu task to get valid score, print score results, and print score as stars"""


def main():
    score = get_valid_score()
    print_main_menu()
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = get_valid_score()
        elif user_choice == "P":
            result = calculate_result(score)
            print(f"{result} (Press enter to continue)")
            input()
        elif user_choice == "S":
            print_stars_score(score)
            print("(Press enter to continue)")
            input()
        else:
            print("Invalid command \n")
        print_main_menu()
        user_choice = input(">>> ").upper()
    print("Program finished")


def print_main_menu():
    print("""(G)et a valid score
(P)rint results
(S)how stars
(Q)uit Program""")


def get_valid_score(score=None):
    is_valid_input = False
    while not is_valid_input:
        try:
            score = float(input("Enter score: "))
            if score < 0 or score > 100:
                print("Invalid score")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid score")
    return score


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


def print_stars_score(score: float):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        score = round(score)
        print("*" * score)


main()
