# Pets
# Solution: She was reassigning 'bowser' as they value for dog key
# instead, appending 'bowser' to the list value for dog key works better

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}