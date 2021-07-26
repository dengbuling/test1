a = "abcba"
if a == a[::-1]:
    print("true")
else:
    print("false")

b = "hello_world_yoyo"
print(b.split("_"))


print("_".join(b.split("_")))

s = "We are happy."
print(s.replace(" ","%20"))

#99乘法表
# for i in range(1,10):
#     for m in range(1,i+1):
#         print("%s * %s\t" % (i,m), end="")
#     print()

x = "Hello, welcome to my world."
print(x.find("welcome"))
print(x.count("w"),x.count("my"))

a="welcome to my world"
try:
    if a.index("world9"):
        print("true")
except ValueError:
    print("false")

l = "hi how are you hello world, hello yoyo !"
print(l.find("hello"),l.rfind("hello"))

q = "1236i6"
if q.isnumeric():
    print("true")
else:
    print("false")

aa = " welcome to my world ！    "
print(aa.strip(" "),aa.replace(" ",""))


for i in range(1,5):
    print(("*"*(i*2-1)).center(10))
for m in range(1,4):
    print(("*"*((4-m)*2-1)).center(10))


aaa = 12345               
print("这是%s位数"%(len(str(aaa))))
print(str(aaa)[::-1])
