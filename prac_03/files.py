# 1.
input_name = input("Enter your name: ")
file_out = open("name.txt", "w")
print(input_name, file=file_out)
file_out.close()

# 2.
file_in = open("name.txt")
name_from_file = file_in.read()
print(f"Hi {name_from_file}")
file_in.close()

# 3.
with open("numbers.txt") as file_in:
    result = int(file_in.readline().strip()) + int(file_in.readline().strip())
    print(result)

# 4.
with open("numbers.txt") as file_in:
    numbers = []
    for number in file_in.read().split():
        numbers.append(int(number))
    total = sum(numbers)
    print(total)
