from django.shortcuts import render
from django.db.models import Max, Min, F, Q
from datetime import datetime

# Create your views here.
from .models import Students, Grades

from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a goog man")

#添加对象
def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudnet("陈冬",34,True,"我叫陈冬",grade,"2017-8-10", "2017-8-10")
    stu.save()
    return HttpResponse("alfjl")


def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    # stu = Students.createStudnet("刘德华",34,True,"流动的话",grade,"2017-8-10", "2017-8-10")
    stu = Students.createStudnet("张学友",34,True,"张学友的话",grade,"2017-8-10", "2017-8-10")
    return HttpResponse("%%%%%%%%%%%%%%")

from django.core.paginator import Paginator
def students(request, pageid):
    studentsList = Students.stuobj.all()

    paginator = Paginator(studentsList, 6)
    page = paginator.page(pageid)
    # # studentsList = Students.stuobj.get(pk=1)
    # print(studentsList)
    # return render(request, 'myApp/students.html', {"students": studentsList})
    # print(type(paginator))
    # studentsList = Students.stuobj.get(pk=1)
    # print(studentsList)
    # return render(request, 'myApp/stu1.html', {"students": studentsList, "num": 10, "str": "hhhhhhh"})
    return render(request, 'myApp/stu1.html', {"students": page, "num": 10, "str": "hhhhhhh"})



def studentSearch(request):
    # 模糊查询名字带孙
    # studentsList = Students.stuobj.filter(sname__contains="孙")
    #名字以孙开头
    # studentsList = Students.stuobj.filter(sname__startswith="孙")
    #id=2，4，6，8，10
    # studentsList = Students.stuobj.filter(pk__in=[2,4,6,8,10])
    #年龄大于30
    # studentsList = Students.stuobj.filter(sage__gt=30)

    #最后编辑时间
    # studentsList = Students.stuobj.filter(lastTime__year=2021)
    #
    # maxAge = Students.stuobj.aggregate(Max('sage'))
    # print(maxAge)

    studentsList = Students.stuobj.filter(Q(pk__lte=3) | Q(sage__gt=50))

    return render(request, 'myApp/students.html', {"students": studentsList})




def students2(request):
    #报异常
    # studentsList = Students.stuobj.get(sgender=True)
    studentsList = Students.stuobj.all()
    studentsList1 = Students.stuobj.all().values()
    # print(type(studentsList))
    # print(studentsList)
    #创建字典
    data = []
    for i in studentsList:
        dic = {}
        #print(i)
        dic['name'] = i.sname
        dic['age'] = i.sage
        data.append(dic)
    #print(data)

    # print(type(studentsList1))
    # print(type(list(studentsList1)))

    # return render(request, 'myApp/students.html', {"students": studentsList})
    #return HttpResponse(data)
    return JsonResponse(data, safe=False)


#显示前5条学生
def students3(request):
    studentsList = Students.stuobj.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})

#分页显示学生
def stupage(request, page):
    #0-5    6-10  10-15
    page = int(page)
    studentsList = Students.stuobj.all()[(page - 1)*5:page*5]
    return render(request, 'myApp/students.html', {"students": studentsList})


def grades(request):
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+10)
    print(g)
    return HttpResponse("dfffds ")

#打印
def attribute(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribute")


#获取GET传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+"   " + b + "    " + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + "    " + a2 + "    " + c)

def ShowRegister(request):
    return render(request, 'myApp/register.html')

def register(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    grade = Grades.objects.get(pk=1)
    lastTime = datetime.now()
    CreateTime = datetime.now()
    print(lastTime)
    print(CreateTime)
    # stu = Students.createStudnet("张学友",34,True,"张学友的话",grade,"2017-8-10", "2017-8-10")
    stu = Students.createStudnet(name, age, gender, hobby, grade, lastTime, CreateTime)
    # print(stu)
    stu.save()
    # return render(request, 'myApp/students.html', {"students": studentsList})

    return HttpResponse("studentsList")


def showresponse(request):
    res = HttpResponse()
    res.content = 'hdsfiidsf9ds9'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # print(res.content-type)
    return res

#编cookie
def cookietest(request):
    res = HttpResponse()
    # 新增cookie
    # cookie = res.set_cookie("sunck89","good99")
    cookie = request.COOKIES
    res.write("<h1>"+cookie["sunck"]+cookie["sunck89"]+"</h1>")
    red = HttpResponse()
    print(res.content)
    print(red.content)
    print(cookie)
    return res

#重定向
from django.http import HttpResponseRedirect
# def redirect1(request):
#     return HttpResponseRedirect('/redirect2')
# def redirect2(request):
#     return HttpResponse("重定向后的视图")

from django.shortcuts import redirect
#重定向简写
from django.http import HttpResponseRedirect
def redirect1(request):
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse("重定向后的视图")


#session
def main(request):
    #取session
    username = request.session.get("name", "游客登录哈哈哈哈哈哈")
    return render(request, 'myApp/main.html', {'username': username})

def login(request):
    return render(request, 'myApp/login.html')

def showmain(request):
    username = request.POST.get("username")
    #存储session
    request.session["name"] = username
    #设置过期时间单位是秒
    # request.session.set_expiry(10)
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):
    #清除session
    #方法一
    logout(request)
    #方法二
    # request.session.clear()
    return redirect('/main')

def good(request, page):
    return render(request, 'myApp/stu1.html', {"num1": page})
    # return redirect('/students')

def mainpage(request):
    return render(request, 'myApp/mainpage.html', {"code":"<h1>hhhhh</h1>"})
    # return redirect('/students')


import os
def upfile(request):
    dirs = "/Users/apple/Downloads/cv(17)"
    files = os.listdir(dirs)
    print(files)
    with open(file="/Users/apple/Downloads/文本(2021-05-25 141104)(1).txt", mode="r") as docfile:
        data = docfile.read()
        print(data)
    # print(os.sep)
    # print(os.name)
    print(os.path)
    # print(os.getenv('path'))
    # print(os.getcwd())
    return render(request, 'myApp/upfile.html')


from django.conf import settings
def savefile(request):
    if request.method == "POST":
        #文件描述符
        f = request.FILES["file"]
        #文件在服务器端的路径
        filepath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filepath, 'wb') as fb:
            #文件流分段，每次只能接受一部分
            for info in f.chunks():
                fb.write(info)
        return HttpResponse("上传成功")

    else:
        return HttpResponse("上传失败")

def edit(request):
     return render(request, 'myApp/edit.html')

def test1(request):
    return render(request, 'myApp/test1.html')
def test2(request):
    return render(request, 'myApp/test2.html')
def test6(request):
    return render(request, 'myApp/test6.html')
def title(request):
    return render(request, 'myApp/title.html')
def title1(request):
    return HttpResponse('1123')

from django.http import JsonResponse
def test_json_1(request):
    x = [{'name': 'peter', 'age': 18}, {'name': 'harry', 'age': 19}]
    #如果需要序列化费字典结构需要添加safe=False参数
    #JsonResponse会将响应头ct由html改为json
    return JsonResponse(x, safe=False)