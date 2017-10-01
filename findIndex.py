#!usr/bin/env python3.5
# 22. Write a Python program to find the index of an item in a specified list.

myList = [x for x in range(1,11)]

def findIndex(a,myList2):
    for index,i in enumerate(myList2):
        if i == a:
            return index
print(findIndex(2,myList))

# or
# myList.index(3) return index (int)
