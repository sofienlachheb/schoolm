from django.urls import path,include
from . import views

app_name = 'abscence'

urlpatterns = [
    
    #url for abscence 
    path('', views.abscence_list, name='abscence_list'),
    path('abscence_add', views.abscence_add, name='abscence_add'),
    path('abscence_edit/<int:pk>', views.abscence_edit, name='abscence_edit'),
    path('abscence_delete/<int:pk>', views.abscence_delete, name='abscence_delete'),
   
   
]
