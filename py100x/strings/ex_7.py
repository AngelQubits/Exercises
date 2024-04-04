# Is empty or Blank?

def is_empty_or_blank(x):
	if x.isalnum() == True:
		return(False)
	elif x.isspace() == True:
		return(True)
	elif x == '':
		return(True)
	

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# Part of my issue is not understanding problem deeply enough
# going straight into coding, rather than seeifing if there are
# other possible solutions through the use of methods and built in
# functions.

# Solution:
def is_empty_or_blanks(s):
    return not s.strip(' ')

print()
print(is_empty_or_blanks('mars'))  # False
print(is_empty_or_blanks('  '))    # True
print(is_empty_or_blanks('')) 