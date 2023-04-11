from django.urls import path
from . import views  # . означает, что импортируем из текущей папки

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/courses_1/', views.courses_1, name='courses_1'),
    # аргумент '' - корневой маршрут для приложения.
    # name='index' - название маршрута
]
