minimum_password_length = 8
password = input("Password: ")
while len(password) < minimum_password_length:
    print("Password too short")
    password = input("Password: ")
print("*" * len(password))
