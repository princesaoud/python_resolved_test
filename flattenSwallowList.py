#!usr/bin/env python3.5
# 23. Write a Python program to flatten a shallow list.

myList = [[1,2,3],[4,5,6]]
flattenList = []
for i in myList:
    for j in i:
        flattenList.append(j)
print(flattenList)

# or
# import itertools
# flattenList = list(itertools.chain(*myList))
# print(flattenList)
