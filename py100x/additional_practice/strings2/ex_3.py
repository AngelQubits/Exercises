# Ignoring Case

name = 'Roger'
new_name = 'RoGer'

print(name == new_name)
print()
print(name.casefold() == new_name.casefold())
print()
print(name == 'DAVE')
print()
print(name.casefold() == 'Dave'.casefold())