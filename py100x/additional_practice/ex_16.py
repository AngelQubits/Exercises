# Every Other Word

# def function takes string as arg
# split string to list (split)
# iterate through the list skiping one [0:-1:1]
# append to newly assigned list
# join list back into new string

def splitstring (arg):
	lst = arg.split(' ')
	start = 0
	new_list = []
	for x in lst[0:len(lst):2]:
		new_list.append(x)
	output = ' '.join(new_list)
	
	print(output)

splitstring("one two three four five")