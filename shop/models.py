from django.db import models
from django.utils import timezone
from django.contrib import admin


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
    link = models.CharField(max_length=100)
    sort_key = models.CharField(max_length=50, default='id')

    def __str__(self):
        return self.title


# модель "Courses" будет находиться внутри модели "Category"


class Course(models.Model):
    # class Meta:
    #     ordering = ['category', 'title']

    # Создаем еще один класс для таблицы курсов
    title = models.CharField(max_length=127)
    # Цена - число с плавающей точкой
    price = models.FloatField()
    # Количество студентов - целое число
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()  # Кол-во отзывов
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Это поле нужно добавлять для привязки к вышестоящей категории
    # .ForeignKey - это соотношение "многие к одному".
    # Аргумент Category - то, к чему привязываем.
    # Аргумент on_delete=models.CASCADE означает, что
    # при удалении Категории будут удаляться все курсы внутри этой категории
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.title


# admin.ModelAdmin.ordering = ['title']
