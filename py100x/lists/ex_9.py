# Travel
# define function contains takes two args
# function checks if argument is in list(arg2)
# if contained in list returns True if not false
# do not use in operator[rewrite with in operator - Extra]

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
                
def contains(arg1, arg2):
	if arg2.count(arg1) > 0:
		print(True)
	else:
		print(False)

contains('Barcelona', destinations)  
contains('Nashville', destinations)  


def contain(item, lst):
    return lst.count(item) > 0

print(contain('Barcelona', destinations))  
print(contain('Nashville', destinations))  