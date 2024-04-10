# Filter

# count elemets greater or equal to 100

scores = [96, 47, 113, 89, 100, 102]

# iterate through scores
# if element > 100 append to new list
# count elements in new list
new_list = [x for x in scores
         	if x >= 100]
print(len(new_list))