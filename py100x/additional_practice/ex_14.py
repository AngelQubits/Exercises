# Capitalize Words

start = 'launch school tech & talk'
result = [] #'Launch School Tech & Talk'

# I can't work with string
# def function
# take string > split to list of words > iterate through list capitalize words.
# append the capitalized word to new list.
# take new list, define new variable = joined words into string

def upcase(string):
	slit = string.split()
	for x in slit:
		result.append(x.capitalize())
	words = ' '.join(result)
	print(words)

upcase(start)