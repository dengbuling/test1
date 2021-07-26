# for i in range(1,1001):
#     if (i // 100)**3 + ((i % 100)//10)**3 + (i % 10)**3 == i:
#         print(i)

# for i in range(100):
#     for m in range(100):
#         for n in range(100):
#             if 5*i+m*3+n/3 == 100 and i+m+n ==100:
#                 print(i,m,n)


#CRAPS赌博游戏
# import random
#
# isWin = True
# money = 1000
# times = 0
# while money>0:
#     ee = int(input("请下注："))
#     while isWin:
#         a1 = random.randint(1, 6)
#         a2 = random.randint(1, 6)
#         print("a1=%s,a2=%s" % (a1, a2))
#         if a1+a2 == 7 or a1+a2 == 11:
#             money+=ee
#             times +=1
#             print("赢钱啦，还有%s"%(money))
#             break
#         elif a1+a2 == 2 or a1+a2 == 3 or a1+a2 == 12:
#             money-=ee
#             print("输钱啦，还有%s"%(money))
#             break
#         else:
#             a3 = random.randint(1, 6)
#             a4 = random.randint(1, 6)
#             print("a3=%s,a4=%s" % (a3, a4))
#             if a3 + a4 == 7:
#                 money -= ee
#                 print("输钱啦，还有%s"%(money))
#                 break
#             elif a3+a4 == a1+a2:
#                 money += ee
#                 print("赢钱啦，还有%s"%(money))
#                 break


#求素数
# issushu = True
# for i in range(2,101):
#     for k in range(2,i):
#         if i % k == 0:
#             issushu = False
#             break
#
#         else:
#             issushu = True
#
#
#     if issushu == True:
#         print(i)

#求完美数

# for i in range(1,10001):
#     m = 0
#     for k in range(1,i):
#
#         if i % k == 0:
#             #print("%s的完美数是%s"%(i,k))
#             m+=k
#
#             #print(m)
#     if m==i:
#         print(m)


#求素数2

# for i in range(2,101):
#
#     for k in range(2,i):
#         #print(k)
#         if i % k == 0:
#             break
#     else:
#         print(i)

# aa = 0
# for i in range(2,101,2):
#     aa+=i
# print(aa)
# cc = 1
# bb = int(input("请输入非负整数："))
# for i in range(1,bb+1):
#     cc*=i
# print(cc)



# bb = int(input("请输入非负整数："))
#
# for i in range(2,bb):
#     if bb%i==0:
#         print("不是素数")
#         break
# else:
#     print("是素数")




# cc = int(input("请输入整数："))
# dd = int(input("请输入整数："))
# if cc>dd:
#     cc,dd = dd,cc
# for i in range(cc,0,-1):
#     #print(i)
#     if dd%i==0 and cc%i==0:
#         print(i)
#         print(cc*dd/i)
#         break

# ee = int(input("请输入行数："))
# for i in range(1,ee+1):
#     print("*"*i)
# for i in range(1,ee+1):
#     print(" "*(ee+1-i)+"*"*i)
# for i in range(1,ee+1):
#     print(("*"*(i*2-1)).center(ee*2-1))




#CRAPS赌博游戏
# import random
# money = 1000
# while money>=0:
#     ee = int(input("请下注:"))
#     times = 0
#     while True:
#         a1 = random.randint(1, 6)
#         a2 = random.randint(1, 6)
#         times += 1
#         print("第%s次掷骰子。骰子1点数是%s，骰子2点数是%s，一共%s点。" % (times, a1, a2, a1+a2))
#         if a1+a2 == 7 or a1+a2 == 11:
#             money += ee
#             times += 1
#             print("赢啦，赌注还有%s" % (money))
#             break
#         elif a1+a2 == 2 or a1+a2 == 3 or a1+a2 == 12:
#             money -= ee
#             print("输啦，赌注还有%s" % (money))
#             break
#         else:
#             while True:
#                 a3 = random.randint(1, 6)
#                 a4 = random.randint(1, 6)
#                 times += 1
#                 print("第%s次掷骰子。骰子1点数是%s，骰子2点数是%s，一共%s点。" % (times, a3, a4, a3+a4))
#                 if a3 + a4 == 7:
#                     money -= ee
#                     print("输钱啦，赌注还有%s" % (money))
#                     break
#                 elif a3+a4 == a1+a2:
#                     money += ee
#                     print("赢钱啦，赌注还有%s" % (money))
#                     break
#             break
# print("垃圾，再见")


# for i in range(1,100):
#     ll = 0
#     for m in range(1,i):
#         if i%m==0:
#             ll+=m
#     if ll==i:
#
#         print(ll)

