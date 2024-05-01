# py100-Py Basics> Loops
# Continue

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]
          
for x in cities:
	if x == None:
		continue
	print(len(x))