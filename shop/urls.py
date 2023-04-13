from django.urls import path
from . import views  # . означает, что импортируем из текущей папки

app_name = 'shop'  # имя приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
    # аргумент '' - корневой маршрут для приложения.
    # name='index' - название маршрута
]
