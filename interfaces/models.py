from django.db import models

# Create your models here.

"""
1.定义模型类必须继承Model或者Model子类，一个模型类相当于一个table
2.定义的类属性(Field对象)为表的字段信息
3.默认表名是子应用名_模型类名小写
4.默认自动创建一个ID主键（自增，非空）
5.生成迁移脚本：python manage.py makemigrations 子应用名
  执行迁移脚本：python manage.py migrate 子应用名
6.CharField指定varchar类型，必须设置max_length参数，指定最大长度
  unique=True设置唯一约束，默认unique=False
  default:默认值
  null:数据保存时指定是否允许为空，默认null=False
  blank:前端传参时是否允许为空，默认blank=False
  primary_key:主键，orm会自动创建id为主键，但如果某个字段定义了primary_key=True则orm不会在自动创建ID主键
  auto_now_add：=True时创建一条数据时会自动化将当前时间赋值给该字段，只修改一次
  auto_now:=True时每次更新数据时会自动将当前时间赋值该字段
7.可以在Meta子类中修改当前表的元数据信息，

8.Projects表和interfaces表的关系,一对多的关系，往往是在多的表中添加外键字段
9.ForeignKey：外键字段，
  参数to="子应用名.模型类名"，
  参数on_delete=models.CASCADE：父表数据删除时对应的从表数据被自动删除
  参数on_delete=models.SET_NULL：父表数据删除时对应的从表数据中的外键字段被自动设置null
  参数on_delete=models.SET_DEFAULT：父表数据删除时对应的从表数据中的外键字段被自动设置default的值
  参数on_delete=models.PROTECT：父表数据删除时,如果存在对应的从表数据那么会抛出异常
  
  
"""


class Interfaces(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id主键", help_text="id主键")
    name = models.CharField(verbose_name="接口名称", help_text="接口名称", max_length=15, unique=True)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=10)
    # 外键字段
    projects = models.ForeignKey(to='projects.Projects', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        # 自定义表名
        db_table = "tb_interfaces"
        verbose_name = "接口表"
        verbose_name_plural = "接口表"

    # 魔术方法默认return出的数据，当前方法指的是返回接口的name
    def __str__(self):
        return self.name
