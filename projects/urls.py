"""
@author:yuanzhihao
@file:urls.py
@time:2021/07/03
"""
from django.urls import path
from projects import views

urlpatterns = [
    # path('projects/<int:pk>/', views.ProjectViews.as_view()),
    path('projects/<pk>/', views.ProjectViews.as_view()),

]
