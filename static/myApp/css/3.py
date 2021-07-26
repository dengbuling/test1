x = [1, "a", 0, "2", 0, "a", 1]
if x[::-1] == x:
    print("true")
else:
    print("false")
print(x)

aa = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
#print(sorted(aa))
aa.sort(reverse=True)

print(aa)



#3.2
a=[1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
#print(a[1:6:2])
#print(max(a),min(a))


ab = ["hello", "world", "yoyo", "congratulations"]
max = ""
for i in ab:
    #print(i,len(i))
    if len(i) > len(max):
        max = i
print(max)


L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
L1.sort(reverse=True)
print(L1[0:3])

#3.7列表按绝对值排序
aac = [1, -6, 2, -5, 9, 4, 20, -3]
aac.sort(key=abs)
print(aac)


#3.8按字符串长度排序
bbc = ["hello", "helloworld", "he", "hao", "good"]
bbc.sort(key=len)
print(bbc)


L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
l = set(L1)
ll = list(l)
ll.sort()
print(ll)

#3.10 去重保留顺序
aab=[3, 2, 1, 4, 2, 6, 1]
aba = []
for i in aab:
    if i not in aba:
        aba.append(i)
b4 = [i for i in aab if i not in aba]
#print("hahaahah%s"%(b4))


a1 = [1, 3, 5, 7]
b1 = ['a', 'b', 'c', 'd']
a1.extend(b1)
print(a1)


b2 = [i for i in range(1,11) if i %2==0 ]
print(b2)

a3 = [1,2,3,4,5]
b3 = [i**2 for i in a3]
print(b3)




# 3.14 找出列表大于0的数
# 使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
# 找出大于0的数，重新生成一个新的列表

a5 = [1, 3, -3, 4, -2, 8, -7, 6]
b5 = [i for i in a5 if i > 0]
print(b5)


a6 = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
b6 = [i for i in a5 if i > 0]
b66 = [i for i in a5 if i < 0]
# print(len(b6))
# print(len(b66))

# 3.16列表排除筛选
# a = ["张三","张四","张五","王二"] 如何删除姓张的
a7 = ["张三","张四","张五","王二"]
b8 = [i for i in a7 if i[0]!="张"]
print(b8)

for i in range(2,101):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        print(i)

p9 = filter(lambda x: x>0, [1, 3, 5, 7, 0, -1, -9, -4, -5, 8])
print(list(p9))


p8 = filter(lambda x: x[0]!="张", ["张三", "张四", "张五", "王二"])
print(list(p8))




a66 = [
{"name": "张三", "score": 66},
{"name": "李四", "score": 88},
{"name": "王五", "score": 90},
{"name": "陈六", "score": 56},
]

# print(a66[0]['name'])
p7 = filter(lambda x: x["score"]>60, a66)
print(list(p7))

def fun1(x):
    return x["score"]>60
p6 = filter(fun1, a66)
print(list(p6))

a144 = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
a88= [456, 700, 200]


