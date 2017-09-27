# !/usr/bin/env python3
# 8. Write a Python program to check a list is empty or not.

def isEmpty(li):
    if not li:
        return 'Empty'
    else:
        return 'Not empty'

print(isEmpty([1,2]))
