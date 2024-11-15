from django.urls import path
from . import views
app_name='grades'
urlpatterns = [
    path('', views.grade_list, name='grade_list'),
    path('grade_edit/<pk>', views.grade_edit, name='grade_edit'),
    path('grade_add', views.grade_add, name='grade_add'),
    path('grade_delete/<pk>', views.grade_delete, name='grade_delete'),
    
]