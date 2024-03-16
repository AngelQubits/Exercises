# TypeError usually indicates that the wrong data type is being refernced.
# In this case, the error is tryint to add an int and str
# You'd have to use parenthesis, to separate the len function from the int.
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = (len(tweet) + 5)
print(length_of_tweet)

# raises error:
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)