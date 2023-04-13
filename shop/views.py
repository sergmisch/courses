from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Category, Course
# . перед models означает импорт из текущей папки


def index(request):
    courses = Course.objects.all()  # Создаем QuerySet объект из модели Course
    return render(request, 'courses.html', {'courses': courses})


# аргумент 'course_id' получаем из файла urls.py из аргумента функции path()
def single_course(request, course_id):
    # который изначально приходит из адреса в строке браузера
    # # вывод страницы 404 способ 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    # вывод страницы 404 способ 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'single_course.html', {'course': course})
