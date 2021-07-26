from django.db import models

# Create your models here.


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    #django将空值以null存储在数据库中
    # gdata = models.DateTimeField(null=True)
    gdata = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    # 定义最后编辑时间
    # lastTime = models.DateField(auto_now=True)

    #默认标签
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"

#定义查询集
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)
    def createStudnet(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        print(type(grade))
        stu.sname = name
        stu.sage =age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.CreateTime = createT
        return stu






class Students(models.Model):
    #自定义模型管理器
    #当自定义模型管理器，django就不再为模型类生成objects模型类管理器
    stuobj = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    #设置字段名称
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    #关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.sname

    def GetStudent(self):
        return self.sname

    # 定义最后编辑时间
    lastTime = models.DateTimeField(auto_now=True)
    # 定义创建时间,最后编辑时间和创建时间不能同时
    CreateTime = models.DateTimeField(auto_now_add=True)



    class Meta:
        #定义数据表名，推荐使用小写
        db_table = "students"
        #ordeing = ['id']

    # #定义一个类方法创建对象
    #在模型类中添加方法
    @classmethod
    def createStudnet(cls, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender,
                   scontend=contend, sgrade=grade, lastTime=lastT,
                  CreateTime=createT, isDelete=isD)
        # print(stu)
        return stu





