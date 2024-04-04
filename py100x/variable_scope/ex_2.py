# What's my value? (Part 2)
# print 15

# Lesson: we can access global variables locally, but can't reassign them
# unless we use keyword 'global'

# here we are accessing global variable locally to print.

x = 10

def my_function():
    print(x)

my_function()

# here we are accessing global variable locally, and reassigning it new value
# both locally and globally. Note use of 'global' keyword. Prints 15

x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()

# Here we are raising the error, because python cannot re-assign global variable
# locally without the 'global' keyword.  As shown above, it can access it
# however, it can't re-assign it.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()