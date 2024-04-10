# Checking items off the grocery list:

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']
length = len(grocery_list)
start = 0

while start < length:
	print(grocery_list[0])
	grocery_list.pop(0)
	start += 1

print(grocery_list)




#print(grocery_list)

# iterate through the list, pop out the element and print return
