"""
CP1404/CP5632 Practical
Colour names to hex code program
"""

import requests
import re

COLOUR_NAME_TO_HEX_CODE = {'Acid Green': '#b0bf1a', 'Beige': '#f5f5dc', 'Black': '#000000', 'Blue Bell': '#a2a2d0',
                           'Ebony': '#555d50', 'Emerald': '#50c878', 'Grullo': '#a99a86', 'Lemon Curry': '#cca01d',
                           'Peach': '#ffe5b4', 'Raspberry': '#e30b5d'}


def main():
    colour = input("Enter colour: ").title()
    while colour != "":
        try:
            print(colour, "is", COLOUR_NAME_TO_HEX_CODE[colour])
        except KeyError:
            print("Invalid colour")
        colour = input("Enter colour: ").title()


"""Extended work below"""

def generate_colour_dictionary():
    """Generate colour dictionary from colour hex website"""
    start_string = "<tbody><tr><td>"
    end_string = "</tbody"

    response = requests.get("https://www.color-hex.com/color-names.html")
    text = response.text

    start_index = text.find(start_string) + len(start_string)  # Find start of colour codes on page
    finish_index = text.find(end_string)

    section = text[start_index:finish_index]  # Extract section of web page that contains colour information
    colours = section.split("<tr><td>")  # Split into list with each colour as an entry

    pattern = re.compile(r"^(.*?)</td>.*?>(#[0-9a-fA-F]{6})<", re.DOTALL)  # Create pattern for colour information
    color_to_hex_code = {}

    for colour in colours:
        match = pattern.search(colour)
        if match:
            name, color = match.groups()  # Extract the colour and hex code
            color_to_hex_code[name.strip()] = color

    for i in range(800):  # Print the first 800 colours and their codes
        print(f"'{list(color_to_hex_code)[i]}': '{list(color_to_hex_code.values())[i]}'")


main()
