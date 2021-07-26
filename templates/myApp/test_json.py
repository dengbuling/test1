# import json
# data_list = {'name': 'harry', 'age': 18}
#
# json_str = json.dumps(data_list)
# print(type(json_str))
# print(json_str)
#
# json_str1 = json.loads(json_str)
# print(json_str1)
# print(type(json_str1))

def mul(x=5,y=1,*args):
    return x * y
    print(args)
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))


def mul(*args,**kwargs):
    #return x * y
    # print(args)
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    sum = 1
    for i in args:
        sum = sum * i
    return sum

print('mul(5) =', mul(5,6,7,age = 5,name = "hhh",sex="boy"))

def fun1(n):
    if n==1:
        return 1
    return n * fun1(n-1)
print(fun1(100))

# def fun2(n,x,y,z):
#     if n==1:
#         print(x,'------',z)
#     else:
#         fun2(n-1, x, z, y)
#         fun2(n, x, y, z)
#         fun2(n-1, z, y, x)
# fun2(3, "x", "y", "z")

def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(2, "x", "y", "z")

def fun3(n):
    if len(n)==0:
        return n
    elif n[0]==" ":
        return n[1:]
    elif n[-1]==" ":
        return n[:-2]
print(fun3("jjj"))

def trim(s):
    '''首先判断该字符串是否为空，如果为空，就返回该字符串，
    如果不为空的话，就判断字符串首尾字符是否为空，
    如果为空，就使用递归再次调用该函数trim(),否则就返回该函数'''
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return (trim(s[1:]))    #从1:-1
    elif s[-1] == ' ':
        return (trim(s[:-1]))   #从-1:0
    return s
print(trim("    dasdas   "))




def findMinAndMax(L):
    if len(L)==0:
        return(None,None)
    max = L[0]
    min = L[0]
    for i in L:
        if max < i:
            max = i
    for m in L:
        if min > m:
            min = m
    return (min, max)

m = [x for x in range(10) if x % 2 ==0]
print(m)

aa = [x if x % 2 == 0 else -x for x in range(10)]
# print(aa)

# L = ['Hello', 'World', 18, 'Apple', None]
# bb = [x.lower() for x in L if isinstance(x, str)]
# print(bb)

L = ['Hello', 'World', 18, 'Apple', None]
bb = [x.lower() if isinstance(x, str) else x for x in L]
# print(bb)

def fun5(x):
    return x*x
qqq = list(map(fun5,[1,2,3,4,5]))
print(qqq)

from functools import reduce
def add(x, y):
     return x + y

print(reduce(add, [1, 3, 5, 7, 9]))


x = list(map(lambda x:x*x,[i for i in range(1,10)]))
#print((x))

pp = add
print(pp.__name__)


def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:",arc)
    return say
@funA
def funB(bbb):
    print("funB():", bbb)
funB("http://c.biancheng.net/python")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')





















