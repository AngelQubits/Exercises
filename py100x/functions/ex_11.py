# Internalization 2 - Cloud 9
def extract_language(locale):
	language = locale[0:2].split()
	return (language[0])
	
def extract_region(locale):
	result = locale[3:5].split()
	return (result[0])


def local_greet(locale):
	if extract_language(locale) == 'en' and extract_region(locale) == 'US':
		print('Hi!')
	elif extract_language(locale) == 'en'and extract_region(locale) == 'GB':
		print('Hello!')
	elif extract_language(locale) == 'en'and extract_region(locale) == 'AU':
		print('Howdy!')
	elif extract_language(locale) == 'fr':
		print('Salut!')
	elif extract_language(locale) == 'es'and extract_region(locale) == 'AR':
		print('Hola!')
	elif extract_language(locale) == 'es'and extract_region(locale) == 'DO':
		print('Saludos!')
	elif extract_language(locale) == 'es'and extract_region(locale) == 'ES':
		print('Que Tal!')
	elif extract_language(locale) == 'de':
		print('Hallo!')
	elif extract_language(locale) == 'sv':
		print('Hej!')
	elif extract_language(locale) == 'af':
		print('Haai!')
	else:
		print("I do not recognize this language yet!!!")
	
local_greet('en_US.UTF-8')
local_greet('en_GB.UTF-8')
local_greet('en_AU.UTF-8')
local_greet('fr_FR.UTF-8')
local_greet('es_ES.UTF-8')
local_greet('es_DO.UTF-8')
local_greet('es_PE.UTF-8')