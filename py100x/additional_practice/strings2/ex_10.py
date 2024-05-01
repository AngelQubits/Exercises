# check prefix

# define a function takes two arguments
# first a full string, second part of string
# function searches if arg 1 starts with arg 2, return True if in 

def count_substrings(arg1, arg2):
	 return arg1.count(arg2)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0