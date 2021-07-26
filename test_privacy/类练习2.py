class Apple(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def get_information(self):
        return self.width
    @get_information.setter
    def set_information(self, width):
        if isinstance(width, int):
            self.width = width * 2
        else:
            print("请输入整数")


apple = Apple(30, 40)

print(apple.get_information)

apple.set_information = 90

print(apple.set_information)




class Screen(object):
    def __init__(self):
        self.width = 0
        self.height = 0
    @property
    def resolution(self):
        return self.width * self.height
    @resolution.setter
    def set_resolution(self,value):
        self.width = value
    @property
    def add_resolution(self):
        return self.width ** self.height


s = Screen()
s.width = 1024
s.height = 768

print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
s.set_resolution = 900
print('set_resolution =', s.set_resolution)
print('add_resolution =', s.add_resolution)



try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')


try:
    with open("/",'r') as f:
        print("peter")
except IsADirectoryError as m:
    print("错误是：",m)

import os
print(os.name)
print(os.path)
print(os.path.abspath('../static/myApp/css'))


import json

d = {'name':'tom','age':20,'interest':['music','movie']}
j = json.dumps(d)

print(j)