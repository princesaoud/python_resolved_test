#!usr/bin/env python3
# 2. Write a Python program to multiplies all the items in a list.

def multiList(item):
    result = 1

    for i in item:
        result *= i

    return result

print(multiList([2,4,6]))
