class Astronaut:
    """
    This is a class for astronauts.
      
    Attributes:
        name (str): The name of the astronaut.
        spaceflight_hours (int): The number of hours of space flights.
        status (str): The status: Active, Deceased, Management, Retired.

    Methods:
        __init__: Initializes new instances of the object.
        __gt__: Compares greater than.
        __ge__: Compare greather than or equal to.
        __eq__: Compares equality.
        __str__: Customizes user-displayed output.

    """

    def __init__(self, name, spaceflight_hours, status):
        self.__name = name
        self.__spaceflight_hours = spaceflight_hours
        self.__status = status

    def __gt__(self,other):
        print(f'__gt__ called - self: {self}, other: {other}')
        if (self.__spaceflight_hours > other.__spaceflight_hours):
            return self.__spaceflight_hours > other.__spaceflight_hours
        else:
            return False

    def __ge__(self,other):
        print('__ge__ called')
        if (self.__spaceflight_hours >= other.__spaceflight_hours):
            return self.__spaceflight_hours >= other.__spaceflight_hours
        else:
            return False

    def __eq__(self,other):
        print('__eq__ called')
        if (self.__spaceflight_hours == other.__spaceflight_hours):
            return self.__spaceflight_hours == other.__spaceflight_hours
        else:
            return False

    def __str__(self):
        return f'{self.__name}, {self.__status}'

# Part III: Create a List of Astronaut Objects
# Part IIIA: Read in all of the data from the CSV file. As you read in each astronaut,
# create an Astronaut object with your constructor and store this in a list.

import csv
astro_list = []
with open('astronauts.csv','r',newline='',encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        astro_row = Astronaut(row['Name'],row['Space Flight (hr)'],row['Status'])
        astro_list.append(astro_row)

# Part IIIB: List all the mutable properties for the first astronaut object

print(astro_list[0].__dict__.keys())

# Part IIIC: Pick two random Astronaut objects and compare them based on Space Flight (hr)

import random

astro1 = random.choice(astro_list) # return a random astronaut from astro_list
astro2 = random.choice(astro_list) # return a random astronaut from astro_list

print(astro1 > astro2)

print(astro1 >= astro2)

print(astro1 == astro2)

# Part IIID: Print out all astronauts from the astronaut list. Assume you cannot access
# any attributes for this print

for astronaut in astro_list: # for the entire length of the list of astronauts
    print(astronaut)