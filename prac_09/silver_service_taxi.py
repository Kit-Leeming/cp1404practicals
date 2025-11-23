"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has a fanciness attribute to scale the price per km."""
    flagfall = 4.50

    def __init__(self, name: str, fuel: int, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
