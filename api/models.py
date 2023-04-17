from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['created_at', 'reviews_qty']
        # список полей, которые не будут передаваться клиенту
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):  # влияет на то, как обрабатываются данные от клиента
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        # это метод влияет на то, как приходят данные клиенту
        bundle.data['category'] = bundle.obj.category
        bundle.data['category_id'] = bundle.obj.category_id
        # добавление поля 'category' в json вывод
        return bundle

    def dehydrate_title(self, bundle):
        # в возвращаемых клиенту данных содержимое поля 'title' будет заглавными буквами
        return bundle.data['title'].upper()
