"""
Emails
Estimated time: 25 mins
Actual time:    47 mins
"""

import re


def main():
    quit_program = False
    name_to_email = {}
    while not quit_program:
        full_email = str(input("Email: "))
        if full_email == '':
            quit_program = True
        else:
            local_email_username = full_email.split("@")[0]  # Remove email host
            local_email_username = re.sub(r"\d+", "", local_email_username)  # Remove any non letter characters
            names = re.split(r"[-._]+", local_email_username)  # Split username at common delimiters
            full_name = " ".join(names).title()

            user_confirmation = input(f"Is your name {full_name}? (y/n)").lower()
            if user_confirmation == "y" or user_confirmation == "":
                name_to_email[full_name] = full_email
            elif user_confirmation == "n":
                full_name = input("Name: ")
                name_to_email[full_name] = full_email
            else:
                print("Invalid selection, please try again")

    max_name_length = max(len(name) for name in name_to_email)

    for name, email in name_to_email.items():
        print(f"{name:<{max_name_length}} ({email})")


main()
