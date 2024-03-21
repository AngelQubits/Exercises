# Locale Part 2
def extract_region(locale):
	result = locale[3:5].split()
	print(result[0])

extract_region('en_US.UTF-8')      
extract_region('en_GB.UTF-8')      
extract_region('ko_KR.UTF-16')     

