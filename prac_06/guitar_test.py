"""Testing module for guitar class"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
washburn = Guitar("Washburn TA-80", 1982, 3205)
fender = Guitar("Fender Stratocaster", 2015, 1200)

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.4),
           Guitar("Washburn TA-80", 1982, 3205),
           Guitar("Fender Stratocaster", 2015, 1200)]

print(f"{gibson.name} get_age() - expected 103. Got {gibson.get_age()}")
print(f"{washburn.name} get_age() - expected 43. Got {washburn.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{washburn.name} is_vintage() - Expected False. Got {washburn.is_vintage()}")
