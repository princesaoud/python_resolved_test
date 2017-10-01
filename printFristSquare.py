# !usr/bin/env python3.5
# 16. Write a Python program to generate and print a list of first and
# last 5 elements where the values are square of numbers between 1 and 30
# (both included). Go to the editor

result = []
for i in range(1,30):
    result.append(i**2)

print(result[:5])
print(result[-5:])
