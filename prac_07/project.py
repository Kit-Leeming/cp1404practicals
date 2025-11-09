"""CP1404 Practical
Project class
"""


class Project:
    """Project class"""

    def __init__(self, name, start_date, priority, estimated_cost, percent_complete):
        """Initialise a project object"""
        self.percent_complete = percent_complete
        self.estimated_cost = estimated_cost
        self.priority = priority
        self.start_date = start_date
        self.name = name

    def __repr__(self):
        """Representation of project object for debugging"""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.estimated_cost}, {self.percent_complete}"

    def __str__(self):
        """String representation of project object"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.estimated_cost}, completion: {self.percent_complete}%")

    def __lt__(self, other):
        """Determine if project has a lower priority than another project"""
        return self.priority < other.priority

    def is_start_date_after(self, filter_date):
        """Determine if project was started after a certain date"""
        return self.start_date > filter_date

    def is_complete(self):
        """Determine if project is complete"""
        return self.percent_complete == 100


if __name__ == "__main__":
    project1 = Project("project1", "9/11/2025", 2, 5000, 5)
    print(project1)
