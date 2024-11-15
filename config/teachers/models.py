from django.db import models
from django.core.validators import RegexValidator
from account.models import User
from grades.models import Grade
from django.core.exceptions import ValidationError
from managers.models import Subjects
class Teacher(models.Model):
        user= models.ForeignKey(User,on_delete=models.CASCADE)
        teacherName=models.CharField(
                                     max_length=200,
                                     verbose_name='اسم المدرس',
                                     ) 
       
        
        teacherFunction = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='teachers')
        mobile_num_regex = RegexValidator(
         regex="^[0-9]{10,15}$", message="رقم الهاتف المحمول الذي تم إدخاله ليس بالتنسيق الصحيح!")
        teacherPhone = models.CharField(
                                       max_length=11,
                                       null=True,
                                       blank=True,
                                       validators=[mobile_num_regex],
                                       verbose_name='رقم الهاتف',
                                      )
        teacherEmail=models.EmailField(
           verbose_name='البريد الالكتروني'
        )
        profile_image = models.ImageField(
                                          null=True,
                                          blank=True,
                                          upload_to='teachers/',
                                          # default='img/avatars/7.jpg',
                                          verbose_name='صورة المدرس')
        
        #you must put many to many relations between teacher and grades
        grades = models.ManyToManyField(Grade, related_name='teachers')
        
        def __str__(self):
               return str(self.teacherName)
        class Meta:
           ordering = ['teacherName']

        