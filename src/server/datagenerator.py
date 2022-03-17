#!/usr/bin/env python

# datagenerator.py: When executed, this file generates random values for 
# the example variables, which are stored in files under the data folder.
# The random values generate a hundred times per second.

import time
import random
import string

def get_string_random(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for n in range(length))

while True:
    with open('data/exampleA', 'w') as f:
        f.write(str(random.randrange(100)))

    with open('data/exampleB', 'w') as f:
        f.write(str(random.randrange(1000)/10))

    with open('data/exampleC', 'w') as f:
        f.write(get_string_random(8))

    time.sleep(1/100)
