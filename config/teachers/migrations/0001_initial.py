# Generated by Django 5.1 on 2024-11-09 18:00

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("grades", "0001_initial"),
        ("managers", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "teacherName",
                    models.CharField(max_length=200, verbose_name="اسم المدرس"),
                ),
                (
                    "teacherPhone",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="رقم الهاتف المحمول الذي تم إدخاله ليس بالتنسيق الصحيح!",
                                regex="^[0-9]{10,15}$",
                            )
                        ],
                        verbose_name="رقم الهاتف",
                    ),
                ),
                (
                    "teacherEmail",
                    models.EmailField(max_length=254, verbose_name="البريد الالكتروني"),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="teachers/",
                        verbose_name="صورة المدرس",
                    ),
                ),
                (
                    "grades",
                    models.ManyToManyField(related_name="teachers", to="grades.grade"),
                ),
                (
                    "teacherFunction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teachers",
                        to="managers.subjects",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["teacherName"],
            },
        ),
    ]
