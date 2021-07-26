x="abc"
y="def"
z=["d","e","f"]

print(x.join(y))
print(x.join(z))


list1=['ak','uk',"4"]
list2=[str(i) for i in list1] #使用列表推导式把列表中的单个元素全部转化为str类型

list3=' '.join(list1)
print(list3)


import re
reg = r"\d+"
m = re.search(reg,"abc123d")
print(m)


#a2 = input("请输入网址——————")
# while True:
#     a2 = input("请输入网址——————")
#     if re.search(r".com$",a2):
#         re.findall(r".com$",a2)
#         print(a2)
#         print(re.findall(r".com$",a2))
#         continue
#     elif a2 == "q":
#         break
#     else:
#         print("incorrect email format。注意必须以.com 结尾")


a3 = "aababbc"
a4 = ""
for i in a3:
    if i == "a" and (i+1) == "b":
        print(i)
for i in range(len(a3)-1):
    if a3[i] != "a" and a3[i+1] != "b":
        a4 += str(a3[i])
#print(a4)

