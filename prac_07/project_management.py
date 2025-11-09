"""CP1404 Practical
Project class
"""

import datetime
from prac_07.project import Project

DEFAULT_FILE_NAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    load_projects(projects, DEFAULT_FILE_NAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE_NAME}")
    display_menu()
    user_input = input(">>> ").upper()

    while user_input != "Q":
        if user_input == "L":
            pass
        elif user_input == "S":
            pass
        elif user_input == "D":
            complete_projects, incomplete_projects = split_projects_by_completion(projects)
            print("Incomplete projects:")
            display_projects(incomplete_projects)
            if len(complete_projects) != 0:  # Check if there are completed projects
                print("Complete projects: ")
                display_projects(complete_projects)
        elif user_input == "F":
            pass
        elif user_input == "A":
            pass
        elif user_input == "U":
            pass
        else:
            print("Invalid input")

        display_menu()
        user_input = input(">>> ").upper()


def load_projects(projects, file_name, skip_header=True):
    with open(file_name, "r") as in_file:
        if skip_header:
            in_file.readline()  # Skip header
        for row in in_file:
            parts = row.strip().split("\t")  # Split rows into parts
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            projects.append(Project(*parts))
        # print(sorted(projects))


def display_menu():
    print(f"- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
          f"- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def display_projects(projects):
    projects.sort()  # Sort projects by priority
    for project in projects:
        print(f"{project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.estimated_cost}, completion: {project.percent_complete}%")


def split_projects_by_completion(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        print(project.percent_complete)
        if project.percent_complete == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    return complete_projects, incomplete_projects


main()
