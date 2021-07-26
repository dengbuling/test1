from time import sleep


# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()




class Person1(object):
    限定对象只能绑定("name","age","gender")
    __slots__ = ("name","age","gender")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name_info(self):
        return self.name

    @property
    def age_info(self):
        return self.age

    @name_info.setter
    def name_info(self,name):
        self.name = name

    def play(self):
        if self.age<16:
            print(f"{self.name}正在打篮球")
        else:
            print(f"{self.name}正在上网")
aaa = Person1("王浩",17)

aaa.name_info="陈冬"


aaa.gender="女"
aaa.gender="nan"
#aaa.conrent="nan"
print(aaa.gender)
print(aaa)