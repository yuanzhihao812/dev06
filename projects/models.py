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
"""


class Projects(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id主键", help_text="id主键")
    name = models.CharField(verbose_name="项目名称", help_text="项目名称", max_length=20, unique=True)
    leader = models.CharField(verbose_name="项目负责人", help_text="项目负责人", max_length=10)
    is_execute = models.BooleanField(verbose_name="是否开展", help_text="是否开展", default=False)
    desc = models.TextField(verbose_name="项目描述信息", help_text="项目描述信息", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        # 自定义表名
        db_table = "tb_projects"
        verbose_name = "项目表"
        verbose_name_plural = "项目表"

    def __str__(self):
        return self.name
