# Capitalize Words

# define function takes a string as argument
# take string, split and iterate through words
# string convert to list to make maneagable
# iterate through list and capitalize words
# add capitalized words to new list
# join list of capitalized words into new string
# return / print new string

string = 'launch school tech & talk'
words = []

def upcase(string):
	lstring = string.split(' ')
	for word in lstring:
		words.append(word.capitalize())
upcase(string)
result = ' '.join(words)  
print(result)