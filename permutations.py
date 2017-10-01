# !usr/bin/env python3.5
# Write a Python program to generate all permutations of a list in Python.

import itertools
container = [x for x in range(1,4)]
print(list(itertools.permutations(container)))
