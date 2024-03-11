# Large Numbers

print('documentation is not found under literals, but under lexical analysis')
print('lexical analysis is like understanding grammar in python, find it here:')
print('https://docs.python.org/3/reference/lexical_analysis.html#index-0')

print()
print('Further Exploration: ')
# Yes, underscore can break up numbers any way, python
# will still read as a numeric value
print(1000 == 1000)    #True
print(1_000 == 1000)   #True 
print(1_000 == 10_00)  #True
print(1_000 == 100_0)  #True