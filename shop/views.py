from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Course
# . перед models означает импорт из текущей папки


def index(request):
    courses = Course.objects.all()  # Создаем QuerySet объект из модели Course
    return render(request, 'courses.html', {'courses': courses})



def single_course(request, course_id): # аргумент 'course_id' получаем из файла urls.py из аргумента функции path()
    # который изначально приходит из адреса в строке браузера
    course = Course.objects.get(pk=course_id)
    return render(request, 'single_course.html', {'course': course})
