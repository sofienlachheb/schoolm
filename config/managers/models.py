from django.db import models
from django.db.models import Count

class Subjects(models.Model):
    subjectName=models.CharField(max_length=100,verbose_name='اسم المادة')
    photo = models.ImageField(
    null=True,
    blank=True,
    upload_to='subjects/',
    default='img/default_subject.jpg',
    verbose_name='صورة المادة'
)
    def __str__(self):
            return self.subjectName 
class SiteSetting(models.Model):    
 
    # Fields
    school_name = models.CharField(
        max_length=20,
        verbose_name="اسم المدرسه",
    )
    school_logo = models.ImageField(
        upload_to="manager/school_logo/",
        verbose_name="لوجو مدرسه",
    )
    favicon = models.ImageField(
        upload_to="manager/school_logo/",
        verbose_name=" ايقونة الموقع",
        null=True,
        blank=True,
    )
    # Metadata
    class Meta:
        verbose_name = 'إعدادات الموقع'
        # Methods
    def __str__(self):
        return self.school_name
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')