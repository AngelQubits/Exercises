# Last Element

def last(arg):
	if arg:
		return arg[-1]
	else:
		return "Empty List"
print(last(['Earth', 'Moon', 'Mars']))  # Earth
print(last([]))