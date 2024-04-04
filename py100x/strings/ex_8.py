def capital(text):
	new_text = text.split(' ')
	answer = ''
	for x in new_text:
	    answer += (x.capitalize() + ' ')
	print(answer)

capital('launch school tech & talk')