# !usr/bin/env python3.5
# 19. Write a Python program to get the difference between the two lists.

flist = [x for x in range(1,5)]
slist = [x for x in range(3,7)]
# dif = [x for x in flist if x not in list(slist)]
# print('the difference are :',dif)
# or
print(set(flist) - set(slist))
