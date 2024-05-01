# Reverse Word Order

# def function takes single argument string
# convert list into string separated by words
# reverse the order of the sequence
# convert back to string in new var
# output = string in reversed word order

string = "hello gorld"
def inverse(string):
	new_string = string.split(' ')
	new_string.sort(reverse= True)
	output = ' '.join(new_string)
	print(output)

inverse(string)

string = "hello gorld"

# .sort vs .reverse: 
# .sort re-orders based on lexigraphical order
# .reverse re-orders based on position of the element

def inverse(string):
    new_string = string.split(' ')
    new_string.reverse()  
    output = ' '.join(new_string)
    print(output)

inverse(string)
