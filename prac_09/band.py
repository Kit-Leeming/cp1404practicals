"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class for storing details of a band, such as name and players."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Format string representation of the band name and its members and their details"""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add new musicians to the band"""
        self.musicians.append(musician)

    def play(self):
        """Print what each member of the band is playing"""
        return "\n".join(musician.play() for musician in self.musicians)

