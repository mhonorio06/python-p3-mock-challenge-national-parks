#!/usr/bin/env python3
import ipdb
import random

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
national_park = NationalPark("Yosemite")
national_park2 = NationalPark("YellowStone")
national_park3 = NationalPark("Wolfe") 

national_park_list = [national_park, national_park2, national_park3]

# national_park.best_visitor = "Victor"
# ipdb.set_trace()
visitor = Visitor("Victor")
visitor2 = Visitor("Denise")
visitor3 = Visitor("Angel")
visitor4 = Visitor("Dan")

visitor_list = [visitor, visitor2, visitor3, visitor4]


# trip = Trip(visitor, "Yosemite", )
for i in range(5):
    Trip(visitor_list[random.randint(0,3)], national_park_list[random.randint(0,2)], "08-13-2024", "08-13-2024")

national_park.best_visitor()
