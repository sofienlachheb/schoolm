from django.db import models
from django.core.validators import RegexValidator
from django.db import models

from account.models import User
# Create your models here.
class Parent(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    parentName=models.CharField(max_length=50,verbose_name='اسم ولي الأمر' ,null=True, blank=True)
    mobile_num_regex = RegexValidator(
         regex="^[0-9]{10,15}$", message="رقم الهاتف المحمول الذي تم إدخاله ليس بالتنسيق الصحيح!")
    
    parentPhone = models.CharField(
                                       max_length=13,
                                       null=True,
                                       blank=True,
                                       validators=[mobile_num_regex],
                                       verbose_name='رقم الهاتف',
                                      )
    
    def __str__(self):
        return str(self.parentName)
    