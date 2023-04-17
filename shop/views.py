from django.shortcuts import render, get_object_or_404
from django import http
from .models import Category, Course
# . перед models означает импорт из текущей папки


def index(request):
    # Создаем QuerySet объект из модели Course
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


# аргумент 'course_id' получаем из файла urls.py из аргумента функции path()
def single_course(request, course_id):
    # который изначально приходит из адреса в строке браузера
    # # вывод страницы 404 способ 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    # вывод страницы 404 способ 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})