#回文数
# nn = 0
# ll = 0
# mm = str(input("请输入整数："))
# l9 = len(str(mm))
# for i in range(len(str(mm))):
#     nn = nn+int(mm[i])*(10**(len(str(mm))-i-1))
#     ll = ll+int(mm[l9-1-i])*(10**(len(str(mm))-i-1))
# if nn == ll:
#     print("True")
# else:
#     print("False")


# def num1(n,m):
#     aaa = 0
#     bbb = 0
#     if n>m:
#         n,m = m,n
#     for i in range(n,1,-1):
#         if n % i == 0 and m % i == 0:
#             return i
#     #print("最大公约数是%s,最小公倍数是%s"%(aaa,n*m/aaa))
# print(num1(6,12))


# #判断回文数
# def is_num2(n):
#     num = 0
#     m = n
#     while n>1:
#         num = num * 10 + n % 10
#         n //= 10
#     #print(num)
#     #print(m)
#     # if num==m:
#     #     print("True")
#     # else:
#     #     print("False")
#     return num==m

# #判断素数
# def is_num3(n):
#     for i in range(2,n):
#         #print(i)
#         if n % i == 0:
#             #print(i)1
#             #print(n % i)
#             return False
#     else:
#         return True
#
# n = int(input("请输入数字："))
# print(is_num2(n))
# print(is_num3(n))
# if is_num2(n) and is_num3(n):
#     print(f"{n}是回文数")
# else:
#     print(f"{n}不是回文数")



# a, b = 5, 10
# print(f'{a} * {b} = {a * b}')

# list1 = [1, 3, 5, 7, 100]
# list1.append(200)
# list1.insert(1, 400)
# print(list1)
#
#
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# print(items2)
# items1 = dict(one=1, two=2, three=3, four=4)
# print(items1)
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# scores.update(冷面=67, 方启鹤=85)
#
# scores.popitem()
# print(scores)



# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         #os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:]+content[0]
#
# if __name__ == '__main__':
#     main()


# import random
# #密码生成器
# def password():
#     aa = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
#     bb = len(aa)
#     dd = ""
#     #cc = random.randint(0,bb-1)
#     for i in range(4):
#         cc = random.randint(0, bb - 1)
#         dd+=aa[cc]
#     print(dd)
# password()


# def msx_value(m):
#     for i in range(len(m)-1):
#
#
#         if m[i]>m[i+1]:
#             m[i], m[i + 1] =  m[i + 1] ,m[i]
#     m.sort(reverse=True)
#     return m[0],m[1]
#
# print(msx_value([5,3,4]))
#
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
# print(max2([5,3,4]))


#
# def which_day(year, month,date):
#     dd = 0
#     if year%4==0 and year % 100 != 0 or year % 400 == 0:
#         month_2  = 29
#     else:
#         month_2 = 28
#     for i in range(1,month-1):
#         if i in (1, 3, 5, 7, 8, 10, 12):
#             month_day = 31
#         # elif is_leap_year(year):
#         #     month_day = 28
#         # elif not is_leap_year(year):
#         #     month_day = 29
#         elif i in (4, 6, 9, 11):
#             month_day = 30
#         dd += month_day
#     return dd+month_2+date
#     #print(dd)
# print(which_day(2021, 12,11))



# #菲波那切数列
# def is_feibo():
#     ss = int(input("请输入数列个数："))
#     aa = [i for i in range(ss)]
#     #print(aa)
#     for i in range(2,ss):
#         aa[i] = aa[i-2]+aa[i-1]
#     return aa
# print(is_feibo())

#生成器
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     #return 'done'
# for i in fib(6):
#     print(i)


# rr = [[1], [1,1]]
# tt = []
# for i in range(2,6):
#     cow = [1] * (i+1)
#     for m in range(i//2):
#         old = rr[i-1][m]+rr[i-1][m+1]
#         cow[m+1] = old
#         cow[i-m-1] = old
#     rr.append(cow)
#print(rr)




# rr = [[1], [1,1]]
# tt = []
# for i in range(2,7):
#     cow = [1] * (i+1)
#     for m in range(i-1):
#         old = rr[i-1][m]+rr[i-1][m+1]
#         cow[m+1] = old
#         #print(m+1)
#         cow[i-m-1] = old
#         #print(i-m-1)
#     rr.append(cow)
# print(rr)

















#杨辉三角
uu = [[1],[1,1]]
for i in range(2,7):
    cow = [1]*(i+1)
    for m in range(i-1):
        #print(m)
        iii = uu[i-1][m]+uu[i-1][m+1]
        print(iii)
        cow[m+1] = iii
    uu.append(cow)

for i in uu:
    print(f'{i}')

    #print(f'cow:{cow}')










