#!usr/bin/env python3
# 1. Write a Python program to sum all the items in a list.

myList = [1,2,3,4]
result = 0
for i in range(0,len(myList)):
    result += myList[i]

print(result)
