from django.contrib import admin
from .models import Category, Course

admin.site.site_header = "Courses admin"  # меняем заголовок
admin.site.site_title = "My Courses"  # меняем название вкладки в браузере
# приветствие на странице admin:
admin.site.index_title = "Welcome to the courses admin area"


# класс для отображения дополнительных полей на странице курсов:
class CourseAdmin(admin.ModelAdmin):
    # какие поля будем отображать:
    list_display = ('title', 'price', 'category')
    ordering = ['title', 'category']  # по каким полям сортировка


# класс для вставки таблицы курсов на другие страницы:
class CourseInline(admin.TabularInline):
    model = Course  # модель таблицы
    exclude = ['created_at']  # какие поля хотим исключить
    extra = 1  # сколько рядов полей для добавления курса


# класс для отображения дополнительных полей на странице категорий:
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # какие поля будем отображать
    fieldsets = [                          # дополнительные поля на странице одной категории
        (None, {'fields': ['title']}),
        ('Dates',
         {
             'fields': ['created_at'],
             'classes':['collapse']
         }
         )
    ]
    # отображение таблицы классов, привязанных к текущей категории:
    inlines = [CourseInline]


# подключение приложения shop к админпанели
# не забыть зарегистрировать класс CategoryAdmin:
admin.site.register(Category, CategoryAdmin)
# не забыть зарегистрировать класс CourseAdmin:
admin.site.register(Course, CourseAdmin)
