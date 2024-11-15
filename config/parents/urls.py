from django.urls import path, include
from . import views
from .views import import_parents
app_name = 'parents'
urlpatterns = [
    path('',views.parent_dashboard,name='parent_dashboard'),
    path('parent_add',views.parent_add,name='parent_add'),
    path('parent_edit/<int:pk>',views.parent_edit,name='parent_edit'),
    path('parent_delete/<int:pk>',views.parent_delete,name='parent_delete'),
    path('import_parents/', import_parents, name='import_parents'),
]
