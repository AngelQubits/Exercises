# First Element

# define a function called first takes list as argument
# if list is empty it should return empty
# else return first element of list.

def first(arg):
	if len(arg) == 0:
		return "Empty List"
	else:
		return arg[0]
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))