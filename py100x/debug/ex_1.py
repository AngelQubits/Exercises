def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

#1:  TypeError, too many arguments given for function, it only takes 1 argument
#2:  TypeError, the integer 1 is not an iterable object