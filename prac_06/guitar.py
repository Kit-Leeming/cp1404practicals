"""CP1404/CP5632 Practical - guitar class."""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

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
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
