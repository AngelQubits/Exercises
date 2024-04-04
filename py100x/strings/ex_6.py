# Is Empty

def is_empty(x):
	print(True) if len(x) == 0 else print(False)


is_empty('mars')  # False
is_empty('  ')    # False
is_empty('')      # True

# pythonic solution
print()

def is_empty_too(x):
	print (not x)

is_empty_too('mars')  # False
is_empty_too('  ')    # False
is_empty_too('')      # True
