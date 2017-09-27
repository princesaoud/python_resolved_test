#!usr/bin/env python3
# 3. Write a Python program to get the largest number from a list.

def largest(items):
    bigest_num = items[0]

    for i in items:
        if i > bigest_num:
            bigest_num = i

    return bigest_num

print(largest([22,11,44,33]))

# Be careful with the space *X
