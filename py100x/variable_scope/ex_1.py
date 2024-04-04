# What's My value? (Part 1)
# answer: nothing as variable defined in inner scope.

if True:
    my_value = 20

#print(my_value)

#Lesson: variables defined inside an if statement can be accessed outside
# of that block.

def my_variable():
	your_value = 21

#print(my_value)
#print(your_value)

# while this is the case for an if statement, obviously not the case for a 
# function.

# if False, I believe it will also return the value within the block. As
# the boolean value is not the limitation here.

if False:
    my_new_value = 42

print(my_new_value)

# Answer: because its false, python doesn't know the new variable exists.