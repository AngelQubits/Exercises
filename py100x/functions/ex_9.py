# Locale Part 1
def extract_language(locale):
	result = locale[0:2].split()
	print(result[0])

extract_language('en_US.UTF-8')      
extract_language('en_GB.UTF-8')      
extract_language('ko_KR.UTF-16')     
