# Pig Latin Translator
string = "Python World"
# def function takes string as arg
# split string into list of words
# iterate through words on list remove/replace first letter
# append to end of list + add 'ay' at end of word
# join list back to string
# output = "ythonPay orldWay

def pig(string):
	words = string.split(' ')
	result = []
	for x in words:
		result.append(x[1:] + list(x).pop(0) + "ay")
	ouput =" ".join(result)
	print(ouput)

pig(string)