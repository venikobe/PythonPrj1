
from django.urls import path, include
from . import views

app_name = "wiki"

urlpatterns = [
    path('', views.mainPage, name='main'),
     path('page/<int:pk>', views.page, name='page'),


]
