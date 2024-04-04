# Ignoring Case
name = 'Roger'

# part 1

if name.lower() == 'RoGer'.lower():
	print(True)
else:
	print(False)
	
# part 2
if name.lower() == 'DAVE'.lower():
	print(True)
else:
	print(False)
	
# Solution: str.casefold()
	
if name.casefold() == 'RoGer'.casefold():
	print(True)
else:
	print(False)