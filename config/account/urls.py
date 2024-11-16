# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
  # path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('user/password-change/', views.ChangePasswordView.as_view(), name='change_password'),
    path('user/password-done/', views.password_change_done, name="user_password_done"),
    path('all_users/',views.all_users,name='all_users'),
    path('user_edit/<pk>',views.user_edit,name='user_edit'),
    path('user_delete/<pk>',views.user_delete,name='user_delete'),

]