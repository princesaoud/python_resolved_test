#!usr/bin/env python3
# 11. Write a Python function that takes
# two lists and returns True if they have at least one common member.

def commonElement(l,ll):
    for i in l:
        for j in ll:
            if i == j:
                return True
    return False

print(commonElement([12,34,56,78],[23,45,67,12]))
