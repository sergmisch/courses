from django.contrib import admin
from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    # fields = ['title', 'price']
    list_display = ['title', 'category']
    list_display_links = ['title', 'category']
    ordering = ['title']
    radio_fields = {"category": admin.VERTICAL}


admin.site.register(models.Category)
# admin.site.register(models.Course)
# admin.site.register(models.Course, CourseAdmin)
# Register your models here.
