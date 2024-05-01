# py100-pybasis> dicts> prob. 7

# Nested Dicts

from pprint import pprint
vehicle = {'car': {
	'type': 'sedan',
    'color': 'blue',
    'year': 2003},
    
'truck': {
	    'type': 'pickup',
	    'color': 'red',
	    'year': 1998}
}

pprint(vehicle.keys())