# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    is_admin= models.BooleanField('مدير الموقع', default=False)
    is_teacher = models.BooleanField('مدرس', default=False)
    is_student = models.BooleanField('طالب', default=False)
    is_parent = models.BooleanField('ولي أمر', default=False)
   
    @property
    def parent_count(self):
        parents = User.objects.filter(is_parent=True, is_active=True).count()
        return parents

    @property
    def teacher_count(self):
        teachers = User.objects.filter(is_teacher=True, is_active=True).count()
        return teachers

    @property
    def student_count(self):
        students = User.objects.filter(is_student=True, is_active=True).count()
        return students