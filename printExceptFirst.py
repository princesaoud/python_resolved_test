# !usr/bin/env python3.5
# 17. Write a Python program to generate and print a list except
# for the first 5 elements, where the values are square
# of numbers between 1 and 30 (both included).

result = []

for i in range(1,31):
    result.append(i**2)

print(result[5:])
