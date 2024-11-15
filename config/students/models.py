from django.db import models
from grades.models import Grade
from account.models import User
from parents.models import Parent
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey(Parent, 
                               on_delete=models.SET_NULL, 
                               null=True,
                               blank=True,default='')
    grade=models.ForeignKey(
                                Grade, null=True,
                                on_delete= models.SET_NULL,verbose_name='الصف'
                                )
    name=models.CharField( max_length=50,verbose_name='اسم الطالب')
    #إضافة مرض للطالب إن كان يعاني من مرض
    
    roll_number = models.CharField(max_length=20, unique=True,verbose_name='رقم الطالب')
    def __str__(self):
        return f"{self.name} - {self.grade.name} - {self.roll_number}"
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')