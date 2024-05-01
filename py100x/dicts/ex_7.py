# Multiple Cars


car = {'type': 'sedan',
       'color': 'blue',
       'year': 2003,
       }
truck = {'type': 'pickup',
         'color': 'red',
         'year': 1998,
         }
         

options = {'vehicle1': car,
           'vehicle2': truck
           }

print(type(car))
print(type(truck))
print(type(options))

# if car is the 'key' then the values can be nested dict

# Alternative solution is more clear

alternative = {'cars': {
	                'type': 'sedan',
	                'color': 'blue',
	                'year': 2003
	                },
	            'truck': {
	            	'type': 'pickup'
	            	'color': 'blue',
	            	'year': 1998
	            }
	          }