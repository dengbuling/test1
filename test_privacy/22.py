for i in range(100,1000):
    m = (i//100) ** 3
    n = ((i % 100)//10) ** 3
    q = (i % 10) ** 3

    if m+n+q == i:
        print(i)


# print((153//100) ** 3)
# print(((153 % 100)//10) ** 3)
# print((153 % 10) ** 3)
# print((153//100) ** 3+((153 % 100)//10) ** 3+(153 % 10) ** 3)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

sum1 = 0
for i in range(1,101):
    if i%2 == 0:
        sum1 -= i
    else:
        sum1 += i
print(sum1)

sum2 = 0
for i in range(1,101):
    if i%2 == 0:
        sum2 += i
    else:
        sum2 -= i
print(sum2)


sum3 = 0
for i in range(1,101):
    if i%5 == 0:
        sum3 += i
print(sum3)


#2.7
sum4 = 0
for i in range(1,6):
    sum4 = sum4 + (i**3)
print(sum4)

#2.8
sum5 = 1
for i in range(1,11):
    sum5 = sum5 * i
print(sum5)

#2.9
sum6 = 0
sum7 = 1
for i in range(1,11):
    sum7 = sum7 * i
    sum6 = sum6 + sum7
print(sum6)


#2.11
sum8 = 0
sum9 = 1
while sum8<10:



    #print(sum8,end=",")
    sum8 = sum8+sum9
    #print(i, end="")


a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b