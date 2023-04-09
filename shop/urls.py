from django.urls import path
from . import views  # . означает, что импортируем из текущей папки

urlpatterns = [
    path('', views.index, name='index'),
    path('testpage/', views.testpage, name='testpage')
    # аргумент '' - корневой маршрут для приложения.
    # name='index' - название маршрута
]
