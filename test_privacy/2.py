# a = float(input("请输入华氏温度："))
# print("摄氏度为%.2f"%((a-32)/1.8))


# b = int(input("请输入圆的半径："))
# print("圆的面积为%s，周长为%s"%(3.14*(b**2),2*3.14*b))


# c = int(input("请输入年份："))
# if c%4 == 0:
#     print("年份%s，是闰年" % (c))
# else:
#     print("年份%s，不是闰年" % (c))

# d = int(input("请边长："))
# e = int(input("请边长："))
# f = int(input("请边长："))
# if d+e>f and d+f>e and e+f>d:
#     print("三角形周长为%s"%(d+e+f))
# else:
#     print("您输入的不是三角形")

# import random
# g = random.randint(1,100)
# i = 0
# while True:
#     h = int(input("请输入数字："))
#     if h>g:
#         print("大了大了")
#     elif h<g:
#         print("小了小了")
#     else:
#         print("恭喜你")
#         break
#     i += 1
# print("一共猜了%s次"%(i))

##99乘法表
# for i in range(1,10):
#     for m in range(1,i+1):
#         print("%s*%s=%s"%(i,m,i*m),end=" ")
#     print("\n")


# 判断数字为素数
# while True:
#     l = int(input("请输入数字："))
#     issushu = False
#     for i in range(2,l):
#         if l % i==0:
#             print("不是素数")
#             issushu = False
#             break
#         else:
#             issushu = True
#     if issushu == True:
#         print("是素数")



# for k in range(2,101):
#     issushu = False
#     for i in range(2,k):
#         if k % i==0:
#             #print("不是素数")
#             issushu = False
#             break
#         else:
#             issushu = True
#             #print(issushu)
#     if issushu == True:
#          print(k)


#最大公约数和最下公倍数

# m = int(input("请输入数字："))
# n = int(input("请输入数字："))
# o = 0
# p = 1
# for i in range(1,m):
#     for l in range(1, n):
#         if m%l ==0 and m%i==0:
#             if n % l == 0 and n % i == 0:
#                 if l==i:
#                     #print(l,i)
#                     o = i
# p = o*(m/o)*(n/o)
#
#
# print(o)
# print(p)




# r = int(input("请输入数字："))
# s = int(input("请输入数字："))
# if r>s:
#     r,s = s,r
# for i in range(r,0,-1):
#     if r%i==0 and s%i==0:
#         print("最大公约数%s"%(i))
#         print("最小公倍数%s"%(s*r/i))
#         break


# t = int(input("请输入行数："))
# for i in range(1,t+1):
#     print("*"*i)
# for i in range(1,t+1):
#     print(" "*(t+1-i)+"*"*i)
# for i in range(1,t+1):
#     a = "*" * (i * 2 - 1)
#
#     print(a.center(t*2-1))


#提交不为空

#fjdisfjidshfdshfdshfidshfihdsifhds
8903790349032849032849032740932
#89327498374983740937409324
4739288888c4n7v24327v49v9n79n2v9c92
v432yn432y9v8n4293v948ncn234983v2
4vy3829n48932c8947n8239n74c98n729c8n42
cn49832nc984y8c5y9c5897c985nc52c5
