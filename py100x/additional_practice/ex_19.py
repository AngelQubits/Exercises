# Checking Items off the grocery list
# Output:
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']


for x in grocery_list[0:]:
	print(grocery_list.pop(0))
    
print(grocery_list)