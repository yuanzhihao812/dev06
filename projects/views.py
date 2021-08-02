# from django.http import HttpResponse
# # Create your views here.
# from django.views import View
# from projects.models import Projects
# from interfaces.models import Interfaces


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


# class ProjectViews(View):
#     def get(self, reuqest, pk):
#         # # 方法1：调用手动调用save()方法进行保存
#         # one_project = Projects(name="项目1", leader="张三")
#         # one_project.save()
#         # 方法2：objects.create()查看源码可知道自动掉了save()）
#         one_project = Projects.objects.create(name="项目11223", leader="张三")
#         # 添加子表数据
#         # 方法1
#         Interfaces(name="登录接口", tester="arae", projects_id=one_project.id)
#         # 方法2
#         # Interfaces(name="登录接口", tester="arae", projects=one_project)
#         return HttpResponse('')
#
#     def post(self, request, pk):
#         pass

from projects.models import Projects
from django.views import View
from django.http import JsonResponse, HttpRequest
import json


class ProjectViews(View):

    def get(self, request):
        """
        GET projects 获取项目列表数据，（json形式数据返回）
        1.从数据库中获取所有的项目数据，（查询集对象）
        2.查询集转化为json数据
        3.将json数据返回到前端
        :param request:
        :return:
        """
        qs = Projects.objects.all()
        projects_list = []
        obj: Projects
        for obj in qs:
            project_dict = {
                "id": obj.id,
                "name": obj.name,
                "leader": obj.leader,
                "is_execute": obj.is_execute,
                "desc": obj.desc,
                "create_time": obj.create_time,
                "update_time": obj.update_time,
            }
            projects_list.append(project_dict)
        return JsonResponse(data=projects_list, safe=False, json_dumps_params={"ensure_ascii": "False"})

    def post(self, request: HttpRequest):
        """
        POST /projects 创建一条数据，（以json形式传递数据，同时需要将创建成功之后的数据以json形式返回）
        1.获取json参数并转化为Python中的数据类型（字典或是嵌套字典的列表）
        2.需要对入参进行校验，
        3.创建项目数据
        4.创建成功的数据转换为json数据
        5.json数据返回
        :param request:
        :return:
        """
        err_msg = {
            "status": False,
            'msg': "参数有误"
        }
        # 1.获取json参数并转化为Python中的数据类型（字典或是嵌套字典的列表）
        try:
            json_str = request.body.decode('utf-8')
            python_data = json.loads(json_str)
        except Exception:
            err_msg = {
                "status": False,
                'msg': "参数有误"
            }
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        # 2.需要对入参进行校验
        if 'name' not in python_data or len(python_data.get('name')) > 20:
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        # 3.创建项目数据
        obj = Projects(name=python_data.get("name"), leader=python_data.get("leader"), desc=python_data.get("desc"))
        # obj = Projects(**python_data)
        obj.save()
        # 4.创建成功的数据转换为json数据
        project_dict = {
            "id": obj.id,
            "name": obj.name,
            "leader": obj.leader,
            "is_execute": obj.is_execute,
            "desc": obj.desc,
            "create_time": obj.create_time,
            "update_time": obj.update_time,
        }
        return JsonResponse(project_dict, json_dumps_params={"ensure_ascii": False}, status=200)


class ProjectDetailViews(View):
    def get(self, request, pk):
        """
        GET /projects/<int:pk>/获取一条项目详情数据(json对象形式返回)
        1.从数据库中获取一条项目数据
        2.数据校验
        3.将获取的模型类数据转化为json数据
        4.将json数据返回
        :param request:
        :param pk:
        :return:
        """
        try:
            obj = Projects.objects.get(id=pk)
        except Exception:
            err_msg = {
                "status": False,
                'msg': "参数有误"
            }
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        project_dict = {
            "id": obj.id,
            "name": obj.name,
            "leader": obj.leader,
            "is_execute": obj.is_execute,
            "desc": obj.desc,
            "create_time": obj.create_time,
            "update_time": obj.update_time,
        }
        return JsonResponse(project_dict, json_dumps_params={"ensure_ascii": False}, status=200)

    def delete(self, request, pk):
        """
        DELETE /projects/<int:pk>/删除一条项目详情数据(返回删除成功的json数据)
        1.获取待删除的模型类对象
        2.需要校验PK是否存在
        3.删除模型类对象
        4.将删除程光的信息返回
        :param request:
        :param pk:
        :return:
        """
        try:
            obj = Projects.objects.get(id=pk)
        except Exception:
            err_msg = {
                "status": False,
                'msg': "参数有误"
            }
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        obj.delete()
        success_msg = {
            "status": True,
            'msg': "删除成功"
        }
        return JsonResponse(success_msg, json_dumps_params={"ensure_ascii": False}, status=200)

    def put(self, request, pk):
        """
        PUT /projects/<int:pk>/更新一条项目数据(以json形式传递参数，同时需要将更新成功的之后的数据以json形式返回)
        1.获取json参数并转化为python中的数据类型，
        2.需要大量的数据校验
        3.获取待更新的模型类对象
        4.需要校验pk是否存在
        5.数据更新
        6.返回数据
        :param request:
        :param pk:
        :return:
        """
        err_msg = {
            "status": False,
            'msg': "参数有误"
        }
        try:
            json_str = request.body.decode('utf-8')
            python_data = json.loads(json_str)
        except Exception:
            err_msg = {
                "status": False,
                'msg': "参数有误"
            }
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)

        if 'name' not in python_data or len(python_data.get('name')) > 20:
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        try:
            obj = Projects.objects.get(id=pk)
        except Exception:
            err_msg = {
                "status": False,
                'msg': "参数有误"
            }
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        obj.id = python_data.get("id") or obj.id
        project_dict = {
            "id": obj.id,
            "name": obj.name,
            "leader": obj.leader,
            "is_execute": obj.is_execute,
            "desc": obj.desc,
            "create_time": obj.create_time,
            "update_time": obj.update_time,
        }
        return JsonResponse(project_dict, json_dumps_params={"ensure_ascii": False}, status=200)
