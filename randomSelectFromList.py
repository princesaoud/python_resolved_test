#!usr/bin/env python3.5
import random
flist = [x for x in range(1,11,2)]
result = random.sample(flist,1)

print(flist,'\n',result)
# or
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))
