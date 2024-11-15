from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_grades/',views.teacher_grades,name='teacher_grades'),
    path('teacher_list', views.teacher_list, name='teacher_list'),
    path('teacher_add', views.teacher_add, name='teacher_add'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher_edit/<int:pk>', views.teacher_edit, name='teacher_edit'),
    path('teacher_delete/<int:pk>', views.teacher_delete, name='teacher_delete'),
    path('import_teachers/', views.import_teachers, name='import_teachers'),
    
]
