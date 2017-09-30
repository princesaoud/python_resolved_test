# !usr/bin/env python3.5
# 14. Write a Python program to print the numbers of
# a specified list after removing even numbers from it.

numbers = [1,2,3,4,5,6,7,8,9,10]
odd = [x for x in numbers if x%2  !=0]
print(odd)
