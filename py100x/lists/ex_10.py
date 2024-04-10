# Passcode
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

index = 0
string = ' '
while index < len(passcode):
	string += passcode[index] + '-'
	index +=1

print(string.removesuffix('-'))

# Analyze this further:
# print('-'.join(passcode))  # 11-jZ5-hQ3f*-8!7g3-p3Fs


