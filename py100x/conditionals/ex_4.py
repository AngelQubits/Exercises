# Check the Weather, Part 1

import random
random_number = random.randint(0,1 + 1)


def outside():
    if random_number == 0:
	    outside = 'sunny'
    elif random_number == 1:
	    outside = 'rainy'
    else:
	    outside = 'inside'
    return outside

weather = outside()
if weather == 'sunny':
	print("It's a beautiful day!")
elif weather == 'rainy':
	print("Grab your umbrella.")
elif weather == 'inside':
	print("Let's stay inside.")
