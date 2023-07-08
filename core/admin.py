from django.contrib import admin
from core import models


@admin.register(models.Coder)
class Coder(admin.ModelAdmin):
    pass


@admin.register(models.Course)
class Course(admin.ModelAdmin):
    pass


class LessonInline(admin.TabularInline):
    model = models.Lesson
    extra = 0


@admin.register(models.Unit)
class Unit(admin.ModelAdmin):
    inlines = (LessonInline, )


