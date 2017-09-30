# !usr/bin/env python3.5
# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle

numbers = [x for x in range(1,10)]
print('Before shuffle',numbers)
shuffle(numbers)
print('After shuffle',numbers)
