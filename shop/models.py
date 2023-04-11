from django.db import models
from django.utils import timezone
from django.contrib import admin

admin.ModelAdmin.ordering = ['title']


class Category(models.Model):
    # Модель Category - это наш класс, созданный из родительского класса models.Model
    # Здесь мы задаем параметры таблицы для базы данных
    title = models.CharField(max_length=255)
    # создаем атрибут title. CharField - это класс строка
    # и задаем максимальную длину max_length
    # Это первый столбец таблицы
    created_at = models.DateTimeField(default=timezone.now)
    # Это время создания категории. Это второе поле или иначе столбец
    # admin.ModelAdmin.ordering = ['title']
    link = models.URLField()

    def __str__(self):
        return self.title


# модель "Courses" будет находиться внутри модели "Category"


class Course(models.Model):
    # Создаем еще один класс для таблицы курсов
    title = models.CharField(max_length=127)
    price = models.FloatField()  # Цена - число с плавающей точкой
    students_qty = models.IntegerField()  # Количество студентов - целое число
    reviews_qty = models.IntegerField()  # Кол-во отзывов
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Это поле нужно добавлять для привязки к вышестоящей категории
    # .ForeignKey - это соотношение "многие к одному".
    # Аргумент Category - то, к чему привязываем.
    # Аргумент on_delete=models.CASCADE означает, что
    # при удалении Категории будут удаляться все курсы внутри этой категории
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
