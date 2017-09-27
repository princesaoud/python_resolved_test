#!usr/bin/env python3
# 4. Write a Python program to get the smallest number from a list
def min_number(items):
    min = items[0]
    for i in items:
        if i < min:
            min = i
    return min

print(min_number([22,44,11,66]))
