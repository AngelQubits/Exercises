#py100-pybasics>strings>is empty? problem 6


# Write a function that checks whether a string is empty or not
def is_empty(string):
	return not len(string) > 0
	
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

def empty(string):
	return not string
print()
print(empty('mars'))  # False
print(empty('  '))    # False
print(empty(''))      # True	