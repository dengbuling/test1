a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
print(a.index(max(a)))

max1 = 0
maxname = ""
a2 = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
for i in a2:
    if a2.count(i) > max1:
        max1 = a2.count(i)
        maxname = i
print(maxname)

a4 = []
a5 = [
'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
'need', 'skills', 'more', 'my', 'ability', 'are',
'so', 'poor'
]
# for i in a5:
#     if i not in a4:
#         a4.append(i)
# for i in a4:
#     print("%s出现次数是%s"%(i,a5.count(i)))

a7 = [["A", 1], ["B", 2]]
print(a7[1][1])

import random
L = [1, 2, 3, 5, 6]
random.shuffle(L)
print(L)

