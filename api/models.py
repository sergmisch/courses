from tastypie.resources import ModelResource
from shop.models import Category, Course


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resourses_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resourses_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']