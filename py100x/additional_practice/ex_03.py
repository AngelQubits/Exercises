# py100>pybasics>variable_scope>ex2
# Whats my value? Part 2

# will print error as python will not re-assign value to 
# outerscope variable, within the inner scope unless 'global'
# keyword is used.

x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()