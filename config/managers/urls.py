from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account import views
from .import views
app_name = 'managers'

urlpatterns = [
    path('', views.manager_dashboard, name='manager_dashboard'),
    
#######              Subjects              #########################################
    path('all_subjects/', views.all_subjects, name='all_subjects'),
    path('subjects_add/', views.subjects_add, name='subjects_add'),
    path('subject_edit/<pk>/', views.subjects_edit, name='subjects_edit'),
    path('subject_delete/<pk>/', views.subject_delete, name='subject_delete'),

########              Site Settign            ######################################    
    path('all_settings/', views.all_settings, name='all_settings'),
    path('setting_add/', views.setting_add, name='setting_add'),
    path('setting_edit/<pk>', views.setting_edit, name='setting_edit'),
    path('setting_delete/<pk>', views.setting_delete, name='setting_delete'),
########              uplod files            ######################################  
   path('upload_users/', views.upload_users, name='upload_users'),
]
