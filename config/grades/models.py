from django.db import models

class Grade(models.Model):
    name=models.CharField( max_length=50)
    class Meta:
            verbose_name = "اسم الصف"
    def __str__(self):
        return self.name
    