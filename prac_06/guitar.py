"""CP1404/CP5632 Practical - guitar class."""


class Guitar:
    """Represent a Guitar object."""
    current_year = 2025

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        """Calculate the age of guitar"""
        return self.current_year - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= 50

