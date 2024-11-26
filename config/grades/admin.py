# admin.py
from django.contrib import admin
from .models import ClassGrade, GradeName, Grade

@admin.register(ClassGrade)
class ClassGradeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GradeName)
class GradeNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_grade')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('code', 'grade_name')