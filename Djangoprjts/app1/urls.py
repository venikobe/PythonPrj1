
from django.urls import path, include
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('about/', views.about, name='about'),
    path('task/', views.task, name='task'),
    path('answer/', views.taskAnswer, name='answer'),
    path('article/aigis', views.AigisArticle, name='aigis'),
    path('article/makoto', views.MakotoArticle, name='makoto'),
    path('article/kotone', views.KotoneArticle, name='kotone'),
    path('article/fuuka', views.FuukaArticle, name='fuuka'),
]
