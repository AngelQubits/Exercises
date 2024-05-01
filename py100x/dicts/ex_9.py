# Divided by Two

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}


half_numbers = [int(x / 2) for x in numbers.values()]
print(half_numbers)
