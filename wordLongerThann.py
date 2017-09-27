#!usr/bin/env python3
# 10. Write a Python program to find the list of ...
# words that are longer than n from a given list of words.


def longerWord(n,words):
    words = words.split(' ')
    res = []
    for i in words:
        if len(i)>n:
            res.append(i)
    return res

words = 'The chicken will kill for your pleasure Sir'
n=4
print(longerWord(n,words))
