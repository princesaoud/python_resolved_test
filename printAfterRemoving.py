#!usr/bin/env python3.5
# 12. Write a Python program to print a specified list after removing
# the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def movingElement(arr):
    myArr = []
    for i in range(len(arr)):
        if i != 0 and i != 4 and i != 5:
            myArr.append(arr[i])
    return myArr

print(movingElement(['Red','Green','White','Black','Pink','Yellow']))

# another way to get the job done
# --------------
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
