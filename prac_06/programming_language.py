"""CP1404/CP5632 Practical - programming language class."""


class ProgrammingLanguage:
    """Represent a programming language as an object"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a programming language instance"""
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language has dynamic typing"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation of guitar object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

