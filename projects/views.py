from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class ProjectViews(View):
    """
    定义类视图
    1.必须继承View父类或者View子类
    2.不同的请求方法，是以不同的请求方法一一对应，例如 GET——get POST--post  DELETE--delete
    """

    def get(self, request, pk):
        return HttpResponse(f"GET请求：PK值为{pk}")
        # return render(request, 'index.html')

    def post(self, request, pk):
        return HttpResponse(f"POST请求：PK值为{pk}")

    def put(self, request, pk):
        return HttpResponse(f"PUT请求：PK值为{pk}")

    def delete(self, request, pk):
        return HttpResponse(f"DELETE请求：PK值为{pk}")
