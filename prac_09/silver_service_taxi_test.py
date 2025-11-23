"""CP1404/CP5632 Practical - silver service taxi class testing module."""

from prac_09.silver_service_taxi import SilverServiceTaxi


my_taxi = SilverServiceTaxi("Prius 2 (silver)", 100, 2)

my_taxi.drive(18)

print(my_taxi.get_fare())
# assert my_taxi.get_fare() == 48.78
