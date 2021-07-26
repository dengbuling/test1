from functools import wraps
import time
def log_print(fun):
    start_run_time = time.ctime()
    start_time = time.time()

    @wraps(fun)
    def log_print_function_in(*args, **kw):

        print("函数执行时间为:{0},函数开始执行时间为:{1},函数名为:{2},函数运行结果为:{3}".format(run_time, start_run_time, fun.__name__, fun(*args, **kw)))
        fun(*args, **kw)

        print("函数执行时间为:%s,函数开始执行时间为:%s,函数名为:%s,函数运行结果为:%s"%(run_time, start_run_time, fun.__name__,fun(*args, **kw)))


    end_time = time.time()
    run_time = end_time - start_time

    return log_print_function_in
#log_print是一个装饰器，将funAA作为参数传递给log_print（fun）
@log_print
def funAA(x,y):
    print("我是函数funAA")
    time.sleep(1)
    return x ** y
funAA(2,9)













def required_ints(fun):
    @wraps(fun)
    def required_fun(*args,**kw):
        for i in (args + tuple(kw.values())):
            print(args + tuple(kw.values()))
            if not isinstance(i, int):
                print("参数必须为整形")
                #raise TypeError('参数必须为整形')
                #raise TypeError("参数必须为整形")
        #跳出循环
        else:
            return fun(*args, **kw)
    return required_fun
@required_ints
def required_func_B(*args,**kw):
    #print("恭喜你输入的是整形")
    return sum(args + tuple(kw.values()))
print(required_func_B(888,99.33,99,8.77))


# # 定义装饰器
# def required_ints(fun):
#     @wraps(fun)
#     def wrapper(*args, **kwargs):
#         # 遍历整个想要求和的元组
#         for i in args + tuple(kwargs.values()):
#             # 判断每个元素是否为整型,如果不是,则抛出异常
#             if not isinstance(i, int):
#                 # raise TypeError(): 抛出异常
#                 raise TypeError('参数必须为整形')
#         else:
#             # 调用函数,并返回函数返回值
#             res = fun(*args, **kwargs)
#             return res
#
#     return wrapper
#
#
# # 添加装饰
# @required_ints
# # 定义被装饰函数:
# # *args:可变参数  **kwargs:关键字参数
# def add(*args, **kwargs):
#     # args:字典类型   kwargs.values():元组类型
#     # 由于数据类型不同,所以不能直接用+来连接,必须先转换数据类型
#     return sum(args + tuple(kwargs.values()))


# 注意：如果有字典类型的实参，则必须写在最后边
#print(add(1, 2, a=3, b=5))


def AA():
    for i in range(10):
        if isinstance(i, int):
            print("参数必须为整形")
            #raise TypeError('参数必须为整形')
            # raise TypeError("参数必须为整形")
    else:
        print("hh")
#AA()