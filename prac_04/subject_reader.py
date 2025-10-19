"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects_details = load_data(FILENAME)
    print_subject_report(subjects_details)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    file_data = []
    for line in input_file:
        parts = line.strip().split(',')  # Remove the \n and separate each value
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        file_data.append(parts)
    input_file.close()
    return file_data


def print_subject_report(subjects_details: list):
    """Print subject details from a list with each element
    formatted like: [subject code, lecturer, number of students]"""
    for subject in subjects_details:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
