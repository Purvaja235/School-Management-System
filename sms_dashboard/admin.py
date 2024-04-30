from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Student)
admin.site.register(models.Staff)
admin.site.register(models.StudentClass)
admin.site.register(models.Class)
