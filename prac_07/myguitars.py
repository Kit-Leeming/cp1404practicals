"""Program to read guitar details from a csv"""

import csv
from guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    guitars = []
    read_guitar_csv(guitars)
    guitars.sort(reverse=True)
    print(guitars)


def read_guitar_csv(guitars):
    with open(FILE_NAME, "r") as in_file:
        in_file.readline()  # Skip header
        reader = csv.reader(in_file)

        for row in reader:
            # Convert year and cost into number types
            row[1] = int(row[1])  # type warning is not a problem
            row[2] = float(row[2])
            guitars.append(Guitar(*row))


main()
