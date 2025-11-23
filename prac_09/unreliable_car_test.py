"""CP1404/CP5632 Practical - unreliable car class testing module."""

from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("V8 Potato", 100, 50)
for i in range(100):
    my_car.drive(1)
print(my_car.fuel)

