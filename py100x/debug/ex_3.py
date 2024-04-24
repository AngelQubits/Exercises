# Multiply By Five
# Solution: n was a string, as a result python understood repeat n 5 times
# instead of mathematical function. Converting input to integer solves this.

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")