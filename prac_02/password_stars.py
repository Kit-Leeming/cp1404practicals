

def main():
    minimum_password_length = 8
    password = get_password(minimum_password_length)
    print_hidden_password(password)


def print_hidden_password(password: str, character="*"):
    print(character * len(password))


def get_password(minimum_password_length: int) -> str:
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print("Password too short")
        password = input("Password: ")
    return password


main()
