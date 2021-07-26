
from myApp import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    #
    # url(r'^addstudent/$', views.addstudent),
    url(r'^students/$', views.students),
    url(r'^addstudent/$', views.addstudent),
    url(r'^addstudent2/$', views.addstudent2),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^students/(\d+)/$', views.students),

    url(r'^studentSearch/$', views.studentSearch),
    url(r'^grades/$', views.grades),
    url(r'^attribute/$', views.attribute),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^ShowRegister/register/$', views.register),
    url(r'^ShowRegister/$', views.ShowRegister),
    path(r'^ShowRegister/$', views.ShowRegister),
    url(r'^showresponse/$', views.showresponse),
    #编辑cookie
    url(r'^cookietest/$', views.cookietest),
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^login/showmain/$', views.showmain),
    url(r'^quit/$', views.quit),
    # url(r'^st1/$', views.stu1),
    url(r'^good/(\d+)/$', views.good, name="Appurl"),
    path('mainpage/', views.mainpage),
    path('upfile/', views.upfile),
    path('savefile/', views.savefile),
    path('edit/', views.edit),
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test6/', views.test6),
    path('title/', views.title),
    path('title1/', views.title1),
    path('test_json_1/', views.test_json_1),
]
