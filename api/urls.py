from django.urls import path, include  # добавляем импорт include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')  # вариант с версией api


api.register(CourseResource())  # вариант с версией api
api.register(CategoryResource())  # вариант с версией api
# регистрация в API сервисе

# Пути для api:
# api/v1/courses/         GET, POST
# api/v1/courses/1/       GET, DELETE
# api/v1/categories/      GET
# api/v1/categories/1/    GET

urlpatterns = [
    path('', include(api.urls), name='index')
]
