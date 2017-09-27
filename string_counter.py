#!usr/bin/env python3
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def counterString(val):
    result = 0

    for i in val:
        i = str(i)
        if len(i)>2:
            if i[0] == i[-1]:
                result += 1
    return result

print(counterString(['1kl','madam',1221,2211,9234]))
