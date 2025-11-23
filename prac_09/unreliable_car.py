"""
CP1404/CP5632 Practical
Car class
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < random.randint(1, 100):
            super().drive(distance)
