from django.contrib import admin
from . import models


# подключение приложения shop к админпанели
admin.site.register(models.Category)
admin.site.register(models.Course)
# Register your models here.
