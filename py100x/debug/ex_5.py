# Confucious Says
# problem is conditional statement was returning none, a falsy value.
# adding the 'return' statement allows pythong to recognize the string and 
# concotanate accordingly.

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
#print(get_quote('Confucius'))
print('"' + get_quote('Confucius') + '"')