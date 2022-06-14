# Create a dictionary called cities, use the names of three cities as keys.
# Create a dictionary of information about each cities pop, state, and year.
# Print city and all the values. Print the cities by year.

from collections import OrderedDict  # importing a few methods to use for sorting
from operator import getitem

cities = {'boston' : {'state': 'massachusetts', 'population': 692600, 'founded': '1630'},
          'miami' : {'state': 'florida', 'population': 467963, 'founded': '1825'},
          'jacksonville': {'state': 'North Carolina', 'population': 72436, 'founded': '1757'}, }

# new 'sorted' list where i use OrderedDict() and Sorted() to sort the nested dictionary
sorted_cities = OrderedDict(sorted(cities.items(), key=lambda x :getitem(x[1], 'founded')))

for city, city_info in sorted_cities.items () :  # use a simple for loop to print the sorted dictionary.
    print(f'City:{city.title ()}')
    print(f'State: {city_info["state"].title ()}, Population: {city_info["population"]}, '
            f'Year Founded: {city_info["founded"]}\n')
