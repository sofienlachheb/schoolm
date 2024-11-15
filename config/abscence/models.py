from django.db import models
from students.models import Student
from teachers.models import Teacher
from grades.models import Grade
from account.models import UserProfile
class Abscence(models.Model):
    sc=(
        ('a','الحصة الأولى'),
        ('b','الحصة الثانية'),
        ('c','الحصة الثالثة'),
        ('d','الحصة الرابعة'),
        ('e','الحصة الخامسة'),
        ('f','الحصة السادسة'),
        ('g','الحصة السابعة'),
    )
    seance=models.CharField(
                             max_length=10,
                             choices=sc,
                             verbose_name='الحصة',
                            ) 
    student = models.ForeignKey(
                                Student,
                                on_delete=models.CASCADE,
                                verbose_name='اسم الطالب',)
    teacher = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,
                                related_name='absences_added',
                                verbose_name='اسم المدرس',)
   
    date = models.DateField()
    grade = models.ForeignKey(
                              Grade,
                              on_delete=models.CASCADE,
                              verbose_name='الصف',
                              )
    
         
    def __str__(self):
        return f"{self.student}كان غائما  {self.date} من {self.reason} (teachers: {', '.join([str(t) for t in self.teachers.all()])})"

