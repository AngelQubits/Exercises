# Internalization 1
def greet(x):
	if x == 'en':
		print('Hi!')
	elif x == 'fr':
		print('Salut!')
	elif x == 'pt':
		print('Olá!')
	elif x == 'de':
		print('Hallo!')
	elif x == 'sv':
		print('Hej!')
	elif x == 'af':
		print('Haai!')
	else:
		print("I do not recognize this language yet!!!")

greet('en')
greet('fr')
greet('pt')
greet('de')
greet('sv')
greet('af')
greet('ho')

#match case not availabe cloud9