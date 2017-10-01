#!usr/bin/env python3.5
# 24. Write a Python program to append a list to the second list.

flist = [x for x in range(1,5)]
slist = [x for x in range(5,9)]
print(flist,'\n',slist)
for i in slist:
    flist.append(i)
print('\n',flist)
# or
# appendList = flist + slist
