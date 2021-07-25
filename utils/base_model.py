# @Time : 2021/7/25 20:29
# @Author : yuanzhihao
# @File : base_model.py
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id主键", help_text="id主键")
    create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        # abstract定义当前模型类为抽奖模型类，
        # 一般模型类均有公共基类id,create_time,update_time，因此将该公共字段抽取出来成为基类
        # 但是该字段在迁移脚本时不应该迁移，因此需要加abstract = True
        abstract = True
