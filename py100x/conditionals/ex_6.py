# Check the Weather, Part 2
# Note match case not compatible with this version

weather = 'sunny'
match weather:
	case 'sunny':
	    print("It's a beautiful day!")
    case 'rainy':
	    print("Grab your umbrella.")
    case_:
     	print("Let's stay inside.")
