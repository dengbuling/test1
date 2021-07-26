class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
        self.name = name
        self.gender = gender
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__gender
    def print_info(self):
        print("学生姓名是：%s，年龄是%s" % (self.__name,self.__gender))



class Student1(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def print_info1(self):
        print("学生姓名是??：%s，年龄是%s" % (self.name,self.gender))

class Plane(Student,Student1):
    def __init__(self,name,gender):
        super().__init__(name,gender)
        super().__init__(name,gender)
    def speak(self):
        print("学生喜好是：%s，年龄是%s" % (self.name,self.gender))
    def print_info(self):
        print("ppp")

stu2 = Plane('harry', 18)
stu2.speak()
stu2.print_info()
stu2.print_info1()
#print(Plane.__mro__)





class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

#print(C.__mro__)












