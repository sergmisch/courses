from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Course
# . перед models означает импорт из текущей папки


def index(request):
    courses = Course.objects.all()  # Создаем QuerySet объект из модели Course
    return render(request, 'courses.html', {'courses': courses})


def categories(request):
    # Создаем QuerySet объект из модели Course
    categories = Category.objects.all()  # Создаем QuerySet объект из модели Course
    return render(request, 'categories.html', {'categories': categories})


def courses_1(request):
    courses = Course.objects.filter(category_id=1)
    return render(request, 'courses.html', {'courses': courses})
