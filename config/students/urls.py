from django.urls import path
from . import views
app_name='students'

urlpatterns = [
    path('', views.student_dashboard, name='student_dashboard'),
   
    path('student_edit/<pk>', views.student_edit, name='student_edit'),
    
    path('student_add', views.student_add, name='student_add'),
    
    path('student_delete/<pk>', views.student_delete, name='student_delete'),
    
    path('upload/', views.upload_file, name='upload_file'),
    
    path('student_list_notes/',views.student_list_notes,name='student_list_notes'),
]