# Three-way Comparison
def compare_by_length(string1, string2):
	s1 = len(string1)
	s2 = len(string2)
	if s1 < s2:
		print(-1)
		return -1
	elif s1 > s2:
		print(1)
		return 1
	else:
		print(0)
		return 0

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0
