from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Course
# . перед models означает импорт из текущей папки


def index(request):  # назвали index , т.к. она будет отвечать за то,
    # что возвращается при обрашении на главную страницу приложения shop
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def testpage(request):
    return HttpResponse("Это тестовая страница")
