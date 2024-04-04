# What's my value? (Part 5)
# will print '1', as it will first reference the
# outerscope value, before changing the variable to 2.

# Solution:
# You get a type error, because python notices a variable
# is being defined within the function; whereas it would normally
# recognize the outserscope variable if it weren't being re-assigned
# from within the function scope.