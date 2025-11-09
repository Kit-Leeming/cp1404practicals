"""CP1404 Practical
Project class
"""

import datetime
from prac_07.project import Project

DEFAULT_FILE_NAME = "projects.txt"
REMOVE_EXISTING_PROJECTS_ON_LOAD = False


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    load_projects(projects, DEFAULT_FILE_NAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE_NAME}")
    display_menu()
    user_input = input(">>> ").upper()

    while user_input != "Q":

        if user_input == "L":  # Load new projects into memory
            file_name = input("Enter filename to load data from: ")
            if REMOVE_EXISTING_PROJECTS_ON_LOAD:
                projects = []
            load_projects(projects, file_name)

        elif user_input == "S":  # Save projects to .txt file
            file_name = input("Enter filename to save data to: ")
            save_projects(projects, file_name)

        elif user_input == "D":  # Display projects
            complete_projects, incomplete_projects = split_projects_by_completion(projects)
            print("Incomplete projects:")
            display_projects(incomplete_projects)
            if len(complete_projects) != 0:  # Check if there are completed projects
                print("Complete projects: ")
                display_projects(complete_projects)

        elif user_input == "F":
            filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = []
            for project in projects:
                if project.is_start_date_after(filter_date):
                    filtered_projects.append(project)
            display_projects(filtered_projects)

        elif user_input == "A":
            add_project(projects)

        elif user_input == "U":
            display_projects(projects, True)
            project_choice = get_valid_positive_number("Project choice: ", int)
            display_projects(projects[project_choice])
            new_percentage = get_valid_positive_number("New Percentage: ", int, True, True)
            new_priority = get_valid_positive_number("New Priority: ", int, True, )
            if new_percentage:
                projects[project_choice].percent_complete = new_percentage
            if new_priority:
                projects[project_choice].priority = new_priority

        else:
            print("Invalid input")

        display_menu()
        user_input = input(">>> ").upper()
    if input("Would you like to save to projects.txt? ").upper() in ("Y", "YES"):
        save_projects(DEFAULT_FILE_NAME, projects)
        print("Projects saved")
    print("Thank you for using custom-built project management software")


def add_project(projects):
    name = input("Let's add a new project\nName: ")
    start_date = get_valid_date("Start date(dd/mm/yy): ")
    priority = get_valid_positive_number("Priority: ", int)
    cost_estimate = get_valid_positive_number("Cost estimate: $", float, False, True)
    percent_complete = get_valid_positive_number("Percent complete: ", int, False, True)
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


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


def save_projects(projects, file_name,
                  header=("Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage")):
    """Save projects to text file with default header"""
    with open(file_name, "w") as out_file:
        out_file.write("\t".join(header) + "\n")
        for project in projects:
            line = (f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}"
                    f"\t{project.estimated_cost}\t{project.percent_complete}\n")
            out_file.write(line)


def display_menu():
    print(f"- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
          f"- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def display_projects(projects, show_index=False):
    if not isinstance(projects, list):  # If projects only contains one project, convert it to a list
        projects = [projects]
    projects.sort()  # Sort projects by priority
    for i, project in enumerate(projects):
        index_string = f"{i} " if show_index else ""
        print(f"{index_string}{project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.estimated_cost}, completion: {project.percent_complete}%")


def split_projects_by_completion(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    return complete_projects, incomplete_projects


def get_valid_positive_number(print_message, number_type, return_blank=False, is_0_valid=False):
    """Get a valid number of a type from the user. Return None, when return_blank is True"""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = input(print_message)
            if user_input == "" and return_blank:
                return None
            number = number_type(user_input)
            if number > 0 or is_0_valid:
                is_valid_input = True
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # no problem with reference before assignment


def get_valid_date(print_message, date_format="%d/%m/%y"):
    """Get a valid date from user"""
    is_valid_date = False
    while not is_valid_date:
        try:
            date = datetime.datetime.strptime(input(print_message), date_format).date()
            is_valid_date = True
        except ValueError:
            print("Invalid date")
    return date  # no problem with reference before assignment


main()
