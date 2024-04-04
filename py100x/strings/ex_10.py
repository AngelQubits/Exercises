# define function count_substirngs takes a string and arg
# return count of how many times arg appears

def count_substrings(full, part):
	return full.count(part)
	
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0