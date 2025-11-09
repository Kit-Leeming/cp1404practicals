"""CP1404 Practical
Estimated: 1:15
Actual:
"""

import datetime


class Project:
    """Project class"""

    def __init__(self, name, start_date, priority, estimated_cost, percent_complete):
        self.percent_complete = percent_complete
        self.estimated_cost = estimated_cost
        self.priority = priority
        self.start_date = start_date
        self.name = name

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.estimated_cost}, {self.percent_complete}"

    def __lt__(self, other):
        return self.priority < other.priority


if __name__ == "__main__":
    project1 = Project("project1", "9/11/2025", 2, 5000, 5)
    print(project1)
