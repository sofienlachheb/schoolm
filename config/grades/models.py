from django.db import models
from django.db.models import Count

class ClassGrade(models.Model):
    CLASS_CHOICES = (
        ('إبتدائي', 'إبتدائي'),
        ('إعدادي', 'إعدادي'),
        ('ثانوي', 'ثانوي'),
    )
    name = models.CharField(choices=CLASS_CHOICES, max_length=50, verbose_name="المرحلة")

    class Meta:
        verbose_name = "المرحلة الدراسية"
        verbose_name_plural = "المراحل الدراسية"

    def __str__(self):
        return self.class_grade

class GradeName(models.Model):
    GRADE_CHOICES = (
        ('الصف الأول', 'الصف الأول'),
        ('الصف الثاني', 'الصف الثاني'),
        ('الصف الثالث', 'الصف الثالث'),
        ('الصف الرابع', 'الصف الرابع'),
        ('الصف الخامس', 'الصف الخامس'),
        ('الصف السادس', 'الصف السادس'),
        ('الصف السابع', 'الصف السابع'),
        ('الصف الثامن', 'الصف الثامن'),
        ('الصف التاسع', 'الصف التاسع'),
        ('الصف العاشر', 'الصف العاشر'),
        ('الصف الحادي عشر', 'الصف الحادي عشر'),
        ('الصف الثاني عشر', 'الصف الثاني عشر'),
    )
    class_grade = models.ForeignKey(ClassGrade, on_delete=models.CASCADE, related_name="grade_names")
    name = models.CharField(choices=GRADE_CHOICES, max_length=50, verbose_name="اسم الشعبة")

    class Meta:
        verbose_name = "الشعبة"
        verbose_name_plural = "الشعب"

    def __str__(self):
        return f"{self.name} ({self.class_grade.name})"

class Grade(models.Model):
    grade_name = models.ForeignKey(GradeName, on_delete=models.CASCADE, related_name='grades')
    code = models.CharField(max_length=50, verbose_name='اسم الصف')

    class Meta:
        verbose_name = "اسم الصف"
        verbose_name_plural = "الصفوف"

    def __str__(self):
        return f"{self.code} ({self.grade_name.name})"

    @classmethod
    def count_grades_by_gradeName(cls):
        # Annotate the count of grades grouped by grade_name
        return cls.objects.values('grade_name__gradename').annotate(count=Count('grade_name'))
