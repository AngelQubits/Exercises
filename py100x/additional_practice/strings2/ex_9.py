# check prefix

# define a function takes two arguments
# first a full string, second part of string
# function searches if arg 1 starts with arg 2, return True if in 

def starts_with(arg1, arg2):
	 return arg1.startswith(arg2)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True