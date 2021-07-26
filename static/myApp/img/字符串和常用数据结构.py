# #杨辉三角
# dd = int(input("请输入行数："))
# def yanghui(dd):
#     uu = []
#     for i in range(dd):
#         cow = [1]*(i+1)
#         for m in range(i-1):
#             #print(m)
#             iii = uu[i-1][m]+uu[i-1][m+1]
#             #print(iii)
#             cow[m+1] = iii
#         uu.append(cow)
#
#     return uu
#
# # for i in uu:
# #     print(f'{i}')
# print(yanghui(dd))



#生成器杨辉三角型
# def gender(n):
#     ll = [1]
#     index = 0
#     while index<n:
#         yield ll
#
#         ll = [ll[i]+ll[i+1] for i in range(len(ll)-1)]
#         ll.append(1)
#         ll.insert(0,1)
#         index+=1
#
# a = gender(10)
# for i in a:
#     print(i)


# #生成器菲波那切数列
# def pp(n):
#     ll = [i for i in range(n)]
#     for i in range(2,n):
#         ll[i] = ll[i-1]+ll[i-2]
#     yield ll
# for i in pp(15):
#     print(i)



# #双色球选号
# import random
# def fff():
#     for i in range(1,7):
#         aa = random.randrange(1, 34)
#         bb = random.randrange(1, 16)
#         print("%02d"%aa,end=" ")
#     print("|",end=" ")
#     print("%02d"%bb)
# for i in range(6):
#     fff()

from random import randrange, randint, sample



ff = [i for i in range(1,31)]
kk,ll,n=0,[],0
while n<15:
    for i in ff:
        kk+=1
        if kk%9==0:
            ff.pop(0)
            n+=1
        else:
            ff.append(ff[0])
            ff.pop(0)
kkk = ["非"]*30
for i in ff:
    kkk[i-1]="基"
kkkk ="".join(kkk)
print(kkkk)


def mobi():
    aa = [True]*30
    #print(aa[0])
    n = 0
    count=0
    number=0
    while count<15:
        if aa[number]==True:
            n+=1
            if n==9:
                aa[number]=False
                n=0
                count+=1
        number+=1
        number %= 30
    #print(aa)
    for pp in aa:
        print('基' if pp else '非', end='')
mobi()










