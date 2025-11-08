"""CP1404/CP5632 Practical - guitar class."""
import datetime
from dateutil.relativedelta import relativedelta

VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance"""
        self.name = name
        self.date_of_manufacture = datetime.date(year, 1, 1)
        self.cost = cost

    def __repr__(self):
        """Return string representation of guitar"""
        return f"{self.name} ({self.date_of_manufacture.year}) : ${self.cost:,}"

    def __lt__(self, other):
        return self.date_of_manufacture > other.date_of_manufacture

    def get_age(self):
        """Calculate the age of guitar"""
        age = relativedelta(datetime.date.today(), self.date_of_manufacture)
        return age.years

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE


if __name__ == "__main__":
    guitar1 = Guitar("Fender", 2012, 700)
    guitar2 = Guitar("Washburn", 1988, 3400)
    print(guitar1)
    print(guitar1.get_age())
    print(guitar1.is_vintage())
    print(guitar1 < guitar2)
