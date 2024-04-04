# define function takes two str as args (1 full, 1 part)
# if arg2 is in begining of arg1 return True Else False

def starts_with(arg1, arg2):
	return arg1.startswith(arg2)
		
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True