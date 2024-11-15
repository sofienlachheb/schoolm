from django.urls import path
from . import views
app_name='notes'

urlpatterns = [
   
    path('students/<int:pk>/notes/create/', views.create_note, name='create_note'),
    
    path('students/<int:pk>/notes/<int:note_pk>/update/', views.update_note, name='update_note'),
   
    path('students/<int:pk>/notes/<int:note_pk>/delete/', views.delete_note, name='delete_note'),
 
    
    
    path('students/<int:pk>/notes/', views.student_notes, name='student_notes'),
   
]