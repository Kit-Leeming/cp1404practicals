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
        colour = input("Enter short state: ").title()


def generate_colour_dictionary():
    start_string = "<tbody><tr><td>"
    end_string = "</tbody"

    response = requests.get("https://www.color-hex.com/color-names.html")
    text = response.text

    start_index = text.find(start_string) + len(start_string)
    finish_index = text.find(end_string)

    section = text[start_index:finish_index]
    section = section.split("<tr><td>")

    pattern = re.compile(r"^(.*?)</td>.*?>(#[0-9a-fA-F]{6})<", re.DOTALL)
    color_to_hex_code = {}

    for row in section:
        match = pattern.search(row)
        if match:
            name, color = match.groups()
            color_to_hex_code[name.strip()] = color

    for i in range(800):
        print(f"'{list(color_to_hex_code)[i]}': '{list(color_to_hex_code.values())[i]}'")


main()
