#py100>pybasics>Lists-problem #9

# existing list, check to see if 'x' is in list, return True or False

# define function takes two arguments first string, second list
# function will search through list, return true if found, return false if not

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(search, cities):
	return cities.count(search) > 0

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False