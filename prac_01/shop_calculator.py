"""
Calculator that will find the total price for a number of differently priced items
and apply a 10% discount for orders with a total price over $100
"""

total = 0
item_prices = []
number_of_items = int(input("Please enter the number of items: "))

while number_of_items < 0:
    number_of_items = int(input("""Invalid number of items!
    Please enter the number of items: """))

for i in range(number_of_items):
    item_price = float(input(f"Please enter the price for item {i + 1}: "))
    item_prices.append(item_price)
total = sum(item_prices)
if total > 100:
    total = total * 0.9
print(f"""--------------------------------------
Number of items: {number_of_items}""")
for i in range(number_of_items):
    print(f"Price of item: {item_prices[i]}")
print(f"Total price for {number_of_items} is ${total}")


# -----------------------------------------------------
# Shop Calculator V2 (The all new and improved version)
# -----------------------------------------------------

# total = 0
# number_of_items = 0
# item_prices = []
# user_input = float(input("""To calculate the total enter -1
# Please enter the price for item 1: """))
# item_prices.append(user_input)
# if user_input != -1:
#     number_of_items += 1
#     total = total + user_input
#
# while user_input != -1:
#     user_input = float(input(f"Please enter the price for item {number_of_items + 1}: "))
#     item_prices.append(user_input)
#     number_of_items += 1
# total = sum(item_prices) + 1
# if total > 100:
#     total = total * 0.9
# print(f"""--------------------------------------
# Number of items: {number_of_items - 1}""")
# for i in range(number_of_items - 1):
#     print(f"Price of item: {item_prices[i]}")
# print(f"Total price for {number_of_items - 1} is ${total}")

