from django.http import HttpResponse
# Create your views here.
from django.views import View
from projects.models import Projects
from interfaces.models import Interfaces


# class ProjectViews(View):
#     """
#     定义类视图
#     1.必须继承View父类或者View子类
#     2.不同的请求方法，是以不同的请求方法一一对应，例如 GET——get POST--post  DELETE--delete
#     """
#
#     def get(self, request, pk):
#         return HttpResponse(f"GET请求：PK值为{pk}")
#         # return render(request, 'index.html')
#
#     def post(self, request, pk):
#         return HttpResponse(f"POST请求：PK值为{pk}")
#
#     def put(self, request, pk):
#         return HttpResponse(f"PUT请求：PK值为{pk}")
#
#     def delete(self, request, pk):
#         return HttpResponse(f"DELETE请求：PK值为{pk}")


class ProjectViews(View):
    def get(self, reuqest, pk):
        # # 方法1：调用手动调用save()方法进行保存
        # one_project = Projects(name="项目1", leader="张三")
        # one_project.save()
        # 方法2：objects.create()查看源码可知道自动掉了save()）
        one_project = Projects.objects.create(name="项目11223", leader="张三")
        # 添加子表数据
        # 方法1
        Interfaces(name="登录接口", tester="arae", projects_id=one_project.id)
        # 方法2
        # Interfaces(name="登录接口", tester="arae", projects=one_project)
        return HttpResponse('')

    def post(self, request, pk):
        pass
