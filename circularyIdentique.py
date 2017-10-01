#!usr/bin/env python3.5
# 26. Write a python program to check whether two lists are circularly identical

flist = [10,10,20,0,0,0]
slist = [10,20,0,0,0,0]
tlist = [30,10,20]
def isDuplicates(items):
    dup_items = set()
    for i in items:
        for j in items:
            if i != j:
                dup_items.add(i)
    return dup_items

flist = isDuplicates(flist)
slist = isDuplicates(slist)
tlist = isDuplicates(tlist)

def circularlyIdentical(a,b):
    if a == b:
        return True
    else:
        return False
print(circularlyIdentical(flist,slist))
print(circularlyIdentical(slist,tlist))
