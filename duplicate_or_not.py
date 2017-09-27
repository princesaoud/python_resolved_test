#!/usr/bin/env python3
# 7. Write a Python program to remove duplicates from a list.

def isDuplicates(items):
    dup_items = set()
    for i in items:
        for j in items:
            if i != j:
                dup_items.add(i)
    return dup_items
print(isDuplicates([10,20,30,20,10,50,60,40,80,50,40]))
