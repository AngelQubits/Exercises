# Transformation
s1 = 'Captain Ruby'
print(s1)
print()
s1 = s1.split(' ')
#print(s1)

s1[1] = 'Python'

#print(s1)
#print(type(s1))

s1 = str(s1[0]) + ' ' + str(s1[1])
print(s1)
print(type(s1))

#solution

new_s1 = 'Captain Ruby'.replace('Ruby', 'Python')
print(new_s1)