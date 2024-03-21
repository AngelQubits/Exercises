# Diplsay Division
# '3/1 = 3 thru 30/10 =3'
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three()

#solution:  Parenthesis is required to invoke a function