# py100 basics > prob 9 - Divided by twp

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

# for x in dict 
# create empty list
# for oop append to list if odd
half_numbers = []

for x in numbers.values():
	half_numbers.append(x // 2)
return half_numbers