
from django.urls import path, include
from . import views

app_name = "app02"

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('taskForm/', views.taskForm, name='task'),
    path('answer/', views.taskAnswer, name='answer'),
    path('alldata/', views.alldata, name='alldata'),
    path('notalldata/', views.notAllData, name='notalldata'),

]
