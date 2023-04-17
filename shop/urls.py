from django.urls import path
# . означает, что импортируем из текущей папки
from . import views

# app_name = 'shop'  # имя приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
    # аргумент '' - корневой маршрут для приложения.
    # name='index' - название маршрута
]
