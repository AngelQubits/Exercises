# Checking Key Existence

student = {
    'id': 123,
    'grade': 'B',
}

print(student.get('name'))
print(student.get('grade'))

# I used get which returns none if not found.
# Using the 'in' keyword helps return a bool value.

print('name' in student)
print('grade' in student)