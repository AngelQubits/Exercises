# Line 7: options are strings not recognized as bool by conditionals.
# Line 14: invoke the function so you can actually see if its working.

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
        
predict_weather()